import numpy as np


def matrix_multiplication(u, sigma, v_transpose):
    result = np.dot(u, np.dot(sigma, v_transpose))
    return result

u = np.array([
    [np.sqrt(3)/2, 0, -1/2], 
    [0,            -1, 0],
    [1/2,           0, np.sqrt(3)/2]
    ])

sigma = np.array([
    [3, 0],
    [0, 1],
    [0, 0]
    ])

v = np.array([
    [np.sqrt(3)/2, 1/2],
    [-1/2,          np.sqrt(3)/2]
    ])

v_transpose = np.transpose(v)

x = matrix_multiplication(u, sigma, v_transpose)
print("x = ")
print(x)

c = np.dot(np.transpose(x), x)
print("c = \n", c)

ker = np.dot(x, np.transpose(x))
print("ker = \n", ker)

cEigenvalues, cEigenvectors = np.linalg.eig(c)
print("cEigenvalues = \n", cEigenvalues)
print("cEigenvectors = \n", cEigenvectors)
print("v = \n", v)

cEqualsV = cEigenvectors == v
print("cEqualsV = \n", cEqualsV)

cDifV = cEigenvectors - v
cDifVAround = np.around(cDifV, 3)
cDifVAroundEquals0 = cDifVAround == 0
print("cDifVAroundEquals0 = \n", cDifVAroundEquals0)

xPrime = np.dot(x, v)
print("xPrime = \n", np.around(xPrime,2))
print("x = \n", np.around(x,2))
print("u = \n", np.around(u,2))




