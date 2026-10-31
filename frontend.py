import os
import json
import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="EV Price Prediction Dashboard",
    page_icon="⚡",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model_artifact.pkl"
OPTIONS_JSON_PATH = BASE_DIR / "categorical_options.json"

@st.cache_resource
def load_artifacts():
    try:
        if MODEL_PATH.exists():
            return joblib.load(MODEL_PATH)
        return None
    except Exception as e:
        st.error(f"Error loading model artifact: {e}")
        return None

@st.cache_data(ttl=3600)
def load_categorical_options():
    if OPTIONS_JSON_PATH.exists():
        try:
            with open(OPTIONS_JSON_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading categorical options JSON: {e}")
            return {}
    return {}

artifacts = load_artifacts()
options_data = load_categorical_options()

st.title("⚡ Electric Vehicle (EV) Price Prediction")
st.write("Enter the vehicle specifications below. Dropdown options are dynamically loaded from `categorical_options.json`.")

if artifacts is None:
    st.warning("⚠️ Could not find or load `model_artifact.pkl`. Please ensure it is in the same directory.")
else:
    preprocessor = artifacts.get('preprocessor')
    scaler = artifacts.get('scaler')
    model = artifacts.get('kmeans_model') or artifacts.get('model')  # Supporting general model key naming

    # Dynamically fetch unique choices from categorical_options.json with fallbacks
    counties = options_data.get('County', ["Unknown"])
    cities = options_data.get('City', ["Unknown"])
    states = options_data.get('State', ["WA"])
    makes = options_data.get('Make', ["TESLA", "NISSAN"])
    models = options_data.get('Model', ["UNKNOWN"])
    ev_types = options_data.get('Electric Vehicle Type', ["Battery Electric Vehicle (BEV)"])
    cafv_options = options_data.get('Clean Alternative Fuel Vehicle (CAFV) Eligibility', ["Clean Alternative Fuel Vehicle Eligible"])

    with st.form("ev_form"):
        st.subheader("Vehicle Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            county = st.selectbox("County", options=counties)
            city = st.selectbox("City", options=cities)
            state = st.selectbox("State", options=states)
            make = st.selectbox("Make", options=makes)
            model_name = st.selectbox("Model", options=models)
            
        with col2:
            ev_type = st.selectbox("Electric Vehicle Type", options=ev_types)
            cafv_eligibility = st.selectbox("CAFV Eligibility", options=cafv_options)
            model_year = st.number_input("Model Year", min_value=2010, max_value=2030, value=2023, step=1)
            electric_range = st.number_input("Electric Range (miles)", min_value=0, max_value=500, value=250, step=5)

        submit_btn = st.form_submit_button("Predict Price")

    # Handle form submission and model inference
    if submit_btn:
        # Construct input dataframe passing the exact user selections from categorical_options.json
        input_data = pd.DataFrame({
            'County': [county],
            'City': [city],
            'State': [state],
            'Postal Code': [98101],
            'Model Year': [model_year],
            'Make': [str(make).upper()],
            'Model': [model_name],
            'Electric Vehicle Type': [str(ev_type)],
            'Clean Alternative Fuel Vehicle (CAFV) Eligibility': [cafv_eligibility],
            'Electric Range': [electric_range],
            'Base MSRP': [0],
            'Legislative District': [1],
            'DOL Vehicle ID': [1],
            'Vehicle Location': ['POINT(0 0)'],
            'Electric Utility': ['UNKNOWN'],
            '2020 Census Tract': [1]
        })

        try:
            # Apply transformation pipeline using saved artifact components
            if preprocessor is not None:
                processed_input = preprocessor.transform(input_data)
            else:
                processed_input = input_data

            if scaler is not None:
                processed_input = scaler.transform(processed_input)

            # Generate final price prediction using model
            if model is not None and hasattr(model, 'predict'):
                prediction = model.predict(processed_input)
                estimated_price = float(prediction[0])
                st.success(f"Estimated Car Price: ${estimated_price:,.2f}")
            else:
                st.warning("Model prediction interface not detected in artifact bundle.")
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")