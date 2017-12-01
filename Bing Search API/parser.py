import requests, re, csv

from bs4 import BeautifulSoup

with open('final.csv', 'a', newline = '') as l:

    fieldnames = ['NAME', 'URL','EMAIL']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    toParse = []

    with open('urlList.csv', 'r') as f:

        urlList = csv.reader(f, delimiter = ',')

        for item in urlList:

        #for link in toParse:

            r = requests.get(item[1])

            emails = re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

            writer.writerow({'NAME': item[0],'URL':item[1], 'EMAIL':[email[7:] for email in emails]})

             #([email[7:] for email in emails])
