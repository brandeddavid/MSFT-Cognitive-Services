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



    with open('redo.csv', 'a') as l:

        fieldnames = ['Wave1','Corrections','es','ru','de']

        writer = csv.DictWriter(l, fieldnames=fieldnames)

        writer.writeheader()

        with open('neural.csv','r') as f:

            reader = csv.reader(f, delimiter=',')

            for item in reader:

                headers = {"Authorization ": finalToken}

                toTranslate = item[1]

                #Translate to Spanish
                translateSPUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'es')
                translationSPData = requests.get(translateSPUrl, headers = headers)
                translationSP = ElementTree.fromstring(translationSPData.text.encode('utf-8'))
                spa = translationSP.text

                #Translate to Russian
                translateRUUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'ru')
                translationRUData = requests.get(translateRUUrl, headers = headers)
                translationRU = ElementTree.fromstring(translationRUData.text.encode('utf-8'))
                rus = translationRU.text

                #Translate to German
                translateDEUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'de')
                translationDEData = requests.get(translateDEUrl, headers = headers)
                translationDE = ElementTree.fromstring(translationDEData.text.encode('utf-8'))
                ger = translationDE.text

                #Translate to Portugese
                """
                translatePTUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'pt')
                translationPTData = requests.get(translatePTUrl, headers = headers)
                translationPT = ElementTree.fromstring(translationPTData.text.encode('utf-8'))
                por = translationPT.text
                """



                writer.writerow({'Wave1': item[0],'Corrections':item[1], 'es':spa, 'ru':rus, 'de':ger})



if __name__ == "__main__":

    client_secret = 'cdf0f2f770e44f7697e1898c54cfaead'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)
