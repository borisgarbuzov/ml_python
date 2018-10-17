import copy

class Perceptron:

    def __init__(self, epochCount, learningSpeed):
        print("\n Perceptron gets constructed \n")
        print("\n epochCount = ", epochCount, "\n")
        self.innerEpochCount = epochCount
        self.learningSpeed = learningSpeed

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
        for columnIndex in range (0, columnCount):
            weightVector.append(0)
        print("weightVector: ", weightVector)

        deltaWeightVector = []
        for columnIndex in range (0, columnCount):
            deltaWeightVector.append(0)
        # data structures are created.

        # Now let us fit the data
        for epoch in range (0, self.innerEpochCount):
            for objectIndex in range (0, objectCount):
                # modify this multiplication
                print("epoch = ", epoch)
                print("objectIndex = ", objectIndex)

                pureInput = sum([currentWeight * currentX
                                 for currentWeight, currentX
                                 in zip(weightVector, xMatrixExtended[objectIndex])])
                yPredicted = self.predict(pureInput)
                # update the weights
                deltaWeightVector = (learningSpeed *
                                    (yVector[objectIndex] - yPredicted) *
                                     xMatrixExtended[objectIndex]
                                     )
                print("pureInput inside the loop: ", pureInput)
                print("yPredicted inside the loop: ", yPredicted)
                print("deltaWeightVector inside the loop: ", deltaWeightVector)


        # outside the loop
        print("pureInput exists outside the loop: ", pureInput)
        print("yPredicted exists outside the loop: ", yPredicted)
        print("deltaWeightVector exists outside the loop: ", deltaWeightVector)






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
learningSpeed = 1/2
myPerceptron = Perceptron(epochCount = myEpochCount,
                          learningSpeed = learningSpeed)

myPerceptron.fit(xMatrix = xMatrix,
                 yVector = yVector
                 )


