import jsonReader as jreader
import assignPlaceValues as apv
import getBestLocation as gbl

keyList =[]
locationValues = []
PlaceMatrix = []
data = jreader.readJsonFile()
for i in range(len(data)):

    keyList = apv.assignPlaceValues(data[i]['input1'])
    locationValues = apv.assignLocationValues(data[i]['input1'],keyList)
    searchValues = apv.assignSearchValues(data[i]['input2'],keyList)
    if(None in searchValues):
        print('[]')
    else:
        placeMatrix = gbl.getMatrix(locationValues, searchValues)
        gbl.getDistanceMatrix(placeMatrix, searchValues)
