# C:\Users\Boris\AppData\Local\Programs\Python\Python36-32
import numpy as np
import random
from Tree import Tree
import statistics

class RandomForest(object):
    def __init__(self, studentCount, maxLevel = 10):
        self.studentCount = studentCount
        # print("studentCount =", studentCount)
        self.maxLevel = maxLevel
        # print("maxLevel =", maxLevel)

    # public. Called from main
    def fit(self, X, y, colCount):
        # we pass just colCount
        # rowCount will be the same as beore
        # print("X =", X)
        # print("y =", y)
        # construct Tree studentCount times
        self.studentTrees = []
        self.studentColIndexSamples = []

        for studentIndex in range(self.studentCount):
            # print("studentIndex =", studentIndex)
            self.studentTrees.append(Tree(max_level = self.maxLevel))
            # bootstrap X, y studentCount times and fit each student
            xColCount = X.shape[1]
            colIndexSample = np.random.choice(
                a=range(xColCount), size=colCount, replace=False)
            # print("colIndexSample =", colIndexSample)
            self.studentColIndexSamples.append(colIndexSample)
            # bigger and with replacement
            rowSampleSize = X.shape[0]
            rowIndexSample = np.random.choice(
                a=range(X.shape[0]), size=rowSampleSize, replace=True)
            # print("rowIndexSample =", rowIndexSample)
            # form X submatrix studentX with row and col sampled
            xRowSample = np.take(a=X, indices=rowIndexSample, axis=0)
            # print("xRowSample =", xRowSample)
            xRowColSample = np.take(a=xRowSample, indices=colIndexSample, axis=1)
            yRowSample = np.take(a=y, indices=rowIndexSample, axis=0)
            # print("yRowSample =", yRowSample)

            # store our indexes for predict
            # form X and y for these indexes
            # all we did put into a function
            self.studentTrees[studentIndex].fit(xRowColSample, yRowSample)




    # public. Called from main
    # note, newX is a row vector
    def predict(self, newX):
        # print("newX =", newX)
        studentPredictedYArray = []
        # ask the array of fit students, give newX to each of them
        for studentIndex in range(len(self.studentTrees)):
            # form col subsample of newX
            # ask a student, which columns you need
            studentColIndexSample = self.studentColIndexSamples[studentIndex]
            newStudentX = np.take(a=newX, indices=studentColIndexSample)
            predictedY = self.studentTrees[studentIndex].predict(newStudentX)
            studentPredictedYArray.append(predictedY)
        # get an array of predictedY
        # final predictedY = mode(array of predictedY)
        # print("studentPredictedYArray = ", studentPredictedYArray)
        # predictedY = statistics.mode(studentPredictedYArray)
        predictedY = max(studentPredictedYArray, key=studentPredictedYArray.count)

        return (predictedY)
