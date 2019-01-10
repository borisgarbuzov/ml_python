# C:\Users\Boris\AppData\Local\Programs\Python\Python36-32
import numpy as np
import math
from sklearn.tree import DecisionTreeClassifier
from statistics import mode


class Point():

    def __init__(self):
        self.level = None
        self.variable = None
        self.value = None
        self.left_point = None
        self.right_point = None
        self.entrophy = None
        self.end_value = None


class Tree():

    def __init__(self, max_level):
        self.max_level = max_level
        self.first_point = Point()


    def compute_entrophy(self, y):
        classes = []
        for i in range(0, len(y)):
            add = True
            for j in range(0, len(classes)):
                if y[i] == classes[j]:
                    add = False
                    break
            if add:
                classes.append(y[i])

        p = []
        for i in range(0, len(classes)):
            p.append(0)
            for j in range(0, len(y)):
                if classes[i] == y[j]:
                    p[i] += 1
            p[i] = p[i]/len(y)

        entrophy = 0
        for i in range(0, len(p)):
            entrophy -= p[i] * math.log(p[i], 2)

        return (entrophy)


    def compute_information_gain(self, yLeft, yRight, y):
        IG = (self.compute_entrophy(y) -
             math.pow(len(yLeft)/len(y), 2) * self.compute_entrophy(yLeft) -
             math.pow(len(yRight)/len(y), 2) * self.compute_entrophy(yRight))
        return (IG)


    def find_max_information_gain(self, X, y):
        max_variable = 0
        max_value = 0
        max_IG = 0
        for i in range(0, len(X)):
            for j in range(0, len(X[i])):
                y_left = []
                y_right = []
                for k in range(0, len(X)):
                    if X[k][j] >= X[i][j]:
                        y_right.append(y[k])
                    else:
                        y_left.append(y[k])
                IG = self.compute_information_gain(y_left, y_right, y)
                if IG > max_IG:
                    max_IG = IG
                    max_value = X[i][j]
                    max_variable = j
        return ([max_variable, max_value, max_IG])

    def add_new_point(self, point, X, y, level):
        # print(level)
        point.level = level
        entrophy = self.compute_entrophy(y)
        point.entrophy = entrophy
        if (point.entrophy == 0) or (level == self.max_level):
            # point.end_value = mode(y)
            # does it substitute for mode?
            point.end_value = max(y, key=y.count)

        else:
            IG = self.find_max_information_gain(X, y)
            point.variable = IG[0]
            point.value = IG[1]
            X_left = []
            X_right = []
            y_left = []
            y_right = []
            for i in range(0, len(X)):
                if X[i][point.variable] >= point.value:
                    X_right.append(X[i])
                    y_right.append(y[i])
                else:
                    X_left.append(X[i])
                    y_left.append(y[i])
            if len(y_right) != 0:
                point.right_point = Point()
                self.add_new_point(point=point.right_point, X=X_right, y=y_right, level=level+1)
            if len(y_left) != 0:
                point.left_point = Point()
                self.add_new_point(point=point.left_point, X=X_left, y=y_left, level=level+1)


    def fit(self, X_train, y_train):
        self.add_new_point(point=self.first_point, X=X_train, y=y_train, level=0)

    def predict(self, X):
        point = self.first_point
        while point.end_value == None:
            if X[point.variable] >= point.value:
                point = point.right_point
            else:
                point = point.left_point
        return (point.end_value)
