import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df_wine = pd.read_csv(url, header=None)
print ("df_wine = \n", df_wine)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = \
    train_test_split(X, y,
    test_size=0.3, random_state=0)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)
print ("mean(X_train_std[:,0]) = ", np.mean(X_train_std[:,0] ))
print ("type(X_train_std) = ", type(X_train_std))
print ("var(X_train_std[:,0]) = ", np.var(X_train_std[:,0] ))
