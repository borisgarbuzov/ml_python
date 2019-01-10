import numpy as np
import statistics

myArray = ["a", "b", "c", "d"]
for index, value in enumerate(myArray):
    print("index =", index, " value =", value)

myEnumerate = enumerate(myArray)
print("myEnumerate =", myEnumerate)

# for studentIndex in range(self.studentCount):
#     bootstrapX = []
#     rowIndexArray = sorted(np.random.randint(0, len(X), size=len(X)))
#     colIndexArray = sorted(random.sample(range(0, len(X[0])), colCount))
#
#     for rowIndex in range(rowIndexArray.__len__()):
#         bootstrapX.append([])
#         for colIndex in range(colIndexArray.__len__()):
#             bootstrapX[rowIndex] = \
#                 X[rowIndexArray[rowIndex]][colIndexArray[colIndex]]

# for k, i in enumerate(rowIndexArray):
#     bootstrapX.append([])
#     for j in colIndexArray:
#         bootstrapX[k].append(X[i][j])

myNumArray = [11, 12, 13, 14, 15]
print("myNumArray[1:4] =", myNumArray[1:4])
myRange = range(1,5)
print("myRange =", myRange)
print("myRange[0] =", myRange[0])
print("myRange[1] =", myRange[1])
for rangeIndex in [0,1, 2, 3, 4]:
    print("fake line")

subsetArray = []
for rangeIndex in [0,0, 3]:
    print("myNumArray[rangeIndex] =", myNumArray[rangeIndex])
    subsetArray.append(myNumArray[rangeIndex])

print("subsetArray =", subsetArray)

# Now a matrix

newArray = []
for rangeIndex in range(5):
    print("rangeIndex =", rangeIndex)
    newArray.append(rangeIndex)

print("newArray =", newArray)

# alternatively in one line
new2Array = [rangeIndex for rangeIndex1 in range(5)]
print("new2Array =", new2Array)
# B: new2Array fills as before
# M: new2Array = [4,4,4,4,4] - right
new2Array = [rangeIndex for rangeIndex1 in [4, 4, 4, 4, 4]]
print("new2Array =", new2Array)

# matrix in double loop
newMatrix = []
for rowIndex in range(2):
    print("rowIndex =", rowIndex)
    newRow = []
    for colIndex in range(3):
        print("colIndex =", colIndex)
        newRow.append(rowIndex + colIndex)
    newMatrix.append(newRow)
print("newMatrix =", newMatrix)

# ours
newArray = [50, 40, 30, 20, 10]
indexArray = np.random.randint(0, len(newArray), size=len(newArray))
print("indexArray =", indexArray)
bootstrapArray = []
for obsIndex in indexArray:
    bootstrapArray.append(newArray[obsIndex])
print("bootstrapArray =", bootstrapArray)

# online
bootstrapArray = np.random.choice(newArray, 5, p=[0.2, 0.2, 0.2, 0.2, 0.2])
print("bootstrapArray =", bootstrapArray)

# default p?
bootstrapArray = np.random.choice(newArray, 15)
print("bootstrapArray =", bootstrapArray)

# now without repetitions
newArray = [50, 40, 30, 20, 10]
del newArray[0]
print("newArray =", newArray)
print("put it back")
newArray.insert(0, 50)
print("newArray =", newArray)
print("Take 4 out of 5")
noRepeatSample = []
sampleSize = 4
newArrayRemainder = newArray # try
del newArrayRemainder[0]
print("newArray =", newArray)
print("newArrayRemainder =", newArrayRemainder)
# So they are different aliases of the same object
print("put it back")
newArrayRemainder.insert(0, 50)
print("newArray =", newArray)
print("newArrayRemainder =", newArrayRemainder)
# not to damage the original
newArrayRemainder = newArray [:]
del newArrayRemainder[0]
print("newArray =", newArray)
print("newArrayRemainder =", newArrayRemainder)
print("put it back")
newArrayRemainder.insert(0, 50)
print("newArray =", newArray)
print("newArrayRemainder =", newArrayRemainder)
sample = np.random.choice(a = newArray, size=sampleSize, replace=False)
print("sample =", sample)
print("This should be equivalent to shuffle")
sample = np.random.choice(a = newArray, size=len(newArray), replace=False)
print("sample =", sample)
# try to exceed the size
# sample = np.random.choice(a = newArray, size=len(newArray)+1, replace=False)
# we can use this sampling without replacement for columns in forest

# choose columns from indexes without replacement
# choose rows from values with replacement
# first list of indexes in rows and columns
colSampleSize = len(newArray) - 1
colIndexSample = np.random.choice(
    a = range(len(newArray)), size=colSampleSize, replace=False)
print("colIndexSample =", colIndexSample)

# bigger and with replacement
rowSampleSize = len(newArray)
rowIndexSample = np.random.choice(
    a = range(len(newArray)), size=rowSampleSize, replace=True)
print("rowIndexSample =", rowIndexSample)

data = [
    [11, 12],
    [21, 22],
    [31, 32]
]
print("data =", data)

X = np.array(data)
print("X =", X)
myShape = np.shape(X)
print("myShape =", myShape)
print("Another way. X.shape =", X.shape)

# subsetting by index
myArray = np.array([10, 20,30])
indexSubset = [0, 2]
arraySubset = np.take(a=myArray, indices=indexSubset)
print("arraySubset =", arraySubset)

# now multidimensional
data = [
    [11, 12],
    [21, 22],
    [31, 32]
]
X = np.array(data)
print("data =", data)
rowIndexSubset = [0, 2, 2]
xRowSubset = np.take(a=X, indices=rowIndexSubset, axis=0)
print("xRowSubset =", xRowSubset)
colIndexSubset = [1]
xColSubset = np.take(a=xRowSubset, indices=colIndexSubset, axis=1)
print("xColSubset =", xColSubset)

# mode of equal frequency
myArray = [1, 1, 2, 2, 2]
predictedY = statistics.mode(myArray)
print("predictedY =", predictedY)



