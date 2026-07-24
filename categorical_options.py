import json
import pickle
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Electric_Vehicle_Population_Data.csv"
MODEL_PATH = BASE_DIR / "model_artifact.pkl"
OUTPUT_PATH = BASE_DIR / "categorical_options.json"

# 1. Load the raw dataset
if not DATA_PATH.exists():
    raise FileNotFoundError(f"❌ Could not find dataset at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# 2. Load the trained model artifact
with open(MODEL_PATH, "rb") as f:
    artifact = pickle.load(f)

# 3. Extract feature names safely using getattr to satisfy static type checkers
expected_features = []

# Scenario A: Dict {"preprocessor": ..., "model": ...}
if isinstance(artifact, dict) and "preprocessor" in artifact:
    preprocessor = artifact["preprocessor"]
    expected_features = getattr(preprocessor, "feature_names_in_", [])

# Scenario B: Single fitted object with feature_names_in_
elif hasattr(artifact, "feature_names_in_"):
    expected_features = getattr(artifact, "feature_names_in_", [])

# Scenario C: Scikit-Learn Pipeline object
elif hasattr(artifact, "named_steps"):
    named_steps = getattr(artifact, "named_steps", {})
    preprocessor = named_steps.get("preprocessor")
    if preprocessor is not None:
        expected_features = getattr(preprocessor, "feature_names_in_", [])

# Fallback: Default to all dataset columns if feature names couldn't be extracted
if len(expected_features) == 0:
    print("⚠️ Could not auto-detect feature_names_in_. Defaulting to all CSV columns...")
    expected_features = df.columns

# 4. Extract options for all non-numeric (categorical) columns
options_dict = {}

# Check against both expected_features AND raw dataframe columns
columns_to_check = [col for col in expected_features if col in df.columns]
if not columns_to_check:
    columns_to_check = df.columns.tolist()

for col in columns_to_check:
    # Match object, category, bool, string, or non-numeric types
    if not pd.api.types.is_numeric_dtype(df[col]):
        options_dict[col] = sorted([str(val) for val in df[col].dropna().unique()])

print(f"✅ categorical_options.json generated with {len(options_dict)} active categorical features!")