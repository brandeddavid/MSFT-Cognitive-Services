import requests, re, csv
from urllib import request
from bs4 import BeautifulSoup

urlList = []

with open('urlList1.csv', 'r') as l:

    urlDoc = csv.reader(l, delimiter = ',')

    for item in urlDoc:

        urlList.append(item[1])



with open('test.csv', 'a', newline='') as f:


    fieldnames = ['url', 'text']

    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    
    for url in urlList:

        try:

            r = requests.get(url)

            emails = [email[7:] for email in re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)]


            #phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

            if len(re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)) == 0:

                phones = re.findall(r'[\d]{3}.?[\d]{3}.[\d]{4}', r.text)

            else:

                phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

        except:

            pass

        try:

            data = request.urlopen(url).read().decode('utf-8')
            #re.search(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

            textAfter = ''
            textBefore = ''

            if len(emails) == 0:

                #for phone in phones:

                details = re.search(phones[0], data)

                end = details.end()
                textAft = data[end:end+800]
                textAfter += textAft

                start = details.start()
                textBef = data[start-300:start]
                textBefore += textBef

            else:

                #for email in emails:

                details = re.search(emails[0], data)

                end = details.end()
                textAft = data[end:end+800]
                textAfter += textAft

                start = details.start()
                textBef = data[start-300:start]
                textBefore += textBef

            alltext = textBefore + textAfter
            soup = BeautifulSoup(alltext, 'lxml')
            gettext = soup.get_text()
            alltextfinal = re.sub("\"|\'|>|\r|\xa0","",gettext)

            writer.writerow({'url':url, 'text': alltextfinal})



        except:

            pass
