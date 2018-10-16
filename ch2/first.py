import copy

class Perceptron:

    def __init__(self, epochCount):
        print("\n Perceptron gets constructed \n")
        print("\n epochCount = ", epochCount, "\n")
        self.innerEpochCount = epochCount

    def predict (self, pureInput):
        predictedValue = 0 if pureInput < 0 else 1
        '''
        if pureInput < 0:
            predictedValue = 0
        else :
            predictedValue = 1
        '''
        return predictedValue


    def fit (self, xMatrix, yVector):
        print("\n method doAll self.innerEpochCount: ", self.innerEpochCount, "\n")
        # preparing the data structures
        objectCount = len(xMatrix)
        print("objectCount: ", objectCount)
        # prepend the colmn of ones
        xMatrixExtended = copy.deepcopy(xMatrix)
        for rowIndex in range (0, objectCount):
            # prepend 1 to every row, at index 0
            # it should push all the other elements to the right
            xMatrixExtended[rowIndex].insert(0, 1)
        print("xMatrixExtended: ", xMatrixExtended)
        columnCount = len(xMatrixExtended[0])
        print("columnCount: ", columnCount)
        weightVector = []
        for columnIndex in range (1, columnCount):
            weightVector.append(0)
        print("weightVector: ", weightVector)

        deltaWeightVector = []
        for columnIndex in range (1, columnCount):
            deltaWeightVector.append(0)
        # data structures are created.

        # Now let us fit the data
        for epoch in range (0, self.innerEpochCount):
            for objectIndex in range (0, objectCount):
                pass
                # modify this multiplication
                # pureInput = sum(weightVector * xMatrixExtended[objectIndex])
                # yPredicted = self.predict(pureInput)

            # Z
            # y = phi(z)
            # deltaWeight
            # weight




# w vector weight
# deltaW vector deltaWeight
# xMatrix
# yVector
# zScalar
# indicator that epoch does not have changes, the stoppage criterion isStop
# epochCount
# eta, the learningSpeed



print("\n Define the input parameters \n")
myEpochCount = 5
xMatrix = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
yVector = [0, 1, 1, 1]

myPerceptron = Perceptron(epochCount = myEpochCount)

myPerceptron.fit(xMatrix = xMatrix,
                 yVector = yVector
                 )


