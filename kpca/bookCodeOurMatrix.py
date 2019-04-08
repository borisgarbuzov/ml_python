from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np

def rbf_kernel_pca(X, gamma, n_components):
    sq_dists = pdist(X, 'sqeuclidean')
    # Convert pairwise distances into a square matrix.
    mat_sq_dists = squareform(sq_dists)
    # Compute the symmetric kernel matrix.
    K = exp(-gamma * mat_sq_dists)

    # Center the kernel matrix.
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    print("K = \n", K)
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)
    print("Kcentered = \n", K)
    # Obtaining eigenpairs from the centered kernel matrix
    # numpy.eigh returns them in sorted order
    eigvals, eigvecs = eigh(K)
    print("eigvals = ", eigvals)
    print("eigvecs = \n", eigvecs)
    # Collect the top k eigenvectors (projected samples)
    X_pc = np.column_stack((eigvecs[:, -i]
                            for i in range(1, n_components + 1)))

    return X_pc

import pandas as pd
from sklearn.preprocessing import StandardScaler

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

Identitty3 = np.identity(3)
print("Identitty3 = \n", Identitty3)
allOneThird = 1/3 * np.ones((3, 3))
print("allOneThird = \n", allOneThird)
centering3 = Identitty3 - allOneThird
print("centering3 = \n", centering3)

v_transpose = np.transpose(v)

x = matrix_multiplication(u, sigma, v_transpose)
print("x = ")
print(x)


n_components = 2
gamma = 1/2
myX_pc = rbf_kernel_pca(x, gamma, n_components)
print ("myX_pc =\n", myX_pc)
print ("myX_pc.shape =", myX_pc.shape)

import matplotlib.pyplot as plt
