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

zStd = z.std(axis=0)
print ("zStd =", zStd)
z0Std = z0.std(axis=0)
print ("z0Std =", z0Std)

zStandard = z0 / z0Std
print ("zStandard =", zStandard)

# transpose and multiply matrix
rowCount = zStandard.shape[1]
print ("rowCount =", rowCount)
varMatrix = z0Std.T * z0Std / rowCount
print ("varMatrix =", varMatrix)








