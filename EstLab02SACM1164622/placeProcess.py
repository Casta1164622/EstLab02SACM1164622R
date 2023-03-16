def predicate_function(function,data1,data2):
    return funtion(data1,data2)
def Matchdata(data1, data2):
    return data1 == data2

def hasAllItems(allItemsOfThis,inThis):
    for i in range(len(allItemsOfThis)):
        if((allItemsOfThis[i] in inThis)==False):
            return False
    return True
 
def getMatchTypeBuilder(input1, typeBuilder):
    matching = []
    matchingFinal = []
    for i in range(len(input1)):
        for j in input1[i]['builds'].keys():
            if(j == typeBuilder):
                matching.append(input1[i]['builds'][j])

    for i in matching:
        for j in i:
            matchingFinal.append(j)
    return matchingFinal

def getMatchPlaces(input1,input2):
    MatchTypeBuilderList = []
    MatchTypeBuilderList = getMatchTypeBuilder(input1,input2['typeBuilder'])
    print(MatchTypeBuilderList)




