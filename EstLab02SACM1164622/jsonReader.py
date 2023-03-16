import json

def readJsonFile():
    data = [] 
    with open(r'C:\Users\CASTA\source\repos\EstLab02SACM1164622R\EstLab02SACM1164622\input_lab_2_example.jsonl') as jsonFile:
        for line in jsonFile:
            data.append(json.loads(line))
    return data
