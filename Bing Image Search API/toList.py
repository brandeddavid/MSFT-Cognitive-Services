import csv

with open('keywords.csv', 'r') as f:

    toSearch = []

    words = csv.reader(f, delimiter = ',')

    for word in words:

        toSearch.append(word[0])

    print(toSearch)
