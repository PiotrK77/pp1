DogAgeInHumanYrs = int(input("Enter the dog's age in human years: "))
DogAgeInDogYrs = None

if DogAgeInHumanYrs <= 2:
    DogAgeInDogYrs = DogAgeInHumanYrs / 2 * 21
else:
    DogAgeInHumanYrs -= 2
    DogAgeInDogYrs = DogAgeInHumanYrs * 4 + 21

print(f"The dog's age in dog's years is {DogAgeInDogYrs} years")
