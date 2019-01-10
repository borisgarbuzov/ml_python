myArray = [1, 2, 3]
myArray2 = [2, 2, 5]

import matplotlib.pyplot as plt

plt.plot(myArray, "ro")
# plt.legend(['dependent', 'independent'], loc='upper left')
plt.hist(myArray)
plt.hist(myArray2)
plt.show()

# hist
# several windows
# summery
