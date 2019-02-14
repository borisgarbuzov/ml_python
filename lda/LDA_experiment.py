import numpy as np
z = np.array([
[0,0],
[4,4],
[4,6],
[8,2]
])
y = [1, 1, 2, 2]

zcolmeans = z.mean(axis=0)
print ("zcolmeans =", zcolmeans)
z0 = z - zcolmeans
print ("z0 =", z0)
z0colmeans = z0.mean(axis=0)
print ("z0colmeans =", z0colmeans)

zStDev = z.std(axis=0)
print ("zStDev =", zStDev)
z0StDev = z0.std(axis=0)
print ("z0StDev =", z0StDev)

zStandard = z0 / z0StDev
print ("zStandard =\n", zStandard)

# transpose and multiply matrix
rowCount = zStandard.shape[0]
print ("rowCount =", rowCount)
varMatrix = zStandard.T.dot(zStandard) / rowCount
varMatrixMatmul = np.matmul(zStandard.T, zStandard) / rowCount
print ("varMatrix =\n", varMatrix)
print ("varMatrixMatmul =\n", varMatrixMatmul)
z12cor = np.corrcoef(z[:,0],z[:,1])
print ("z12cor =\n", z12cor)
z12corStandard = np.corrcoef(zStandard[:,0], zStandard[:,1])
print ("z12corStandard =\n", z12corStandard)

# ===============================
x = zStandard
# subset of x rows y = 1
y = np.array(y)
yBoolean = y==1
print ("yBoolean =", yBoolean)
xc1 = x [y==1]
print ("xc1 =\n", xc1)
xc2 = x [y==2]
print ("xc2 =\n", xc2)

meanClass1 = np.mean(xc1, axis=0)
print ("meanClass1 =", meanClass1)
meanClass2 = np.mean(xc2, axis=0)
print ("meanClass2 =", meanClass2)
xc1Centered = xc1 - meanClass1
print ("xc1Centered =\n", xc1Centered)
xc2Centered = xc2 - meanClass2
print ("xc2Centered =\n", xc2Centered)

# outer product of each row of class 1
# add them
# cycle over the rows of the first class
# lines 1,2 or in Python 0, 1
sSize = xc1Centered.shape[0]
print ("rows in  xc1Centered:", sSize)
s1Matrix = np.zeros_like(xc1Centered)
print ("s1Matrix =\n", s1Matrix)

for rowIndex in range(0, 2) :
    currentRow = xc1Centered [rowIndex, :]
    print("currentRow =", currentRow)
    currentOuterProduct = np.outer(currentRow, currentRow)
    print("currentOuterProduct =\n", currentOuterProduct)
    s1Matrix += currentOuterProduct
print ("s1Matrix =\n", s1Matrix)

# same for the second class

















