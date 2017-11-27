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

        fieldnames = ['Wave1','Corrections','ar','zh-CHS','tr','pt']

        writer = csv.DictWriter(l, fieldnames=fieldnames)

        writer.writeheader()

        with open('translate.csv','r') as f:

            reader = csv.reader(f, delimiter=',')

            for item in reader:

                headers = {"Authorization ": finalToken}

                toTranslate = item[1]

                #Translate to Arabic
                translateARUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'ar')
                translationARData = requests.get(translateARUrl, headers = headers)
                translationAR = ElementTree.fromstring(translationARData.text.encode('utf-8'))
                ara = translationAR.text

                #Translate to Chinese
                translateCHUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'zh-CHS')
                translationCHData = requests.get(translateCHUrl, headers = headers)
                translationCH = ElementTree.fromstring(translationCHData.text.encode('utf-8'))
                chi = translationCH.text

                #Translate to Turkish
                translateTRUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'tr')
                translationTRData = requests.get(translateTRUrl, headers = headers)
                translationTR = ElementTree.fromstring(translationTRData.text.encode('utf-8'))
                tur = translationES.text

                #Translate to Portugese
                translatePTUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}&category=generalnn".format(toTranslate, 'pt')
                translationPTData = requests.get(translatePTUrl, headers = headers)
                translationPT = ElementTree.fromstring(translationPTData.text.encode('utf-8'))
                por = translationPT.text



                writer.writerow({'Wave1': item[0],'Corrections':item[1], 'ar':ara,'zh-CHS':chi,'tr':tur,'pt':por})



if __name__ == "__main__":

    client_secret = 'cdf0f2f770e44f7697e1898c54cfaead'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    GetTextAndTranslate(bearer_token)
