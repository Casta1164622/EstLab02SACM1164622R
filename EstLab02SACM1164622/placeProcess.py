def hasAllItems(allItemsOfThis,inThis):
    for i in range(len(allItemsOfThis)):
        if((allItemsOfThis[i] in inThis)==False):
            return False
    return True
 
def filterMatchTypeBuilder(input1, typeBuilder):
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

def getDangerList(danger):
    outputList = []
    match danger:
        case "Red":
            outputList = ["Red"]
        case "Orange":
            outputList = ["Red","Orange"]
        case "Yellow":
            outputList = ["Red","Orange","Yellow"]
        case "Green":
            outputList = ["Red","Orange","Yellow","Green"]
    return outputList

def filterMinDanger(CurrentList,danger):
    matching = []
    dangerList = []
    dangerList = getDangerList(danger)
    for i in range(len(CurrentList)):
        if any(elem in CurrentList[i]['zoneDangerous'] for elem in dangerList):
            matching.append(CurrentList[i])
    return matching

def filterPetFriendly(CurrentList,wannaPetFriendly):
    matching = []
    for i in range(len(CurrentList)):
        if(CurrentList[i]['isPetFriendly'] == wannaPetFriendly):
            matching.append(CurrentList[i])
    return matching


def filterMatchPlaces(input1,input2):
    MatchTypeBuilderList = []
    MatchTypeBuilderList = filterMatchTypeBuilder(input1,input2['typeBuilder'])
    if(input2['typeBuilder']=="Houses"):
        SecondFilterList = filterMinDanger(MatchTypeBuilderList,input2['minDanger'])
    if(input2['typeBuilder']=="Apartments"):
        SecondFilterList = filterPetFriendly(MatchTypeBuilderList,input2['wannaPetFriendly'])
        print(MatchTypeBuilderList)

    print(MatchTypeBuilderList)




