
def myFunction():
    for myIndex in [0, 1, 2, 3]:
        yield myIndex


returnedValue = myFunction()
print ("returnedValue =", returnedValue)