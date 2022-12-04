with open('07-FileHandling/filmTitles.txt', 'r') as f:
    for line in f:
        print(line, end = "")
    f.close()