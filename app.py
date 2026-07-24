from typing import Any, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle as pk
import uvicorn

app = FastAPI(title="EV Model Prediction Backend API")

MODEL_PATH = "model_artifact.pkl"
loaded_artifact: Any = None

try:
    with open(MODEL_PATH, "rb") as file:
        loaded_artifact = pk.load(file)
    print(f"✅ Success: Model loaded cleanly from '{MODEL_PATH}'.")
except Exception as e:
    print(f"❌ Error loading pickle file: {e}")


class InputData(BaseModel):
    Make: str
    Model: str
    State: str
    Electric_Vehicle_Type: str
    Model_Year: int
    Electric_Range: float


@app.post("/predict")
def predict(data: InputData):
    if loaded_artifact is None:
        raise HTTPException(
            status_code=500,
            detail="Server Error: Model artifact is missing or failed to load.",
        )

    try:
        raw_dict = data.model_dump()

        # 1. Map keys to EXACT CSV/Training column names
        formatted_dict = {
            "Make": str(raw_dict["Make"]).strip(),
            "Model": str(raw_dict["Model"]).strip(),
            "State": str(raw_dict["State"]).strip(),
            "Electric Vehicle Type": str(raw_dict["Electric_Vehicle_Type"]).strip(),
            "Model Year": int(raw_dict["Model_Year"]),
            "Electric Range": float(raw_dict["Electric_Range"]),
        }

        # 2. Create DataFrame with explicit column order matching train.py
        feature_order = [
            "Make",
            "Model",
            "State",
            "Electric Vehicle Type",
            "Model Year",
            "Electric Range",
        ]
        input_df = pd.DataFrame([formatted_dict])[feature_order]

        # 3. Print debug log to Docker terminal to verify input
        print("🔍 INCOMING FEATURE VECTOR:")
        print(input_df)

        # 4. Predict
        raw_pred = loaded_artifact.predict(input_df)
        pred_val = float(raw_pred[0])

        print(f"✅ PREDICTED VALUE: {pred_val}")

        return {
            "prediction": {
                "predicted_price": pred_val,
                "primary_class_label": "Class_Positive" if pred_val > 0 else "Class_Negative",
                "confidence_score_pct": pred_val,
                "alternate_score_pct": 0.0,
            }
        }

    except Exception as e:
        print(f"❌ Prediction Error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Internal Model Execution Fault: {str(e)}"
        )