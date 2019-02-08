import numpy as np
import matplotlib.pyplot as plt

m = np.array([[2.5, 0.5], [0.5, 18.5]]) # M
m = np.array([[1, 0.622], [0.622, 1]]) # AJ


eigenvalues, eigenvectors = np.linalg.eig(m)

print("Собственные значение:", eigenvalues)
print("Собственные вектора:", eigenvectors)

plt.plot(eigenvectors)
plt.show()
