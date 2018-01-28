import http.client, urllib.parse, json, csv

subscriptionKey = "763b746a12c74bcca27a50d1a48304a0"

host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

def BingWebSearch(search):
    "Performs a Bing Web search and returns the results."

    addquery = '&count=50&offset=0&mkt=en-US'

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query + addquery, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")

with open('292-301.csv', 'r') as openfile:

    reader = csv.reader(openfile, delimiter=',')

    for row in reader:

        name = row[1] + ' ' + row[2]

        if name == ' ':

            pass

        else:

            searchphrase = 'Optometry Michigan ' + "intitle:" + name + ' contact'
            #searchphrase = row[1] + ' ' + row[2] + ' ' + row[0] + ' intitle:contact'
            #print(searchphrase)

            #searchphrase = 'Alan Smith Lifetime Eyecare intitle:contact'

            with open('searchresults.csv', 'a', newline = '') as l:

                fieldnames = ['NAME', 'URL']

                writer = csv.DictWriter(l, fieldnames=fieldnames)
                #writer.writeheader()

                if len(subscriptionKey) == 32:

                    try:

                        urls = []

                        print('Searching the Web for: ', searchphrase)

                        headers, result = BingWebSearch(searchphrase)

                        jsonResponse = json.loads(json.dumps(json.loads(result), indent=4))

                        for item in jsonResponse['webPages']['value']:

                            if jsonResponse['webPages']['value'].index(item) < 10:

                                urls.append(item['url'])

                        writer.writerow({'NAME':name, 'URL':urls})

                    except:

                        pass

                    finally:

                        urls = []


                else:

                    print("Invalid Bing Search API subscription key!")
                    print("Please paste yours into the source code.")
