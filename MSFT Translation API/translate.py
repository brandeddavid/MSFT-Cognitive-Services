"""
Example application showing the use of the Translate method in the Text Translation API.
"""

from xml.etree import ElementTree
from auth import AzureAuthClient
import requests
import csv
import sys


# reload(sys)
#
# sys.setdefaultencoding('utf-8')



def GetTextAndTranslate(finalToken):

    fromLangCode = "en"



    with open('kcihpu.csv', 'a') as l:

        fieldnames = ['Wave1','Corrections','korean', 'cantonese', 'indonesian', 'hebrew', 'persian', 'urdu']

        writer = csv.DictWriter(l, fieldnames=fieldnames)

        writer.writeheader()

        with open('neural.csv','r') as f:

            reader = csv.reader(f, delimiter=',')

            for item in reader:

                headers = {"Authorization ": finalToken}

                toTranslate = item[1]

                #Translate to Korean
                translateKOUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'ko')
                translationKOData = requests.get(translateKOUrl, headers = headers)
                translationKO = ElementTree.fromstring(translationKOData.text.encode('utf-8'))
                kor = translationKO.text

                #Translate to Cantonese
                translateYUEUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'yue')
                translationYUEData = requests.get(translateYUEUrl, headers = headers)
                translationYUE = ElementTree.fromstring(translationYUEData.text.encode('utf-8'))
                can = translationYUE.text

                #Translate to Indonesian
                translateIDUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'id')
                translationIDData = requests.get(translateIDUrl, headers = headers)
                translationID = ElementTree.fromstring(translationIDData.text.encode('utf-8'))
                ind = translationID.text

                #Translate to Hebrew

                translateHEUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'he')
                translationHEData = requests.get(translateHEUrl, headers = headers)
                translationHE = ElementTree.fromstring(translationHEData.text.encode('utf-8'))
                heb = translationHE.text

                #Translate to Persian

                translateFAUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'fa')
                translationFAData = requests.get(translateFAUrl, headers=headers)
                translationFA = ElementTree.fromstring(translationFAData.text.encode('utf-8'))
                per = translationFA.text

                #Translate to Urdu

                translateURUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'ur')
                translationURData = requests.get(translateURUrl, headers=headers)
                translationUR = ElementTree.fromstring(translationURData.text.encode('utf-8'))
                urd = translationUR.text


                writer.writerow({'Wave1': item[0],'Corrections':item[1], 'korean':kor, 'cantonese':can, 'indonesian':ind, 'hebrew':heb, 'persian':per, 'urdu':urd})



if __name__ == "__main__":

    client_secret = 'fdb5a57660ef45128aeb8167b971e708'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)
