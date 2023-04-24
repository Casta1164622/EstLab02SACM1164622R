import sys
import copy

def getMatrix(locationValues, search2):
    CoincidenceMatrix = []
    OptCoincidenceMatrix = dict()
    for i in locationValues:
        MatrixRow = []
        for j in search2:
            if(j in i):
                MatrixRow.append(1)
            else:
                MatrixRow.append(0)
        CoincidenceMatrix.append(MatrixRow)

    for i in range(len(CoincidenceMatrix)):
        OptCoincidenceMatrix[i] = CoincidenceMatrix[i]
        
    return OptCoincidenceMatrix

def getDistanceMatrix(CoincidenceMatrix, search2):
    DistanceMatrix = copy.deepcopy(CoincidenceMatrix)
    for i in CoincidenceMatrix:
        for j in range(len(search2)):
            shortestDistance = sys.maxsize
            for k in CoincidenceMatrix:
                distance = sys.maxsize
                if(CoincidenceMatrix[k][j] == 1):
                    if(k >= i):
                        distance = k-i
                    else:
                        distance = i-k
                if(distance < shortestDistance):
                    shortestDistance = distance
                DistanceMatrix[i][j] = shortestDistance
    getBestLocations(DistanceMatrix, search2)

def getBestLocations(DistanceMatrix, search2):
    TotalDistance = dict()
    bestLocationsList = dict()
    BestLocations = []
    BestLocationsMin = []
    shortestTotalDistance = sys.maxsize
    for i in DistanceMatrix:
        sum = 0
        for j in range(len(search2)):
            sum+=DistanceMatrix[i][j]
        if(sum < shortestTotalDistance):
            shortestTotalDistance = sum
        TotalDistance[i] = sum

    for i in DistanceMatrix:
        if(TotalDistance[i] == shortestTotalDistance):
            bestLocationsList[i] = shortestTotalDistance

    if(len(bestLocationsList)>0):
        LowestMax = sys.maxsize
        LowestMin = sys.maxsize
        for i in bestLocationsList:
            maxDistance = 0
            maxDistance = max(DistanceMatrix[i])
            if(maxDistance < LowestMax):
                LowestMax = maxDistance
        for i in bestLocationsList:
            if(max(DistanceMatrix[i]) == LowestMax):
                BestLocations.append(i)
        for i in BestLocations:
            minDistance = 0
            minDistance = min(DistanceMatrix[i])
            if(minDistance < LowestMin):
                LowestMin = minDistance
        for i in BestLocations:
            if(min(DistanceMatrix[i]) == LowestMin):
                BestLocationsMin.append(i)
        if(len(BestLocationsMin) == len(BestLocations)):
            print(BestLocations)
        else:
            print(BestLocationsMin)
 
    else:
        print('[]')

