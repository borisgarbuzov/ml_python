import copy

class Perceptron:

    def __init__(self, epochCount, learningSpeed):
        print("\n Perceptron gets constructed \n")
        print("\n epochCount = ", epochCount, "\n")
        self.innerEpochCount = epochCount
        self.learningSpeed = learningSpeed


    def predict (self, xVectorExtended):
        return self.phi (self.computePureInput(xVectorExtended))


    def phi (self, pureInput):

        predictedValue = 0 if pureInput < 0 else 1
        '''
        if pureInput < 0:
            predictedValue = 0
        else :
            predictedValue = 1
        '''
        return predictedValue


    def computePureInput (self, xVectorExtended):
        pureInput = sum([currentWeight * currentX
                 for currentWeight, currentX
                 in zip(self.weightVector, xVectorExtended)])
        return pureInput


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
        self.weightVector = []
        for columnIndex in range (0, columnCount):
            self.weightVector.append(0)
        print("weightVector: ", self.weightVector)

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
                yPredicted = self.predict(xMatrixExtended[objectIndex])
                deltaWeightVector = []
                # update the weights
                # how to multiply vector by scalar?
                for currentX in xMatrixExtended[objectIndex]:
                    deltaWeightVector.append((self.learningSpeed *
                                        (yVector[objectIndex] - yPredicted) *
                                        currentX
                                        ))
                # weight += deltaWeight
                self.weightVector = [weight + deltaWeight for weight, deltaWeight in zip(self.weightVector, deltaWeightVector)]

                print("yPredicted inside the loop: ", yPredicted)
                print("deltaWeightVector inside the loop: ", deltaWeightVector)
                print("weightVector inside the loop: ", self.weightVector)


        # outside the loop
        print("yPredicted exists outside the loop: ", yPredicted)
        print("deltaWeightVector exists outside the loop: ", deltaWeightVector)



