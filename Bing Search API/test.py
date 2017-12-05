import requests, re, csv
from urllib import request
from bs4 import BeautifulSoup

try:

    r = requests.get('http://www.ashwaubenon.k12.wi.us/parkview/contactus_pv.cfm')

    emails = [email[7:] for email in re.findall(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)]


    #phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

    if len(re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)) == 0:

        phones = re.findall(r'[\d]{3}.?[\d]{3}.[\d]{4}', r.text)

    else:

        phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', r.text)

except:

    pass

try:

    data = request.urlopen('http://www.ashwaubenon.k12.wi.us/parkview/contactus_pv.cfm').read().decode('utf-8')
    #re.search(r'mailto\:[0-9a-zA-Z\@\.]{1,}', r.text)

    textAfter = ''
    textBefore = ''

    if len(emails) == 0:

        for phone in phones:

            details = re.search(phone, data)

            end = details.end()
            textAft = data[end:end+100]
            textAfter += textAft

            start = details.start()
            textBef = data[start-100:start]
            textBefore += textBef

    else:

        for email in emails:

            details = re.search(email, data)

            end = details.end()
            textAft = data[end:end+100]
            textAfter += textAft

            start = details.start()
            textBef = data[start-100:start]
            textBefore += textBef
    
    soupbefore = BeautifulSoup(textBefore, 'lxml')
    textbef = soupbefore.get_text()

    for itb in textbef.split('\n'):

        print (itb)

    soupafter = BeautifulSoup(textAfter, 'lxml')
    textaft = soupafter.get_text()

    for ita in textaft.split('\n'):

        print (ita)


    
    

except:

    pass
