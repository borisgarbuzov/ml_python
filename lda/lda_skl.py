from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_wine

myData = load_wine()
y = myData["target"]
print("y = ", y)
X = myData["data"]
print("X = \n", X)
print("X.shape = ", X.shape)

lda = LinearDiscriminantAnalysis(n_components=2)
xLda = lda.fit_transform(X=X, y=y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(xLda, y, random_state=0, test_size=0.25)
print("X_train = \n", X_train)
print("X_test = \n", X_test)
print("X_train.shape = ", X_train.shape)
print("X_test.shape = ", X_test.shape)

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

from matplotlib.colors import ListedColormap
import numpy as np

# =========their code===========================
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)
# ====================================

lr = LogisticRegression()
lr = lr.fit(X_train, y_train)
plot_decision_regions(X_train, y_train, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='lower left')
plt.show()
