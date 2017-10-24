"""
Example application showing the use of the Translate method in the Text Translation API.
"""

from xml.etree import ElementTree
from auth import AzureAuthClient
import requests
import csv



def GetTextAndTranslate(finalToken):

    fromLangCode = "en"
    toLangCode = ""
    textToTranslate = " "


    with open('test.csv', 'r') as f:

        r = csv.reader(f, delimiter=',')

        for row in r:

            textToTranslate = row[0]
            toLangCode = "ru"
            # Call to Microsoft Translator Service
            headers = {"Authorization ": finalToken}
            translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)

            translationData = requests.get(translateUrl, headers = headers)

            # parse xml return values
            translation = ElementTree.fromstring(translationData.text.encode('utf-8'))

            row [2] = translation.text

            print row[2]

        for row in r:

            textToTranslate = row[0]
            toLangCode = "sp"
            # Call to Microsoft Translator Service
            headers = {"Authorization ": finalToken}
            translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)

            translationData = requests.get(translateUrl, headers = headers)

            # parse xml return values
            translation = ElementTree.fromstring(translationData.text.encode('utf-8'))

            row [3] = translation.text

            print row[3]

        for row in r:

            textToTranslate = row[0]
            toLangCode = "du"
            # Call to Microsoft Translator Service
            headers = {"Authorization ": finalToken}
            translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)

            translationData = requests.get(translateUrl, headers = headers)

            # parse xml return values
            translation = ElementTree.fromstring(translationData.text.encode('utf-8'))

            row [4] = translation.text

            print row[4]



"""
    # Call to Microsoft Translator Service
    headers = {"Authorization ": finalToken}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)

    translationData = requests.get(translateUrl, headers = headers)
    # parse xml return values
    translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
    # display translation
    print "The translation is---> ", translation.text

    print " "

"""
if __name__ == "__main__":

    client_secret = 'b084fcc6af46498492cc6b707f4f53cb'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)
