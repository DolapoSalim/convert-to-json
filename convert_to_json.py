import pandas as pd

file_path = input('Enter the file path remove quotes: ')  # Achalugo remove the quotes before pressing enter
df = pd.read_csv(file_path, delimiter=",", encoding="ISO-8859-1")  # Ensure the delimiter matches your file
json_output = df.to_json(orient="records", indent=4)
output_path = input('Enter the path to save directory: ')
output_file_path = output_path + "\\convertfileinjson.json"
with open(output_file_path, "w") as f:
    f.write(json_output)
print(json_output)