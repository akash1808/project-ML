#!/usr/bin/env python

import json
import logging
import sys
import xapian

finalquery=[]
queryupperbound=" "
querylowerbound=" "
def freqcounter(datapath, minfreq, maxfreq):
    # minfreq - minimum frequency of words
    # maxfreq - maximum frequency of words
    # datapath - frequency file to be used for query creation 
    uppercounter = 0;
    lowercounter = 0;
    _file = open(datapath)
    json_output = _file.read()
    finaloutput={}
    parsed_json_dict = json.loads(json_output)
    avgfreq = (int(minfreq) + int(maxfreq))/2
    global queryupperbound,querylowerbound,extraquery
    for item in  parsed_json_dict["freqcounter"]:
         if (item["frequency"] > avgfreq):
             if (uppercounter < 6):
                 queryupperbound=queryupperbound + " " + item["term"]
                 uppercounter = uppercounter +1 ;
             else:
                 uppercounter = 0
                 value={"type":"upper","query":queryupperbound}
                 finalquery.append(value)
                 queryupperbound=item["term"]                 
         elif (item["frequency"] <= avgfreq):
             if (lowercounter < 6):
                 querylowerbound=querylowerbound + " " + item["term"]
                 lowercounter = lowercounter + 1
             else:
                 lowercounter = 0;
                 value={"type":"lower","query":querylowerbound}
                 finalquery.append(value)
                 querylowerbound=item["term"]
    value={"type":"upperextra","query":queryupperbound}
    finalquery.append(value)
    value={"type":"lowerextra","query":querylowerbound}
    finalquery.append(value)
    len=0
    for item in finalquery:
         len=len+count_letters(item["query"])
    for item in finalquery:
         lenact=count_letters(item["query"])
         weight=float(float(lenact)/float(len));
         item["weight"]=weight
    finaloutput["finalquery"]=finalquery
    print json.dumps(finaloutput)
         #print item["frequency"]
         #print item["term"]

def count_letters(word):
    return len(word) - word.count(' ')

if len(sys.argv) < 4:
    print "Usage: %s FREQUENCYFILEPATH MINFREQ MAXFREQ" % sys.argv[0]
    sys.exit(1)

logging.basicConfig(level=logging.INFO)
freqcounter(datapath = sys.argv[1], minfreq = sys.argv[2], maxfreq = sys.argv[3])

