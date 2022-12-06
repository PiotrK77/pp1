import json

icao = {"a": "Alpha", "b": "Bravo", "c": "Charlie"}

file = open("08-DictionariesStacksAndQueues/icao.json", "w")

file.write(json.dumps(icao, indent = 4)) #indent - amount of spaces in json file
file.close()