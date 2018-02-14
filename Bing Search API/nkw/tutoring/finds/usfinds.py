import requests, re, csv, os, sys, ast
from urllib import request
from bs4 import BeautifulSoup
from string import ascii_uppercase

with open('us.csv', 'r') as l:

    reader = csv.reader(l, delimiter=',')

    with open('usFinds.csv', 'a', newline='') as f:

        header = ['name', 'url', 'text']

        writer2 = csv.DictWriter(f, fieldnames=header)

        writer2.writeheader()

        for item in reader:

            print('Scraping Row ', reader.line_num)

            try:

                data = request.urlopen(item[1]).read().decode('utf-8')
                #re.search(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

                textAfter = ''
                textBefore = ''

                item[3] = ast.literal_eval(item[3])

                for email in item[3]:
                    details = re.search(email, data)

                    start = details.start()

                    #end = details.end()
                    textAft = data[start:start+200]
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

            finally:

                writer2.writerow({'name':item[0], 'url':item[1], 'text': alltextfinal})
