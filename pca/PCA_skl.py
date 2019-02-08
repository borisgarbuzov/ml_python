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
X_train_pca = pca.fit_transform(X_train_std)

# print ("pca.explained_variance_ratio_ =", pca.explained_variance_ratio_)


