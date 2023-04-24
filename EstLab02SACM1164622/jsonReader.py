import json

def readJsonFile(fileRoot):
    data = [] 
    with open(fileRoot) as jsonFile:
        for line in jsonFile:
            data.append(json.loads(line))
    return data
