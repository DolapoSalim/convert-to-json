import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(script_dir, "FILE.csv")

df = pd.read_csv(csv_path, delimiter=",")

json_output = df.to_json(orient="records", indent=4)

with open(r"FILE_PATH", "w") as f:
    f.write(json_output)

print(json_output)