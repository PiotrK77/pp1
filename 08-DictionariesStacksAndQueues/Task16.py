import json
import numpy

file = open("08-DictionariesStacksAndQueues/students.json", "r")
limited = open("08-DictionariesStacksAndQueues/limited.json", "w")

content = file.read()
list = json.loads(content)
print(type(list))
for i in list:
    print(i)



file.close()
