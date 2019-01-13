myArray = [2, 1, 3, 5]
import numpy as np
npArray = np.array(myArray)
argsorted = np.argsort(npArray)
print ("argsorted =", argsorted)
inverseSorted = argsorted[::-1]
print ("inverseSorted =", inverseSorted)
invertedMyArray = myArray [::-1]
print ("invertedMyArray =", invertedMyArray)



