import json

def readJsonFile():
    data = [] 
    with open(r'C:\Users\CASTA\source\repos\EstLab02SACM1164622R\EstLab02SACM1164622\input_challenge_lab_2.jsonl') as jsonFile:
        for line in jsonFile:
            data.append(json.loads(line))
    return data
