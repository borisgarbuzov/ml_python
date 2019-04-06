from scipy.spatial.distance import pdist, squareform
from scipy import exp
from numpy.linalg import eigh
import numpy as np


def rbf_kernel_pca(X, gamma, n_components):
    # попарно вычисляем квадратичные евклидовы расстояния
    sq_dists = pdist(X, 'sqeuclidean')

    # попарно конвертируем расстояния в квадратную матрицу
    mat_sq_dists = squareform(sq_dists)

    # вычисляем симметричную матрицу ядра
    K = exp(-gamma * mat_sq_dists)

    # Центрируем матрицу ядра
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # извлекаем собственные пары из центрированной матрицы ядра
    # функция numpy.eigh возвращает их в отсортированном порядке
    eigvals, eigvecs = eigh(K)

    # берем k верхних собственных векторов (спроецированные образцы)
    X_pc = np.column_stack((eigvecs[:, -i]
                            for i in range(1, n_components + 1)))

    return X_pc
