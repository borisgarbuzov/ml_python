import numpy as np
import matplotlib.pyplot as plt
from kernel_pca_func import rbf_kernel_pca
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import KernelPCA
import math

X = np.array([[1, 2, 3],
              [1.1, 1.9, 3.1],
              [1.8, 2.2, 2.7],
              [-1, -2, -3],
              [-1.1, -1.9, -3.1],
              [-1.8, -2.2, -2.7]])
print("X=\n", X)

# standartization
sc = StandardScaler()
X_standard = sc.fit_transform(X)
print("X_standard=\n", np.around(X_standard, 2))

# covariation
cov_matrix = np.cov(X_standard.T)
print("cov_matrix=\n", np.around(cov_matrix, 2))

# xtx
XTX = np.dot(X_standard.T, X_standard)
print("XTX=\n", np.around(XTX, 2))

# xtx eigenvectros, eigenvalues
eigvalues, eigvectors = np.linalg.eig(XTX)
print("XTX eigvalues=\n", np.around(eigvalues, 2))
print("XTX eigvectors=\n", np.around(eigvectors, 2))

# cov eigenvectros, eigenvalues
eigvalues, eigvectors = np.linalg.eig(cov_matrix)
print("eigvalues=\n", np.around(eigvalues, 2))
print("eigvectors=\n", np.around(eigvectors, 2))

# matrix X by eigvectors
X_prim = np.dot(X, eigvectors)
print("X_prim=\n", np.around(X_prim, 2))
print("X_standard=\n", np.around(X_standard, 2))

scikit_pca = PCA(n_components=3)
X_sklearn_transformed = scikit_pca.fit_transform(X)
print("X_sklearn_transformed=\n", np.around(X_sklearn_transformed, 2))

# matrix 6 by 6
XXT = np.dot(X_standard, X_standard.T)
print("XXT=\n", np.around(XXT, 2))

# eigenvalues and vectors of XXT
eigvalues_XXT, eigvectors_XXT = np.linalg.eig(XXT)
print("eigvalues_XXT=\n", np.around(eigvalues_XXT, 1))
print("eigvectors_XXT=\n", np.around(eigvectors_XXT, 1))

# first two columns of XXT
two_columns_XXT = XXT[:, :2]
print("two_columns_XXT=\n", np.around(two_columns_XXT, 2))
print("X_sklearn_transformed=\n", np.around(X_sklearn_transformed[:, :2], 2))
print("X_prim=\n", np.around(X_prim[:, :2], 2))

scikit_kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)
X_skernpca = scikit_kpca.fit_transform(X)
print("X_skernpca=\n", np.around(X_skernpca, 2))

books_kpca, K = rbf_kernel_pca(X = X, gamma=1, n_components=2)
print("books_kpca=\n", np.around(books_kpca, 2))
print("Kernel=\n", np.around(K, 2))
print("XXT=\n", np.around(XXT, 2))

expXXT = np.exp (XXT)
print("expXXT=\n", np.around(expXXT, 1))
