import requests, re, csv, os, sys
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.carrollschool.org/admissions/request-information'

generic = ['enroll', 'careers', 'career', 'info', 'online', 'help', 'desk', 'career', 'job', 'inquire', 'contact', 'post', 'master', 'general', 'admission', 'admissions', 'advise', 'advice', 'service', 'budget', 'department', 'board', 'noreply', 'webmaster', 'nr']

try:

    r = requests.get(url)

    #emails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', r.text)
    emails = re.findall(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', r.text)

    finalemails = []

    for email in set(emails):

        finalemails.append(email)

    for email in finalemails:

        if len(email) < 8:

            finalemails.remove(email)

        elif email[0:email.index('@')] in generic:

            finalemails.remove(email)

        else:

            pass

except:

    pass

finally:

    print (finalemails, len(finalemails))
