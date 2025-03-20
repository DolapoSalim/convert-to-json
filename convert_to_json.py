import pandas as pd

df = pd.read_csv(r"catami-classification\catami\catami-caab-codes.csv", delimiter=",")  # Ensure the delimiter matches your file

json_output = df.to_json(orient="records", indent=4)

with open(r"catami-classification\catami-caab.json2", "w") as f:
    f.write(json_output)

print(json_output)