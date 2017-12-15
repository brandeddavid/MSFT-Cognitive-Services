import requests, re, csv, os, sys
from urllib import request
from bs4 import BeautifulSoup

urlList = []

with open('resultscombined.csv', 'r') as k:

    reader = csv.reader(k, delimiter = ',')

    for item in reader:

        urlList.append(item[1])

with open('Results.csv', 'a', newline = '') as l:

    fieldnames = ['emails', 'http status']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    for url in urlList:

        print ('Url '+ str(urlList.index(url)+1) + ' of ' + str(len(urlList)))

        try:

            r = requests.get(url)

            #email1 = re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

            #emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', r.text)
            emails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', r.text)


        except:

            pass

        writer.writerow({'emails':[email[7:] for email in emails], 'http status':r.status_code})

        emails = []
