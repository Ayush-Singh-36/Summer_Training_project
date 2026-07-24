import os
import requests
import streamlit as st

st.set_page_config(
    page_title="EV Price Prediction Portal", 
    layout="wide"
)

# --- BACKEND URL CONFIGURATION ---
BACKEND_BASE_URL = os.getenv("BACKEND_API_URL", "http://localhost:8000").rstrip("/")
PREDICT_URL = f"{BACKEND_BASE_URL}/predict"
OPTIONS_URL_TEMPLATE = f"{BACKEND_BASE_URL}/options/{{}}"


# --- HELPER: FETCH CATEGORICAL OPTIONS ---
@st.cache_data(ttl=3600)
def fetch_options_from_backend(feature_name: str):
    try:
        response = requests.get(OPTIONS_URL_TEMPLATE.format(feature_name))
        if response.status_code == 200:
            return response.json().get("options", [])
        return []
    except Exception:
        return []


# Load categorical dynamic choices at UI startup
makes = fetch_options_from_backend("Make")
models = fetch_options_from_backend("Model")
states = fetch_options_from_backend("State")
ev_types = fetch_options_from_backend("Electric Vehicle Type")


# --- USER INTERFACE FORM ---
st.title("Electric Vehicle Analysis Dashboard")
st.caption(
    "Interactive UI for model inference connected directly to FastAPI backend with dynamic validation."
)

with st.form("ev_features_ingst_form"):
    # BLOCK A: CATEGORICAL FEATURES
    st.subheader("📁 Categorical Vehicle Parameters")
    cat_col_1, cat_col_2 = st.columns(2)

    with cat_col_1:
        ui_make = st.selectbox(
            "Select Vehicle Make",
            options=makes if makes else ["NISSAN", "TESLA", "CHEVROLET", "FORD"],
        )
        ui_model = st.selectbox(
            "Select Vehicle Model",
            options=models if models else ["LEAF", "MODEL 3", "VOLT", "BOLT EV"],
        )

    with cat_col_2:
        ui_state = st.selectbox(
            "Select Registration State", 
            options=states if states else ["WA", "CA", "NY"],
        )
        ui_ev_type = st.selectbox(
            "Select Electric Vehicle Type",
            options=ev_types if ev_types else [
                "Battery Electric Vehicle (BEV)",
                "Plug-in Hybrid Electric Vehicle (PHEV)",
            ]
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


# --- NETWORK TRANSPORT & RESPONSE RENDERING ---
if execute_submission:
    payload_map = {
        "Make": ui_make,
        "Model": ui_model,
        "State": ui_state,
        "Electric_Vehicle_Type": ui_ev_type,
        "Model_Year": int(ui_model_year),
        "Electric_Range": float(ui_electric_range),
    }

    with st.spinner("Processing feature vector... Requesting Inference..."):
        try:
            api_response = requests.post(PREDICT_URL, json=payload_map)

            if api_response.status_code == 200:
                result = api_response.json()
                predicted_price = result.get("prediction", {}).get(
                    "predicted_price", 0.0
                )

                st.markdown("### 📊 Inference Diagnostic Readouts")
                st.success("✅ Model Inference Completed Successfully!")

                # Render continuous estimated price cleanly
                st.metric(
                    label="Estimated Base MSRP / Price",
                    value=f"${predicted_price:,.2f}",
                )

            else:
                st.error(
                    f"Backend rejected payload (HTTP {api_response.status_code}): \n\n `{api_response.text}`"
                )

        except requests.exceptions.ConnectionError:
            st.error(
                f"🔴 Transport Loop Broken: Unable to connect to FastAPI at `{PREDICT_URL}`."
            )