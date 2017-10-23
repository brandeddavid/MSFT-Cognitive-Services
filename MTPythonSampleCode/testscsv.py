import csv

with open('translate.csv', 'r') as f:

    r = csv.reader(f, delimiter=',')

    for row in r:

        print (row)
