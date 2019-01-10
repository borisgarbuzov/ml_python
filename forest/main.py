import RandomForest as rf
import numpy as np

myForest = rf.RandomForest(maxLevel= 5, studentCount= 100)
xData =[[0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]]
X = np.array(xData)
print("main: X =", X)

yData = [0, 1, 1, 0, 1, 0, 1, 0]
y = np.array(yData)
print("main: y =", y)

myForest.fit(X = X, y = y, colCount = 2)
newX = np.array([0, 0, 0])
print("main: newX =", newX)

predictedY = myForest.predict(newX = newX)
print("main: predictedY =", predictedY)
