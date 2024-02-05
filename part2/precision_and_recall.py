#!/usr/bin/python
import sys
import json
import subprocess
import re
from terminusdb_client import Client

f = sys.argv[1]
duplicates = json.load(open(f,))
id_pairs = []
client = Client("http://127.0.0.1:6363/")
for [id1, id2] in duplicates:
    client.connect(db="resolution")
    dict1 = client.get_document(id1)
    dict2 = client.get_document(id2)
    if dict1["id"][0].isdigit():
        id_pairs.append((dict2["id"],dict1["id"]))
    else:
        id_pairs.append((dict1["id"],dict2["id"]))

id_pairs.sort()
print('"idDBLP","idACM"')
for (id1,id2) in id_pairs:
    print(f"\"{id1}\",{id2}")
