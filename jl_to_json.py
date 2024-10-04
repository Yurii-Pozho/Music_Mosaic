import json

input_file = r"C:\Users\user\Desktop\music\data\genres.jl"
output_file = r"C:\Users\user\Desktop\music\app\genres.json"

data = []

with open(input_file, 'r') as f:
    for line in f:
        data.append(json.loads(line))  

with open(output_file, 'w') as f:
    json.dump(data, f, indent=4) 