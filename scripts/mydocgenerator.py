#!/usr/bin/env python

import json
import logging
import sys
import xapian
import myrecommendeddocs

finalquery=[]
queryupperbound=" "
querylowerbound=" "
def docrecommender(dbpath, topicmappingfile, minweight, queryfilepath):
    ### to be passed to mydocrecommender function
    # dbpath 
    # topicmappingfile
    # minweight 
    ### to be used here  
    # queryfilepath generated queries
    _file = open(queryfilepath)
    json_output = _file.read()
    finaloutput={}
    parsed_json_dict = json.loads(json_output)
    for item in  parsed_json_dict["finalquery"]:
        docs = myrecommendeddocs.recommended(dbpath,topicmappingfile,minweight,item["query"])
        json_docs = json.loads(docs)
        print item["query"]
        for qresult in json_docs["queryresult"]:
            print qresult["docId"] + " " + qresult["trueweight"] +  " " + str(item["weight"]) + " " + str(float(item["weight"])*float(qresult["trueweight"] ))         
    #print item["weight"]
     





if len(sys.argv) < 5:
    print "Usage: %s TOPICDBINDEX TOPICINDOCSFILE MINWEIGHT GENERATEDQUERYPATH" % sys.argv[0]
    sys.exit(1)

logging.basicConfig(level=logging.INFO)
docrecommender(dbpath = sys.argv[1], topicmappingfile = sys.argv[2], minweight = sys.argv[3], queryfilepath = sys.argv[4])

