import json

data = {
"cientifico": {
"nombre": "Alan Mathison Turing",
"edad": "41"
}
}

with open("json/data_file.json", "w") as write_file:
    json.dump(data, write_file)


json_string = json.dumps(data)
print(json_string, type(json_string))

