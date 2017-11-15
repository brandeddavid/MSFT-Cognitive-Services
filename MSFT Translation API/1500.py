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



    with open('1500.csv', 'a') as l:

        fieldnames = ['Wave1','Corrections','ru','de','es','fr']

        writer = csv.DictWriter(l, fieldnames=fieldnames)

        writer.writeheader()

        with open('translate.csv','r') as f:

            reader = csv.reader(f, delimiter=',')

            for item in reader:

                headers = {"Authorization ": finalToken}

                toTranslate = item[1].replace('"','')

                #Translate to Russia
                translateRUUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'ru')
                translationRUData = requests.get(translateRUUrl, headers = headers)
                translationRU = ElementTree.fromstring(translationRUData.text.encode('utf-8'))
                item[2] = translationRU.text

                #Translate to Deutsch
                translateDEUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'de')
                translationDEData = requests.get(translateDEUrl, headers = headers)
                translationDE = ElementTree.fromstring(translationDEData.text.encode('utf-8'))
                item[3] = translationDE.text

                #Translate to Spanish
                translateESUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'es')
                translationESData = requests.get(translateESUrl, headers = headers)
                translationES = ElementTree.fromstring(translationESData.text.encode('utf-8'))
                item[4] = translationES.text

                #Translate to French
                translateFRUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'fr')
                translationFRData = requests.get(translateFRUrl, headers = headers)
                translationFR = ElementTree.fromstring(translationFRData.text.encode('utf-8'))
                item[5] = translationFR.text



                writer.writerow({'Wave1': item[0],'Corrections':item[1], 'ru':item[2],'de':item[3],'es':item[4],'fr':item[5]})



if __name__ == "__main__":

    client_secret = 'f7b89ffc171b4a278ce7d17a6d218cf2'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)
