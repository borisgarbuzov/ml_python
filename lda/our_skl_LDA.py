from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

# Создаем выборку X
X = np.array([[0, 0],
              [4, 4],
              [4, 6],
              [8, 2]])
y = np.array([1, 1, 2, 2])

# Инициализируем наш классификатор и передаем ему выборку
lda = LinearDiscriminantAnalysis()
ldx = lda.fit_transform(X, y)

print("X':\n", ldx)
