import os
import pandas as pd

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full file path
csv_path = os.path.join(script_dir, "catami-caab-codes.csv")

# Load CSV
df = pd.read_csv(csv_path, delimiter=",")

json_output = df.to_json(orient="records", indent=4)

with open(r"catami-classification\catami-caab.json3", "w") as f:
    f.write(json_output)

print(json_output)