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

s2Matrix = np.zeros_like(xc2Centered)
print ("s2Matrix =\n", s2Matrix)
for rowIndex in range(0, 2) :
    currentRow = xc2Centered [rowIndex, :]
    print("currentRow =", currentRow)
    currentOuterProduct = np.outer(currentRow, currentRow)
    print("currentOuterProduct =\n", currentOuterProduct)
    s2Matrix += currentOuterProduct
print ("s2Matrix =\n", s2Matrix)
detS2 = np.linalg.det(s2Matrix)
print ("detS2 =", detS2) # same = 0

sWMatrix = s1Matrix + s2Matrix
print ("sWMatrix =\n", sWMatrix)

sigma1Matrix = sWMatrix / sSize
sigma2Matrix = sWMatrix / sSize
print ("sigma2Matrix =\n", sigma2Matrix)

xc1Colmeans = np.mean(a = xc1, axis=0)
print ("xc1Colmeans =", xc1Colmeans)
xc2Colmeans = np.mean(a = xc2, axis=0)
print ("xc2Colmeans =", xc2Colmeans)

sBOuter1 = np.outer(xc1Colmeans, xc1Colmeans)
print ("sBOuter1 =\n", sBOuter1)
sBOuter2 = np.outer(xc2Colmeans, xc2Colmeans)
print ("sBOuter2 =\n", sBOuter2)

sBMatrix = sSize * (sBOuter1 + sBOuter1)
print ("sBMatrix =\n", sBMatrix)

sWInv = np.linalg.inv(a = sWMatrix)
print ("sWInv =\n", sWInv)

sMult = np.dot(a = sWInv, b = sBMatrix)
print ("sMult =\n", sMult)
eigenValues, eigenVectors = np.linalg.eig(a = sMult)
print ("eigenValues =", eigenValues)
print ("eigenVectors =\n", eigenVectors)
eigenValuesSorted = sorted(eigenValues, reverse=True)
print ("eigenValuesSorted =", eigenValuesSorted)

wMatrix = eigenVectors[:, 1]
print ("wMatrix =\n", wMatrix)
xW = x.dot(wMatrix)
print ("xW =\n", xW)


# import matplotlib.pyplot as plt
# tot = sum(eigenValuesSorted)
# discr = [(i / tot) for i in sorted(eigenValuesSorted, reverse=True)]
# cum_discr = np.cumsum(discr)
# plt.bar(range(1, 14), discr, alpha=0.5, align='center',
#     label='individual "discriminability"')
# plt.step(range(1, 14), cum_discr, where='mid',
#     label='cumulative "discriminability"')
# plt.ylabel('"discriminability" ratio')
# plt.xlabel('Linear Discriminants')
# plt.ylim([-0.1, 1.1])
# plt.legend(loc='best')
# plt.show()



















