import numpy as np
from sklearn.preprocessing import scale

X = np.array([4., 5., 2., 1.], dtype=np.float64)
Y = np.array([6., 3., -4., 7.], dtype=np.float64)

cov = np.cov(X, Y, bias=True)
cor = np.corrcoef(X, Y)

# ---------------------------------------------------------

X_std = scale(X)
Y_std = scale(Y)

cov_std = np.cov(X_std, Y_std, bias=True)

print("cov =", cov[0][1])
print("cor =", cor[0][1])
print("cov_std =", cov_std[0][1])

xMatrix = []
xMatrix.append(X)
xMatrix.append(Y)
xMatrix = np.array(xMatrix)
print("xMatrix =\n", xMatrix)

covMatrixBias = np.cov(xMatrix, bias=True)
print("covMatrixBias =\n", covMatrixBias)
covMatrixNoBias = np.cov(xMatrix, bias=False)
print("covMatrixNoBias =\n", covMatrixNoBias)

corMatrix = np.corrcoef(xMatrix)
print("corMatrix =\n", corMatrix)










