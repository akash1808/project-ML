#!/usr/bin/env python

import json
import sys
import xapian
import csv

# start of the indexing code
def myindexer(datapath, dbpath):
    
    # Create or open the database we're going to be writing to.
    db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)
    
    # Set up a TermGenerator that we'll use in indexing.
    termgenerator = xapian.TermGenerator()
    termgenerator.set_stemmer(xapian.Stem("en"))
    
    
    #parse the json input documents
    _file = open(datapath)
    json_output = _file.read()
    #jsonoutput = '{"name":"anshul", "age":"30", "gender":"male"}'
    print json_output
    parsed_json_dict = json.loads(json_output)
    
    #print(parsed_json_dict['doc'][0]['title'])
    #print len(parsed_json_dict['doc'])      

   # for fields in parse_csv_file('Topics_Words.csv'):            
    for fields in parsed_json_dict['doc']:
            # 'fields' is a dictionary mapping from field name to value.
            # Pick out the fields we're going to index.
            identifier = fields['topicId']
            value = fields['words']
           # domain = fields['domain']
           # category = fields['category']
           # topic = fields['topic']
           # highlight = fields['highlight']
           # note = fields['note']
           # readingDate = fields['readingDate']
           # publishingDate = fields['publishingDate']
           # 
            print(identifier)
            print(value)
            #print(domain)
            #print(category)
            #print(topic)
            #description = fields.get('DESCRIPTION', u'')
            #title = fields.get('TITLE', u'')
            

            # We make a document and tell the term generator to use this.
            doc = xapian.Document()
            termgenerator.set_document(doc)

            # Index each field with a suitable prefix.
            #termgenerator.index_text(title, 1, 'S') #think about weights later
            termgenerator.index_text(value, 1, 'XD')
            #termgenerator.index_text(category, 1, 'XC')
            #termgenerator.index_text(topic, 1, 'XT')
            #termgenerator.index_text(note, 1, 'XN')

            # Index fields without prefixes for general search.
            termgenerator.index_text(value,2)
            termgenerator.increase_termpos()
           # termgenerator.index_text(category,2)
           # termgenerator.increase_termpos()
           # termgenerator.index_text(topic,10)
           # termgenerator.increase_termpos()          
           # termgenerator.index_text(title,10)
           # termgenerator.increase_termpos()
           # termgenerator.index_text(highlight,5)
           # termgenerator.increase_termpos()
           # termgenerator.index_text(note,5)

            # Store all the fields for display purposes.
            doc.set_data(json.dumps(fields, encoding='utf8'))

            # We use the identifier to ensure each object ends up in the
            # database only once no matter how many times we run the
            # indexer.
            idterm = u"Q" + str(identifier)
            doc.add_boolean_term(idterm)
            db.replace_document(idterm, doc)         
    ### End of example code.

if len(sys.argv) != 3:
    print "Usage: %s DATAPATH DBPATH" % sys.argv[0]
    sys.exit(1)

myindexer(datapath = sys.argv[1], dbpath = sys.argv[2])
    
    


    
    
