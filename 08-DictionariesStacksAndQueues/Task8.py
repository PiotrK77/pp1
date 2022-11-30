person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person["name"])
print(person["hobby"])
person["surname"] = "Nowak"
print(person["surname"])
person["married"] = False
person["gender"] = "male"
print(person["gender"])
person["hobby"] += ["bicycle"]
print(person["hobby"])
person["phone"]
print(person["phone"])
person["phone"]["work"] = "313131444"
print(person["phone"])