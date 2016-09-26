#!/usr/bin/env python

import json
import logging
import sys
import xapian


def freqcounter(dbpath, minfreq, maxfreq,stopwordsfile):
    # minfreq - minimum frequency of words
    # maxfreq - maximum frequency of words

    # Open the database we're going to search.
    db = xapian.Database(dbpath)
    add=1
    finaloutput={}
    freqcounter=[]
    stopwords = getstopwords(stopwordsfile)
    for item in  db.get_document(1):
         if (item.term in stopwords or (item.term[1:]) in stopwords):
             add=0
         else:
             add=1
         val={"term":item.term,"frequency":db.get_collection_freq(item.term)}
         if db.get_collection_freq(item.term) > int(minfreq) and db.get_collection_freq(item.term) < int(maxfreq) and add==1:
             freqcounter.append(val)
    freqcounter=sorted(freqcounter, key=lambda k: k.get('frequency', 0), reverse=True)
    #print freqcounter
    finaloutput["freqcounter"]=freqcounter
    print json.dumps(finaloutput)

def getstopwords(stopwordsfilepath):
    d = []
    with open(stopwordsfilepath) as f:
        for line in f:
           d.append(line.rstrip())
    return d

if len(sys.argv) < 4:
    print "Usage: %s DBPATH MINFREQ MAXFREQ STOPWORDSFILE" % sys.argv[0]
    sys.exit(1)

logging.basicConfig(level=logging.INFO)
freqcounter(dbpath = sys.argv[1], minfreq = sys.argv[2], maxfreq = sys.argv[3], stopwordsfile = sys.argv[4])
