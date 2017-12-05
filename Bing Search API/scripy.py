# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, csv

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = "224bb0ef6cd348fe9a5e68be95525d22"

# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
# search APIs.  In the future, regional endpoints may be available.  If you
# encounter unexpected authorization errors, double-check this value against
# the endpoint for your Bing Web search instance in your Azure dashboard.
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

term = 'intitle:Contact (ELL ESL) site:.us "public school" '

def BingWebSearch(search):
    "Performs a Bing Web search and returns the results."

    addquery = '&count=1000&offset=1000'

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query + addquery, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")


with open('urlList.csv', 'a', newline = '') as l:

    fieldnames = ['NAME', 'URL']

    writer = csv.DictWriter(l, fieldnames=fieldnames)

    writer.writeheader()

    if len(subscriptionKey) == 32:

        try:

            print('Searching the Web for: ', term)

            headers, result = BingWebSearch(term)

            jsonResponse = json.loads(json.dumps(json.loads(result), indent=4))

            #print (type(jsonResponse["webPages"]['value']))


            for item in jsonResponse['webPages']['value']:

                if jsonResponse['webPages']['value'].index(item) < 100:

                    writer.writerow({'NAME':item['name'], 'URL':item['url']})




            #print (jsonResponse['webPages'])
        except:

            pass


    else:

        print("Invalid Bing Search API subscription key!")
        print("Please paste yours into the source code.")
