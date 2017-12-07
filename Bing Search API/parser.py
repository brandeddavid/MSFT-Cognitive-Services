import requests, re, csv
from urllib import request
from bs4 import BeautifulSoup

with open('final.csv', 'a', newline = '') as l, open('befaft.csv', 'a', newline='') as f:

    fieldnames = ['name', 'url', 'emails', 'phone-numbers','search-condition', 'http status']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    header = ['url', 'hit', 'text']

    writer2 = csv.DictWriter(f, fieldnames=header)

    writer2.writeheader()

    toParse = []

    with open('urlList.csv', 'r') as f:

        urlList = csv.reader(f, delimiter = ',')

        for item in urlList:

            try:

                r = requests.get(item[1])

                emails = re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)


                #phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

                if len(re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)) == 0:

                    phones = re.findall(r'[\d]{3}.?[\d]{3}.[\d]{4}', r.text)

                else:

                    phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

            except:

                pass

            try:

                data = request.urlopen(item[1]).read().decode('utf-8')
                #re.search(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

                textAfter = ''
                textBefore = ''


                if len(emails) == 0:

                    hit = []

                    for phone in phones:
                        details = re.search(phone, data)
                        hit.append(phone)

                        end = details.end()
                        textAft = data[end:end+200]
                        textAfter += textAft

                        start = details.start()
                        textBef = data[start-200:start]
                        textBefore += textBef

                else:

                    for email in emails:
                        details = re.search(email, data)
                        hit.append(email)

                        end = details.end()
                        textAft = data[end:end+200]
                        textAfter += textAft

                        start = details.start()
                        textBef = data[start-200:start]
                        textBefore += textBef


                alltext = textBefore + textAfter
                soup = BeautifulSoup(alltext, 'lxml')
                gettext = soup.get_text()
                alltextfinal = re.sub("\"|\'|>|\r|\xa0","",gettext)

            except:

                pass


            writer.writerow({'name': item[0],'url':item[1], 'emails':[email[7:] for email in emails], 'phone-numbers':[phone for phone in phones], 'intitle:Contact (ELL ESL) site:.us "public school" ', 'http status':r.status_code})
            writer2.writerow({'url':item[1], 'hit':hit, 'text': alltextfinal})
