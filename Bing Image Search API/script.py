# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, urllib.request, random, string

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = "0643c39bbd3240e6a880f6cf7367b3ee"

# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
# search APIs.  In the future, regional endpoints may be available.  If you
# encounter unexpected authorization errors, double-check this value against
# the endpoint for your Bing search instance in your Azure dashboard.
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/images/search"

toSearch = ['puppies','angry']

def BingImageSearch(search):
    "Performs a Bing image search and returns the results."

    imageFilters = '&size=medium&imageType=clipart'

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query + imageFilters, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")

if len(subscriptionKey) == 32:


    for term in toSearch:
        
        print('Searching images for: ', term)



        headers, result = BingImageSearch(term)

        jsonResponse = json.loads(json.dumps(json.loads(result), indent=4))

        for item in jsonResponse['value']:
            

            if jsonResponse['value'].index(item) < 3:
                

                urllib.request.urlretrieve(item['contentUrl'], term + str((jsonResponse['value'].index(item)+1)) + ".jpg")



else:

    print("Invalid Bing Search API subscription key!")
    print("Please paste yours into the source code.")
