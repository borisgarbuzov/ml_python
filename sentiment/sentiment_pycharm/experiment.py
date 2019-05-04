
def myFunction():
    for myIndex in range(15):
        yield myIndex

def myFunction2():
    return range(15)

returnedValue = myFunction()
print ("returnedValue =", returnedValue)

for anotherIndex in returnedValue:
    print("anotherIndex =", anotherIndex)

returnedValue2 = myFunction2()
print ("returnedValue2 =", returnedValue2)

for anotherIndex2 in returnedValue2:
    print("anotherIndex2 =", anotherIndex2)

print("no function, just loop")


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

def multiReturnFun():
    return 1
    return 2
    return 3

print ("multiReturnFun() =", multiReturnFun())

# for value in multiReturnFun():
#     print(value)



