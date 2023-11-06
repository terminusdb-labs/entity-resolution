import csv
import json

with open("all_records.json", 'w') as output:
    with open("ACM.csv", 'r') as acm:
        dictreader = csv.DictReader(acm)
        for d in dictreader:
            d['source'] = "ACM.csv"
            output.write(json.dumps(d))
            output.write("\n")
    with open("DBLP2.csv", 'r') as dblp:
        dictreader = csv.DictReader(dblp)
        for d in dictreader:
            d['source'] = "DBLP2.csv"
            output.write(json.dumps(d))
            output.write("\n")
