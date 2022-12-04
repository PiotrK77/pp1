film_titles = ["film1", "film2", "film3", "film4", "film5"]

file = open('07-FileHandling/filmTitles.txt', 'w')

for line in film_titles:
    file.write(f"{line}\n")

file.close()