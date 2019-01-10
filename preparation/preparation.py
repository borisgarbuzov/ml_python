import pandas as pd
import numpy as np


from io import StringIO

csv_data = '''A,B,C,D
1.0,2.0,-3.0,4000.0
5.0,6.0,,8.0
 0.0,11.0,,'''
df = pd.read_csv(StringIO(csv_data))
print("df =", df)
print("df.isnull().sum()", df.isnull().sum())
print("df =", int(6.7))
print("df =", np.int64(6.7))
print("df.values =", df.values)
my2dArray = [[1, 2, 3, 4000],
             [5, 6, None, 8],
             [0, 11, None, None]]
print("my2dArray =", my2dArray)
my3dArray = [[[1, 1], [2], [3], [4]],
             [[5], [6], [None], [8]],
             [[0], [11], [None], [None]]]
print("my3dArray =", my3dArray)
dfDroppedRowsNa = df.dropna()
print("dfDroppedRowsNa =", dfDroppedRowsNa)
dfDroppedColsNa = df.dropna(axis=1)
print("dfDroppedColsNa =", dfDroppedColsNa)
dfDroppedRowsWhenAllNa = df.dropna(how='all')
print("dfDroppedRowsWhenAllNa =", dfDroppedRowsWhenAllNa)
df.dropna(thresh=4)
df.dropna(subset=['C'])

print("============ transform ==================== ")

print("df =", df)
# transformedDf = est.transform(df)
# print ("transformedDf =", transformedDf)


print("============ anew ==================== ")
print("df =", df)

from sklearn.impute import SimpleImputer

imr = SimpleImputer(missing_values=np.nan, strategy='mean')
imr = imr.fit(df)
imputed_data = imr.transform(df.values)
print("imputed_data =", imputed_data)

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']
print("df =\n", df)

size_mapping = {
    'XL': ["a"],
    'L': 2,
    'M': 1}
print("type(size_mapping) =", type(size_mapping))
df['size'] = df['size'].map(size_mapping)
print("df =", df)
print("size_mapping =", size_mapping)
myKeys = size_mapping.keys()
myValues = size_mapping.values()
print("myKeys =", myKeys)
print("myValues =", myValues)
myXLValue = size_mapping['XL']
print("myXLValue =", myXLValue)
myPairs = size_mapping.items()
print("myPairs =", myPairs)
size_mapping = {
    'XL': 3,
    'L': 2,
    'M': 1}
inv_size_mapping = {v: k for k, v in size_mapping.items()}
print("inv_size_mapping =", inv_size_mapping)
# in full cycle
inv_size_mapping_by_full_cycle = {}
for k, v in size_mapping.items():
    inv_size_mapping_by_full_cycle[v] = k
print("inv_size_mapping_by_full_cycle =", inv_size_mapping_by_full_cycle)

print("Encoding class labels")

class_mapping = {label:idx for idx,label in\
    enumerate(np.unique(df['classlabel']))}
print("class_mapping =", class_mapping)
dfClassLabel = df['classlabel']
print("dfClassLabel =", dfClassLabel)
print("df =\n", df)
# df with col names
data = {'Commander': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'Date': ['2012, 02, 08', '2012, 02, 08', '2012, 02, 08', '2012, 02, 08', '2012, 02, 08'],
        'Score': [4, 24, 31, 2, 3]}
df2 = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print("df2 =\n", df2)
print("data[Commander] =", data['Commander'])
print("data[Date] =", data['Date'])
print("data[0] =", data['Commander'][1])
data['Commander'][1] = 'Bolly'
print("data[0] =", data['Commander'][1])
data ['Master'] = data.pop('Commander')
print("data =\n", data)
print("data.pop('Master') =", data.pop('Master'))
print("No master data =\n", data)

print ("df before =\n", df )
class_mapping = {label:idx for idx,label in\
enumerate(np.unique(df['classlabel']))}
print ("class_mapping =", class_mapping )
print ("enumerate(np.unique(df['classlabel'])) =", enumerate(np.unique(df['classlabel'])))
for idx, label in enumerate(np.unique(df['classlabel'])):
    print ("idx, label =", idx, label)

df['classlabel'] = df['classlabel'].map(class_mapping)
print ("df =\n", df )

# experiment with map
f1 = {1:10, 2:20}
myDf = pd.DataFrame([1, 1, 1, 2, 2, 2])
# myDf.map(f1)


# ---------------------------------
# Обработка  категориальных данных

import warnings
warnings.filterwarnings("ignore")

df = pd.DataFrame([
    ['green', 'M', 10.1, 'class1'],
    ['red', 'L', 13.5, 'class2'],
    ['blue', 'XL', 15.3, 'class1']])
df.columns = ['color', 'size', 'price', 'classlabel']
print("df =\n", df)

size_mapping = {'XL': 3,
                'L': 2,
                'M': 1}

df['size'] = df['size'].map(size_mapping)
print("df =\n", df)

from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)
print("y =", y)
inverseY = class_le.inverse_transform(y)
print("inverseY =", inverseY)

X = df[['color', 'size', 'price']].values
color_le = LabelEncoder()
X[:, 0] = color_le.fit_transform(X[:, 0])
print("X =\n", X)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
transformedX0 = ohe.fit_transform(X).toarray()
print("transformedX0 =\n", transformedX0)
