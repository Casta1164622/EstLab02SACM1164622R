import json

def readJsonFile():
    data = [] 
    with open('input/input_challenge.jsonl') as jsonFile:
        for line in jsonFile:
            data.append(json.loads(line))
    return data


