def assignPlaceValues(input):
    keyList = dict()
    placeNumber = 0;
    for i in input:
        for key in i:
            if(i.get(key) and key not in keyList):
                keyList[key] = placeNumber
                placeNumber+=1
    return keyList

def assignLocationValues(input, keylist):
    locationValues = []
    for i in input:
        valuesInCurrentLocation = []
        for key in i:
            if(i.get(key)):
                valuesInCurrentLocation.append(keylist.get(key))
        locationValues.append(valuesInCurrentLocation)
    return locationValues

def assignSearchValues(input, keyList):
    searchValues = []
    for i in input:
        searchValues.append(keyList.get(i))
    return searchValues