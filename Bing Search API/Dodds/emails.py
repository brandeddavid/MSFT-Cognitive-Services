import requests, re, csv, os, sys, ast
from urllib import request
from bs4 import BeautifulSoup

#urlList = []
#generic = ['admin', 'frontdesk', 'hiring', 'enroll', 'careers', 'career', 'info', 'online', 'help', 'desk', 'career', 'job', 'inquire', 'contact', 'post', 'master', 'general', 'admission', 'admissions', 'advise', 'advice', 'service', 'budget', 'department', 'board', 'noreply', 'webmaster', 'nr']

with open('292-301_searchresults.csv', 'r') as k:

    reader = csv.reader(k, delimiter = ',')

    for row in reader:

        print('Row number: ', reader.line_num)
        urlList = ast.literal_eval(row[1])
        final = []

        with open('292-301_emails.csv', 'a', newline = '') as l:

            fieldnames = ['name', 'emails']

            writer = csv.DictWriter(l, fieldnames=fieldnames)

            #writer.writeheader()


            for url in urlList:

                print ('Url '+ str(urlList.index(url)+1) + ' of ' + str(len(urlList)))

                try:

                    r = requests.get(url)

                    emails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', r.text)

                    finalemails = []

                    for email in set(emails):

                        finalemails.append(email)

                    for entry in finalemails:

                        final.append(entry)

                except:

                    pass

                finally:

                    emails = []

            writer.writerow({'name':row[0], 'emails':[email for email in final]})
