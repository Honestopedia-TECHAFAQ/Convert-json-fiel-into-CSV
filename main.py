import json
import csv
from collections import abc

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            flattened_data = [flatten_json(item) for item in data]
            keys = set()
            for item in flattened_data:
                keys.update(item.keys())
            keys = list(keys)
            
            with open(csv_file, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(flattened_data)
        else:
            print("JSON file does not contain a list of objects.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
json_to_csv('input.json', 'output.csv')
