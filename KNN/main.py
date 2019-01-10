import KNN, numpy

trainingXdata = [
    [175, 77],
    [187, 80],
    [178, 65],
    [165, 55],
    [160, 50],
    [178, 65]
]
trainingX = numpy.array(trainingXdata)
trainingYdata = [1, 1, 1, 2, 2, 2]
trainingY = numpy.array(trainingYdata)
neighborCount = 3
print("neighborCount = ", neighborCount)
print("trainingX = ", trainingX)
print("trainingY = ", trainingY)


myKNN = KNN.KNN(neighborCount)

myKNN.fit(trainingX=trainingX, trainingY=trainingY)

newX = [170, 65.5]
print("newX = ", newX)

predictedY = myKNN.predict(newX)
print("predictedY = ", predictedY)
