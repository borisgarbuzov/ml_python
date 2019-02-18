import numpy as np

kMatrix = np.matrix(
    [[1, 1],
    [1, 2]]
)
One2 = np.matrix(
    [[1/2, 1/2],
    [1/2, 1/2]]
)
print ("kMatrix.dot(One2) =\n", kMatrix.dot(One2))
print ("One2.dot(kMatrix) =\n", One2.dot(kMatrix))
print ("One2.dot(kMatrix).dot(One2) =\n", One2.dot(kMatrix).dot(One2))
mySum = kMatrix.dot(One2) + One2.dot(kMatrix) + One2.dot(kMatrix).dot(One2)
print ("mySum =\n", mySum)
print ("kMatrix-mySum =\n", kMatrix-mySum)


