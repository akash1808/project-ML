#!/usr/bin/env python

import json
import logging
import sys
import xapian


def recommended(dbpath, topicmappingfile, minweight,querystring, offset=0, pagesize=10):
    # offset - defines starting point within result set
    # pagesize - defines number of records to retrieve
    # minweight - defines minweight of document in search
    # Open the database we're going to search.
    db = xapian.Database(dbpath)
    
    # Set up a QueryParser with a stemmer and suitable prefixes
    queryparser = xapian.QueryParser()
    queryparser.set_stemmer(xapian.Stem("en"))
    queryparser.set_stemming_strategy(queryparser.STEM_SOME)
    
    #set queryparser prefixes
#    queryparser.add_prefix("title", "S")
    queryparser.add_prefix("value", "XD")
#    queryparser.add_prefix("category", "XC")
#    queryparser.add_prefix("topic", "XT")
#    queryparser.add_prefix("note", "XN")

    # And parse the query
    query = queryparser.parse_query(querystring)

    # Use an Enquire object on the database to run the query
    enquire = xapian.Enquire(db)
    enquire.set_query(query)

    # And print out something about each match
    matches = []
    result = []
    # Start of example code.
    # Set up a spy to inspect the MAKER value at slot 1
    #spy = xapian.ValueCountMatchSpy(1)
    #enquire.add_matchspy(spy)
    finalresult={}
    for match in enquire.get_mset(offset, pagesize, 100):
#        print match
        fields = json.loads(match.document.get_data())
#        print fields
        DocsIds= TopictoDoc(match.docid,topicmappingfile,minweight)
#        print DocsIds
     
#        print u"%(rank)i: #%(docid)3.3i  \nValue: %(value)s  \nWeight: %(weight)s" % {
#            'rank': match.rank + 1,
#            'docid': match.docid,
#            'weight':match.weight,
#            'value': fields.get('words', u''),
#            }
#        matches.append(match.docid)
        
        for fields1 in DocsIds:
            fields1["trueweight"]=str(float(fields1["contrib"])*float(match.weight))
            result.append(fields1)
    result=sorted(result, key=lambda k: k.get('trueweight', 0), reverse=True)
    finalresult["queryresult"]=result
    print json.dumps(finalresult)
    return json.dumps(finalresult)
    # Fetch and display the spy values
    #for facet in spy.values():
    #    print "Facet: %(term)s; count: %(count)i" % {
    #        'term' : facet.term,
    #        'count' : facet.termfreq
    #    }
     
    # Finally, make sure we log the query and displayed results
    #support.log_matches(querystring, offset, pagesize, matches)
### End of example code.



def TopictoDoc(topicId, topicmappingfile,minweight):
    _file = open(topicmappingfile)
    json_output = _file.read()
    mapping=[]
    parsed_json_dict = json.loads(json_output)
#    print topicId
    for fields in parsed_json_dict['rel']:
        #print fields        
        valtopicId = fields["topicid"]
#        print valtopicId
        valrank = fields["contrib"]
        
        if (valtopicId == str(topicId) and float(valrank) > float(minweight)):
#            print fields
             mapping.append(fields);                

    return mapping




