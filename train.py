import pickle
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# --- FILE PATH SETUP ---
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Electric_Vehicle_Population_Data.csv"
MODEL_OUTPUT = BASE_DIR / "model_artifact.pkl"

# 1. LOAD DATA
df = pd.read_csv(DATA_PATH)

target_col = "Base MSRP"

# =====================================================================
# 📍 STEP 2 CODE GOES HERE (Right after loading data & before training)
# =====================================================================
print(f"📊 Original dataset size: {len(df)} rows")

# Filter out rows where Base MSRP is 0 or unrecorded
df = df[df[target_col] > 0]

print(f"📊 Filtered dataset size (valid MSRP only): {len(df)} rows")
# =====================================================================

# 2. DEFINE FEATURES AND TARGET
categorical_cols = ["Make", "Model", "State", "Electric Vehicle Type"]
numerical_cols = ["Model Year", "Electric Range"]

X = df[categorical_cols + numerical_cols]
y = df[target_col]

# 3. BUILD PIPELINE
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ]
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=100, random_state=42, n_jobs=-1
            ),
        ),
    ]
)

# 4. TRAIN AND SAVE
print("⏳ Fitting Random Forest Regressor...")
pipeline.fit(X, y)

with open(MODEL_OUTPUT, "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model trained on valid prices & saved cleanly!")