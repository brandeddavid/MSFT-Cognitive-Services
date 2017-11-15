import csv

with open('test.csv', 'r') as f:

    toSearch = []
    notFound = []

    words = csv.reader(f, delimiter = ',')

    for word in words:

        toSearch.append(word[0] + " gifs")


print(toSearch)
