#!/usr/bin/python
import csv
import json

def is_acm(i):
    try:
        x = int(i)
        return True
    except Exception as e:
        return False

# Id map
id_map = {}
id_map_file = "map.json"
for [terminus_id, original_id] in json.load(open(id_map_file,'r')):
    id_map[f"iri:///dblp-acm/i/{terminus_id}"] = original_id

# Correct answers
matches = {} # Match with ACM as key
matches_file = "DBLP-ACM_match.csv"
with open(matches_file, 'r') as f:
    r = csv.reader(f)
    for (dblp,acm) in r:
        matches[acm] = dblp

duplicates_map = {}
duplicates_file = "duplicates.json"
duplicates = json.load(open(duplicates_file,'r'))
for [id1,id2] in duplicates:
    original1 = id_map[id1]
    original2 = id_map[id2]
    if is_acm(original1) and not is_acm(original2):
        duplicates_map[original1] = original2
    elif is_acm(original2) and not is_acm(original1):
        duplicates_map[original2] = original1

# Calculate precision
total = len(matches)
total_retrieved = len(duplicates_map)
relevant = 0
for acm_key in duplicates_map:
    if duplicates_map[acm_key] == matches[acm_key]:
        relevant+=1
precision = relevant / total_retrieved
print(f"relevant: {relevant}")
print(f"total retrieved: {total_retrieved}")
print(f"total relevant: {total}")
print(f"Precision: {precision}")

# Calculate recall
recall = relevant / total
print(f"Recall: {recall}")
