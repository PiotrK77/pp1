mobile = {
    "color" : "black",
    "memory" : "64GB",
    "size" : "6 inches",
    "year": 2020,
    "system": "IOS",
    "camera": "12 mp",
    "warranty": True

}

x = mobile.items()

print(x)

for (key, value) in mobile.items():
    print(key, value)