icao = {"a": "Alpha", "b": "Bravo", "c": "Charlie"}

text = input("Enter text: ")
spelledText = ""
for i in range(0, len(text)):
    spelledText += icao[text[i]] + " "
print(spelledText)