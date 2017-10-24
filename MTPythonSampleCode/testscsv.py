import csv

"""with open('test.csv', 'r') as f:

    

    reader = csv.DictReader(f,delimiter=',')

    for row in reader:

        row['Title'] = 'Hello'

        row['ID'] = 1

        row['ru'] ='Russian'

        row['sp'] = 'Spanish'

        row['du'] = 'Dutch'"""

with open('out.csv', 'a') as l:

    fieldnames = ['Title','ID','ru','sp','du']
    
    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    with open('test.csv','r') as f:

        reader = csv.reader(f, delimiter=',')

        for row in reader:

            writer.writerow({'Title': row[0],'ID':row[1], 'ru':row[2],'sp':row[3],'du':row[4]})
    
    """
    for row in reader:

        writer.writerow(row)
    """
