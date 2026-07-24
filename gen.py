import json
import pickle
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Electric_Vehicle_Population_Data.csv"
OUTPUT_PATH = BASE_DIR / "categorical_options.json"

df = pd.read_csv(DATA_PATH)
options_dict = {}

for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        options_dict[col] = sorted([str(val) for val in df[col].dropna().unique()])

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(options_dict, f, indent=2)

print("DONE")