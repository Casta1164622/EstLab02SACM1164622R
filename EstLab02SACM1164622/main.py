import jsonReader as jreader
import placeProcess as pp

data = jreader.readJsonFile()
for i in range(len(data)):
    pp.filterMatchPlaces(data[i]['input1'],data[i]['input2'])

