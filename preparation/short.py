myArray = [1, 2, 3]
myArray2 = [2, 2, 5]

import matplotlib.pyplot as plt

plt.plot(myArray, "ro")
# plt.legend(['dependent', 'independent'], loc='upper left')
plt.hist(myArray)
plt.hist(myArray2)
plt.show()

# several windows
# summery
from scipy import stats
mySample = [1, 2, 2, 0]
import numpy as np
npSample = np.array (mySample)
print("npSample = ", npSample)
myDescription = stats.describe(npSample)
print("myDescription = ", myDescription)

my2dSample = \
[[1, 2, 2, 0],
[10, 20, 20, 0]]
np2dSample = np.array (my2dSample)
print("np2dSample = ", np2dSample)
my2dDescription = stats.describe(np2dSample)
print("my2dDescription = ", my2dDescription)

my3dSample = \
[[[1, 2, 2, 0],
[10, 20, 20, 0]],
[[21, 22, 22, 20],
[210,220, 220, 20]]]
np3dSample = np.array (my3dSample)
print("np3dSample = ", np3dSample)
my3dDescription = stats.describe(np3dSample)
print("my3dDescription = ", my3dDescription)









