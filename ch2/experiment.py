

a = [4, 5, 6]
b = [1,2,3]
c = [i * j for i, j in zip(a, b)]
print ("c = ", c)
print ("zip(a, b) = ", zip(a, b))
d = [(i, j) for i, j in zip(a, b)]
print ("d = ", d)
myCortege = (1,2)
print ("myCortege = ", myCortege)

a = 10000
b = 10000
print ("a == b", a == b)
print ("a is b", a is b)


bracketedAWithComma = (a,)
print (type(bracketedAWithComma))

class ClassA:

    def __init__ (self, field1):
        self.field1 = field1

    def someMethod(self):
        print ("field 1 without self: ", field1)

field1 = 5
myClassA = ClassA(6)
myClassA.someMethod()







