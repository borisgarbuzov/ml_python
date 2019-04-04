import numpy as np
import matplotlib.pyplot as plt


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

xC = np.dot(centering3, x)
print("xC = \n", xC)

xtx = np.dot(np.transpose(x), x)
print("xtx = \n", xtx)

xxt = np.dot(x, np.transpose(x))
print("xxt = \n", xxt)

cEigenvalues, cEigenvectors = np.linalg.eig(xtx)
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




xxtEigenvalues, xxtEigenvectors = np.linalg.eig(xxt)
print("xxtEigenvalues = \n", xxtEigenvalues)
print("xxtEigenvectors = \n", np.around(xxtEigenvectors,2))
print("u = \n", np.around(u,2))

uSigma = np.dot(u, sigma)
print("uSigma = \n", np.around(uSigma,2))
print("xPrime = \n", np.around(xPrime,2))


# plt.show()
plt.plot(x[:, 0], x[:, 1], 'o')
plt.plot(xPrime[:, 0], xPrime[:, 1], 'o')
# plt.ylim(-1.4, 0)
plt.savefig('plot_of_x.png')
plt.show()
plt.plot(xC[:, 0], xC[:, 1], 'o')

# plt.ylim(-1.4, 0)
plt.savefig('plot_of_xC.png')

