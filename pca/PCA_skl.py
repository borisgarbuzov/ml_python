import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df_wine = pd.read_csv('https://raw.githubusercontent.com/rasbt/python-machine-learning-book/master/code/datasets/wine/wine.data', header=None)
scaler = StandardScaler()
X = df_wine.iloc[:, 1:].values
X_std = scaler.fit_transform(X)
y = df_wine.iloc[:,0].values
x_train_std, x_test_std, y_train, y_test = train_test_split(X_std,
                                                            y,
                                                            random_state = 42,
                                                            test_size = 0.25)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 
'Alcalinity of ash', 'Magnesium', 'Total phenols', 
'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 
'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
# print ("df_wine.head() =", df_wine.head())


from sklearn.decomposition import PCA

pca = PCA(n_components = 2)
x_train_pca = pca.fit_transform(x_train_std)
print ("x_train_pca =", x_train_pca)
print ("x_train_pca.shape =", x_train_pca.shape)
print ("x_train_std.shape =", x_train_std.shape)
x_test_pca = pca.transform(x_test_std)
print ("x_test_pca =", x_test_pca)
print ("x_test_pca.shape =", x_test_pca.shape)

# fit regression on both - pca and original

import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

timeOriginalStart = time.time()
logisticClassifierOriginal = LogisticRegression(random_state=0,
                                                C=1)
logisticClassifierOriginal.fit(X = x_train_std,
                               y = y_train)
print("performace quality of logisticClassifierOriginal",
      accuracy_score(y_test, logisticClassifierOriginal.predict(x_test_std)))
timeOriginalEnd = time.time()
originalDuration = timeOriginalEnd - timeOriginalStart
print("duration of the original classifier work", originalDuration)

timePcaStart = time.time()
logisticClassifierPca = LogisticRegression(random_state=0,
                                                C=1)
logisticClassifierPca.fit(X = x_train_pca,
                               y = y_train)
print("performace quality of logisticClassifierPca",
      accuracy_score(y_test, logisticClassifierPca.predict(x_test_pca)))
timePcaEnd = time.time()
pcaDuration = timePcaEnd - timePcaStart
print("duration of the PCA classifier work", pcaDuration)
durationDifference = originalDuration - pcaDuration
print("durationDifference", durationDifference)
print("durationDifference >= 0", durationDifference >= 0)












