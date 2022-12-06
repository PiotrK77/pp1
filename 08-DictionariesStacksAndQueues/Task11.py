import json

with open("08-DictionariesStacksAndQueues/sample1.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(f"{k}: {v}")
