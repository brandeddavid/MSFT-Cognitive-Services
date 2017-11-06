"""
Example application showing the use of the Translate method in the Text Translation API.
"""

from xml.etree import ElementTree
from auth import AzureAuthClient
import requests
import csv
import sys


reload(sys)

sys.setdefaultencoding('utf-8')



def GetTextAndTranslate(finalToken):

    fromLangCode = "en"



    with open('out.csv', 'a') as l:

        fieldnames = ['Title','ID','ru','sp','du']

        writer = csv.DictWriter(l, fieldnames=fieldnames)

        writer.writeheader()

        with open('test.csv','r') as f:

            reader = csv.reader(f, delimiter=',')

            for item in reader:

                headers = {"Authorization ": finalToken}

                toTranslate = item[0].replace('"','')

                #Translate to Russia
                translateRUUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'ru')
                translationRUData = requests.get(translateRUUrl, headers = headers)
                translationRU = ElementTree.fromstring(translationRUData.text.encode('utf-8'))
                item[2] = translationRU.text.replace('"','')

                #Translate to Spanish
                translateESUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(toTranslate, 'es')
                translationESData = requests.get(translateESUrl, headers = headers)
                translationES = ElementTree.fromstring(translationESData.text.encode('utf-8'))
                item[3] = translationES.text.replace('"','')

                #Translate to Deutsch
                translateDEUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(toTranslate, 'de')
                translationDEData = requests.get(translateDEUrl, headers = headers)
                translationDE = ElementTree.fromstring(translationDEData.text.encode('utf-8'))
                item[4] = translationDE.text.replace('"','')

                writer.writerow({'Title': item[0],'ID':item[1], 'ru':item[2],'sp':item[3],'du':item[4]})



if __name__ == "__main__":

    client_secret = 'f7b89ffc171b4a278ce7d17a6d218cf2'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)
