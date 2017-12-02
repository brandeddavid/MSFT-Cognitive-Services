import requests, re, csv

from bs4 import BeautifulSoup

with open('final.csv', 'a', newline = '') as l:

    fieldnames = ['NAME', 'URL','EMAILS', 'PHONES']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    toParse = []

    with open('urlList.csv', 'r') as f:

        urlList = csv.reader(f, delimiter = ',')

        for item in urlList:

        #for link in toParse:

            r = requests.get(item[1])

            emails = re.findall(r'[0-9a-zA-Z\@\.]{1,}', r.text)

            phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

            #[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4} Best so far
            #(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}) Works just fine
            #\:[\(\)\-0-9\ ]{1,} Works jumbled up
            #\"tel\:[\(\)\-0-9\ ]{1,}\" Worls no results
            #(9\d)\s+(\d{2})\s+(\d{2})\s+(\d{3}) Works no results
            #(1[-.])*([2-9]\d{2})?[-. ]\d{3}[-. ]\d{4} Works a bit

            writer.writerow({'NAME': item[0],'URL':item[1], 'EMAILS':[email for email in emails], 'PHONES':[phone for phone in phones]})

             #([email[7:] for email in emails])
