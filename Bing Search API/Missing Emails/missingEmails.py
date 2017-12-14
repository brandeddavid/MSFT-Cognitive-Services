import csv
import http.client, urllib.parse, json, csv

subscriptionKey = "224bb0ef6cd348fe9a5e68be95525d22"

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

schools = []

with open('missing.csv', 'r') as f:

    reader = csv.reader(f, delimiter=',')

    for item in reader:

        schools.append('"'+item[0]+'"')

searchTerms = ['"Special education"', 'ESL', 'remedial']
intitle = ['contact', 'staff', 'faculty']



for term in searchTerms:

    for intit in intitle:

        for school in schools:

            searchPhrase = school + ' ' + term + ' ' + 'intitle:' + intit

            savefile = term.strip('""').replace(" ","")+intit

            with open(savefile + '.csv', 'a', newline = '') as l:

                fieldnames = ['School', 'NAME', 'URL', 'TERM']

                writer = csv.DictWriter(l, fieldnames=fieldnames)

                #writer.writeheader()

                if len(subscriptionKey) == 32:

                    try:

                        print('Searching the Web for: ', searchPhrase)

                        headers, result = BingWebSearch(searchPhrase)

                        jsonResponse = json.loads(json.dumps(json.loads(result), indent=4))

                        for item in jsonResponse['webPages']['value']:

                            if jsonResponse['webPages']['value'].index(item) < 1:

                                writer.writerow({'School':school.strip('""'), 'NAME':item['name'], 'URL':item['url'], 'TERM':searchPhrase})

                    except:

                        pass


                else:

                    print("Invalid Bing Search API subscription key!")
                    print("Please paste yours into the source code.")
