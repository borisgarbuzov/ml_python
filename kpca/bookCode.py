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
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)
    # Obtaining eigenpairs from the centered kernel matrix
    # numpy.eigh returns them in sorted order
    eigvals, eigvecs = eigh(K)
    # Collect the top k eigenvectors (projected samples)
    X_pc = np.column_stack((eigvecs[:, -i]
                            for i in range(1, n_components + 1)))
    return X_pc

import pandas as pd
from sklearn.preprocessing import StandardScaler

df_wine = pd.read_csv('https://raw.githubusercontent.com/rasbt/python-machine-learning-book/master/code/datasets/wine/wine.data', header=None)
scaler = StandardScaler()
X = df_wine.iloc[:, 1:].values
X_std = scaler.fit_transform(X)
y = df_wine.iloc[:,0].values
# print ("df_wine.head() =", df_wine.head())

n_components = 2
gamma = 1/2
myX_pc = rbf_kernel_pca(X, gamma, n_components)
print ("myX_pc =\n", myX_pc)
print ("myX_pc.shape =", myX_pc.shape)

import matplotlib.pyplot as plt
