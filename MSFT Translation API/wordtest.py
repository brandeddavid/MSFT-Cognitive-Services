#from nltk.corpus import wordnet
#import nltk
#from PyDictionary import PyDictionary
import json
import csv

import sys


reload(sys)

sys.setdefaultencoding('utf-8')

data = json.load(open("dictionary.json"))



"""

with open('test.csv','r') as f:

            reader = csv.reader(f, delimiter=',')

            for item in reader:

                
                sentence = item[0]

                lis = sentence.split(' ')

                with open('out.csv', 'a') as l:

                    fieldnames = ['Title','ID','ru','sp','du']

                    writer = csv.DictWriter(l, fieldnames=fieldnames)

                    writer.writeheader()

                    string = ''

                    for word in lis:

                        if word in data.keys():

                            string += word

                        else:

                            string += '[' + word + ']'

                    print string




sentence = 'a (long a), which is also called a faded schwa'

out = ''

test = sentence.split(' ')

for word in test:

    if word.lower() in data.keys().lower():

        out += word

print out

            

eng_vocab = set(w.lower() for w in nltk.corpus.words.words())

for word in lis:

    if word in eng_vocab:

        print word + ' is an English'

    else:

        print word + ' is not an English word' 


"""
