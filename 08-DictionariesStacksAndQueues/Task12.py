import json

favourite = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5",}

jsonObject = json.dumps(favourite, indent = 4)

favouriteFile = open("08-DictionariesStacksAndQueues/favourite.json", "w")

favouriteFile.write(jsonObject)
favouriteFile.close()
