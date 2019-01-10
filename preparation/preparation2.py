
import pandas as pd
import numpy as np

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']

X = df[['color', 'size', 'price']].values



print ("X =", X )

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
# transformedX0 = ohe.fit_transform(X).toarray()
# print ("transformedX0 =", transformedX0 )

myEncoding = pd.get_dummies(df[['price', 'color', 'size']])
print ("myEncoding =\n", myEncoding )


df_wine = pd.read_csv(\
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df_wine.columns = ['Class label', 'Alcohol',
 'Malic acid', 'Ash',
 'Alcalinity of ash', 'Magnesium',
 'Total phenols', 'Flavanoids',
 'Nonflavanoid phenols',
 'Proanthocyanins',
 'Color intensity', 'Hue',
 'OD280/OD315 of diluted wines',
 'Proline']
print('Class labels', np.unique(df_wine['Class label']))
print('df_wine.head()', np.unique(df_wine.head()))

from sklearn.model_selection import train_test_split
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = \
train_test_split(X, y, test_size=0.3, random_state=0)
print ("X_train =\n", X_train)
print ("X_test =\n", X_test)
print ("y_train =\n", y_train)
print ("y_test =\n", y_test)

from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
print ("X_train_norm =\n", X_train_norm)
print ("X_test_norm =\n", X_test_norm)
print ("-------begin-----------")
print ("min(X_train_norm[:][0]) =\n", min(X_train_norm[:][0]))
print ("max(X_train_norm[:][0]) =\n", max(X_train_norm[:][0]))
print ("-------end-----------")

# print ("X_train[:][0] =\n", X_train[:][0])
# print ("X_train_norm[:][0] =\n", X_train_norm[:][0])

print ("min(X_train_norm[:, 1]) =\n", min(X_train_norm[:, 1]))
print ("max(X_train_norm[:, 1]) =\n", max(X_train_norm[:, 1]))

from sklearn.preprocessing import StandardScaler
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)
print ("X_train_std =\n", X_train_std)
print ("min(X_test_std[:, 1]) =", min(X_test_std[:, 1]))
print ("max(X_test_std[:, 1]) =", max(X_test_std[:, 1]))
print ("np.mean(X_test[:, 1]) =", np.mean(X_test[:, 1]))
print ("np.mean(X_train[:, 1]) =", np.mean(X_train[:, 1]))
print ("np.mean(X_test_std[:, 1]) =", np.mean(X_test_std[:, 1]))
print ("np.mean(X_train_std[:, 1]) =", np.mean(X_train_std[:, 1]))





















