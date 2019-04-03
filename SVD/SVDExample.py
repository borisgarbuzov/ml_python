import numpy as np


def matrix_multiplication(u, sigma, v_transpose):
    result = np.dot(u, np.dot(sigma, v_transpose))
    return result

u = np.array([
    [np.sqrt(3)/2, 0, -1/2], 
    [0, -1, 0],
    [1/2, 0, np.sqrt(3)/2] 
    ])

sigma = np.array([
    [3, 0],
    [0, 1],
    [0, 0]
    ])

v_transpose = np.array([
    [np.sqrt(3)/2, -1/2],
    [1/2, np.sqrt(3)/2]
    ])

X = matrix_multiplication(u, sigma, v_transpose)
print(X)
