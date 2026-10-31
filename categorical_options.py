import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Electric_Vehicle_Population_Data.csv"
OUTPUT_PATH = BASE_DIR / "categorical_options.json"

if not DATA_PATH.exists():
    raise FileNotFoundError(f"❌ Could not find dataset at {DATA_PATH}")

print(f"📂 Loading dataset from {DATA_PATH}...")
df = pd.read_csv(DATA_PATH)

options_dict = {}

for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        unique_values = sorted([str(val) for val in df[col].dropna().unique()])
        options_dict[col] = unique_values

with open(OUTPUT_PATH, "w", encoding="utf-8") as out_f:
    json.dump(options_dict, out_f, indent=4)

print(f"✅ Successfully generated `{OUTPUT_PATH.name}` with {len(options_dict)} categorical features and their unique sub-features!")