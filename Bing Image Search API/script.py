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

toSearch = ['seventeen','seventh','seventieth','seventeen','seventh','seventieth','seventy','sew','sewer','shack','shackle','Shad','shade','shades','shady','shaft','shag','shake','shakes','sham','Shane','shank','shape','shapeless','shapes','sharp','sharpen','shave','shaves','shawl','she','shed','sheep','sheets','shelf','shell','shells','shelve','shepherd','sherbet','Sherry','shield','shift','shin','shines','shins','shiny','ship','shipmates','shipment','ships','shirt','shocked','shoe','shook','shop','shore','short','shortcut','shortstop','shot','shots','should','shoulder','shouted','shouting','show','showering','showing','shows','shrank','shriek','shrimp','shrubs','shrunk','shuns','shut','shuts','shy','sib','sibling','sick','sickish','sickle']
"""
Sid
side
sidestroke
sideswipe
sift
sifted
sighs
sign
silent
silk
silks
sill
silly
silo
silt
simple
simply
since
sing
singed
singular
sink
sinks
sinus
sip
sirloin
Sis
sissy
sit
site
sits
six
sixteen
sixtieth
sixty
size
skate
skates
skeptic
sketch
skid
skill
skillfully
skills
skim
skin
skinny
skip
skirt
skit
skull
skunk
sky
skyline
slab
slack
slacks
Slade
slain
slam
slams
slan
slant
slap
slashing
slaughter
slave
slaves
sled
sleek
sleep
sleepy
sleet
sleigh
sleighs
slen
slept
sleuth
slid
slide
slides
slight
slim
sling
slink
slip
slit
slob
slop
slope
slot
slouch
slow
slum
slung
slurp
slush
sly
small
smart
smartest
smash
smell
smells
smelly
smile
smiles
smirk
Smith
smog
smoke
smooch
smooth
smoothes
smooths
smudges
smug
smut
snack
snag
snail
snails
snake
snakes
snap
snapped
snapshot]
"""

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
