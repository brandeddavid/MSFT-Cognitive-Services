import requests, re, csv, os, sys
from urllib import request
from bs4 import BeautifulSoup

filenames = []

for name in os.listdir('.'):

    if name.endswith('.csv'):

        filenames.append(name[:-4])


with open('EResults.csv', 'a', newline = '') as l, open('EFinds.csv', 'a', newline='') as f:

    fieldnames = ['name', 'url', 'emails','search-condition', 'http status']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    header = ['name', 'url', 'text']

    writer2 = csv.DictWriter(f, fieldnames=header)

    writer2.writeheader()

    toParse = []

    for name in filenames:

        print ('Scraping ' + name + ' Count '+ str(filenames.index(name)+1) + ' of ' + str(len(filenames)))

        with open(name + '.csv', 'r') as k:

            urlList = csv.reader(k, delimiter = ',')

            for item in urlList:

                try:

                    r = requests.get(item[1])

                    emails = re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

                    writer.writerow({'name': item[0],'url':item[1], 'emails':[email[7:] for email in emails], 'search-condition':item[2], 'http status':r.status_code})

                except:

                    pass

                try:

                    data = request.urlopen(item[1]).read().decode('utf-8')
                    #re.search(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

                    textAfter = ''
                    textBefore = ''

                    for email in emails:
                        details = re.search(email, data)

                        end = details.end()
                        textAft = data[end:end+150]
                        textAfter += textAft

                        start = details.start()
                        textBef = data[start-150:start]
                        textBefore += textBef


                    alltext = textBefore + textAfter
                    soup = BeautifulSoup(alltext, 'lxml')
                    gettext = soup.get_text()
                    alltextfinal = re.sub("\"|\'|>|\r|\xa0","",gettext)

                    writer2.writerow({'name':item[0], 'url':item[1], 'text': alltextfinal})

                except:

                    pass


                #writer.writerow({'name': item[0],'url':item[1], 'emails':[email[7:] for email in emails], 'phone-numbers':[phone for phone in phones], 'search-condition':item[2], 'http status':r.status_code})
                #writer2.writerow({'url':item[1], 'hit':hit, 'text': alltextfinal})
