countries = [{"country" : "Poland", "popuation" : 37},
             {"country" : "Germany", "population" : 83},
             {"country" : "Netherlands", "population" : 17},
             {"country" : "France", "population" : 67},
             {"country" : "Spain", "population" : 47}]

i = 0
while i < len(countries):
    print()
    for key, value in countries[i].items():
        print(f"{key}: {value},", end = " ")
    i += 1