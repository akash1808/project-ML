import csv
import json

csvfile = open('../Datasets/WikiRef_dataset_Analyzed/output_csv/releventTopicsInDocs.csv', 'r')
jsonfile = open('../json_files/relevent_WikiRef_dataset_Analyzed_Topics_Docs.json', 'w')

fieldnames = ("docId","topicid","contrib")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',')
    jsonfile.write('\n')
