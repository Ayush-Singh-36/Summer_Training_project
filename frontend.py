import json
import os
import pickle as pk
import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="EV Price Prediction Portal", 
    layout="wide"
)

MODEL_PATH = os.getenv("MODEL_PATH", "model_artifact.pkl")
OPTIONS_JSON_PATH = os.getenv("OPTIONS_JSON_PATH", "categorical_options.json")


# --- HELPER: CACHE & LOAD MODEL ARTIFACT ---
@st.cache_resource
def load_model_artifact(path: str):
    """Loads and caches the pickled model pipeline locally in memory."""
    try:
        with open(path, "rb") as file:
            return pk.load(file)
    except Exception as e:
        st.error(f"❌ Error loading pickle file from path '{path}': {e}")
        return None


# --- HELPER: CACHE & LOAD CATEGORICAL OPTIONS JSON ---
@st.cache_data(ttl=3600)
def load_categorical_options(json_path: str) -> dict:
    """Reads categories directly from categorical_options.json file."""
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            st.warning(f"⚠️ Could not parse '{json_path}': {e}")
            return {}
    return {}


loaded_artifact = load_model_artifact(MODEL_PATH)
options_data = load_categorical_options(OPTIONS_JSON_PATH)

# Extract lists using JSON values with robust fallback lists
makes = options_data.get("Make", ["NISSAN", "TESLA", "CHEVROLET", "FORD"])
models = options_data.get("Model", ["LEAF", "MODEL 3", "VOLT", "BOLT EV"])
states = options_data.get("State", ["WA", "CA", "NY"])
counties = options_data.get("County", ["King", "Pierce", "Snohomish", "Unknown"])
cities = options_data.get("City", ["Seattle", "Tacoma", "Bellevue", "Unknown"])
cafv_options = options_data.get(
    "Clean Alternative Fuel Vehicle (CAFV) Eligibility",
    [
        "Clean Alternative Fuel Vehicle Eligible",
        "Eligibility unknown as battery range has not been researched",
        "Not eligible due to low range"
    ],
)
ev_types = options_data.get(
    "Electric Vehicle Type",
    [
        "Battery Electric Vehicle (BEV)",
        "Plug-in Hybrid Electric Vehicle (PHEV)",
    ],
)


# --- USER INTERFACE FORM ---
st.title("Electric Vehicle Analysis Dashboard")
st.caption("Standalone interactive UI executing local model inference.")

with st.form("ev_features_ingst_form"):
    # BLOCK A: CATEGORICAL FEATURES
    st.subheader("📁 Categorical Vehicle Parameters")
    cat_col_1, cat_col_2, cat_col_3 = st.columns(3)

    with cat_col_1:
        ui_make = st.selectbox("Select Vehicle Make", options=makes)
        ui_model = st.selectbox("Select Vehicle Model", options=models)

    with cat_col_2:
        ui_state = st.selectbox("Select Registration State", options=states)
        ui_county = st.selectbox("Select County", options=counties)

    with cat_col_3:
        ui_city = st.selectbox("Select City", options=cities)
        ui_ev_type = st.selectbox("Select EV Type", options=ev_types)

    ui_cafv = st.selectbox(
        "CAFV Eligibility Status", 
        options=cafv_options
    )

    st.markdown("---")

    # BLOCK B: NUMERICAL METRICS
    st.subheader("🔢 Numerical Metric Parameters")
    num_col_1, num_col_2 = st.columns(2)

    with num_col_1:
        ui_model_year = st.slider(
            "Model Year", min_value=1990, max_value=2026, value=2020
        )

    with num_col_2:
        ui_electric_range = st.number_input(
            "Electric Range (Miles)",
            min_value=0.0,
            value=150.0,
            step=10.0,
        )

    execute_submission = st.form_submit_button("Submit")


# --- LOCAL INFERENCE & RESPONSE RENDERING ---
if execute_submission:
    if loaded_artifact is None:
        st.error("🔴 Model artifact missing or failed to load. Check server log/path.")
    else:
        with st.spinner("Processing feature vector & executing local inference..."):
            try:
                # 1. Map input payload keys directly to training column names
                formatted_dict = {
                    "County": str(ui_county).strip(),
                    "City": str(ui_city).strip(),
                    "State": str(ui_state).strip(),
                    "Make": str(ui_make).strip(),
                    "Model": str(ui_model).strip(),
                    "Model Year": int(ui_model_year),
                    "Electric Vehicle Type": str(ui_ev_type).strip(),
                    "Clean Alternative Fuel Vehicle (CAFV) Eligibility": str(ui_cafv).strip(),
                    "Electric Range": float(ui_electric_range),
                }

                # 2. Convert payload to DataFrame
                input_df = pd.DataFrame([formatted_dict])

                # 3. Local Prediction - Unpack artifact dictionary & transform data
                preprocessor = loaded_artifact["preprocessor"]
                scaler = loaded_artifact["scaler"]
                kmeans_model = loaded_artifact["kmeans_model"]

                processed_data = preprocessor.transform(input_df)
                scaled_data = scaler.transform(processed_data)

                raw_pred = kmeans_model.predict(scaled_data)
                pred_val = int(raw_pred[0])

                # 4. Display Results
                st.markdown("### 📊 Inference Diagnostic Readouts")
                st.success("✅ Local Model Inference Completed Successfully!")

                st.metric(
                    label="Assigned Cluster Segment ID",
                    value=f"Cluster {pred_val}",
                )

            except Exception as e:
                st.error(f"❌ Internal Model Execution Fault: {str(e)}")
