def matmult(m, v):
    nrows = len(m)
    w = [None] * nrows
    for row in range(nrows):
        w[row] = reduce(lambda x,y: x+y, map(lambda x,y: x*y, m[row], v))
    return w


a = [4, 5, 6]
b = [1,2,3]
c = [i * j for i, j in zip(a, b)]
print ("c = ", c)
print ("zip(a, b) = ", zip(a, b))
d = [(i, j) for i, j in zip(a, b)]
print ("d = ", d)
myCortege = (1,2)
print ("myCortege = ", myCortege)


#................................................

# m, n = 2, 3
# vec = range(1, n+1)
# mat = [map(lambda x: i*n+x+1, range(n)) for i in range(m)]
# print ('vec=', vec)
# print ('mat=', mat)
# print ('mat . vec=', matmult(mat, vec))


