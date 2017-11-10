# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, urllib.request, random, string
import csv

subscriptionKey = "0643c39bbd3240e6a880f6cf7367b3ee"


host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/images/search"


    


def BingImageSearch(search):
    "Performs a Bing image search and returns the results."

    imageFilters = '&safeSearch=strict&size=medium&imageType=clipart&license=public'

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query + imageFilters, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")


with open('keywords.csv', 'r') as f:

    toSearch = []

    words = csv.reader(f, delimiter = ',')

    for word in words:

        toSearch.append(word[0])

    if len(subscriptionKey) == 32:


        for term in toSearch:
            
            print('Searching images for: ', term)


            try:

                headers, result = BingImageSearch(term)

                jsonResponse = json.loads(json.dumps(json.loads(result), indent=4))

                for item in jsonResponse['value']:
                    

                    if jsonResponse['value'].index(item) < 3:
                        

                        urllib.request.urlretrieve(item['contentUrl'], term + str((jsonResponse['value'].index(item)+1)))

            except:

                pass



    else:

        print("Invalid Bing Search API subscription key!")
        print("Please paste yours into the source code.")
