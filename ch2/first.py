# module is a file here
import Perceptron

print("\n Define the input parameters \n")
myEpochCount = 5
xMatrix = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
yVector = [0, 1, 1, 1]
learningSpeed = 1/2
myPerceptron = Perceptron.Perceptron(epochCount = myEpochCount,
                          learningSpeed = learningSpeed)

myPerceptron.fit(xMatrix = xMatrix,
                 yVector = yVector
                 )
print("predict([1, 1, 1]) = ", myPerceptron.predict([1, 1, 1]))
print("predict([1, 0, 0]) = ", myPerceptron.predict([1, 0, 0]))

