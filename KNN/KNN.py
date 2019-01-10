import numpy

class KNN(object):

    def __init__(self, neighborCount):
        self.neighborCount = neighborCount

    def fit(self, trainingX, trainingY):
        self.trainingX = trainingX[:][:]
        self.trainingY = trainingY[:]

    def predict(self, newX):
        xDistance = []
        # fill
        for xIndex in range(len(self.trainingY)):
            dist = numpy.linalg.norm(newX - self.trainingX[xIndex][:])
            myPair = [xIndex, dist]
            xDistance.append(myPair)
        print("xDistance =", xDistance)
        xDistance.sort(key=takeSecond)
        print("sorted xDistance =", xDistance)
        indexArray = []
        for rowIndex in range(self.neighborCount):
            indexArray.append(xDistance[rowIndex][0])
        print("indexArray =", indexArray)
        ySubset = []
        for subsettedIndex in indexArray:
            ySubset.append(self.trainingY[int(subsettedIndex)])
        print("ySubset =", ySubset)
        print("indexArray =", indexArray)
        # fill
        predictedY = max(ySubset, key=ySubset.count)
        return (predictedY)

def takeSecond(elem):
    return elem[1]