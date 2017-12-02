import requests, re, csv

from bs4 import BeautifulSoup

with open('final.csv', 'a', newline = '') as l:

    fieldnames = ['name', 'url','emails', 'phone-numbers','search-condition', 'http status']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    toParse = []

    with open('urlList.csv', 'r') as f:

        urlList = csv.reader(f, delimiter = ',')

        for item in urlList:

            r = requests.get(item[1])

            emails = re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

            #phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

            if len(re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)) == 0:

                phones = re.findall(r'[\d]{3}.?[\d]{3}.[\d]{4}', r.text)

            else:

                phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

            #[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4} Best so far
            #(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}) Works just fine
            #\:[\(\)\-0-9\ ]{1,} Works jumbled up
            #\"tel\:[\(\)\-0-9\ ]{1,}\" Worls no results
            #(9\d)\s+(\d{2})\s+(\d{2})\s+(\d{3}) Works no results
            #(1[-.])*([2-9]\d{2})?[-. ]\d{3}[-. ]\d{4} Works a bit

            writer.writerow({'name': item[0],'url':item[1], 'emails':[email[7:] for email in emails], 'phone-numbers':[phone for phone in phones], 'search-condition':'intitle:Contact (ELL OR ESL)  site:.us ("public school" OR "public schools")', 'http status':r.status_code})
