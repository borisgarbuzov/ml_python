rm(list = ls())
x = 1:100

one = rep(1, 11)
X = as.matrix(cbind(one, x))
X
XtX = t(X) %*% X
XtXinv = solve(XtX)
# make sure it is inverse indeed
XtXinv %*% XtX

# pseudoinverse
xPlus = XtXinv %*% t(X)
xPlus

# To get hat or projection matrix, we need to multiply xPlus pseudo-inverse by X on the left
pMatrix = X %*% xPlus
pMatrix
X

y = x

yHat = pMatrix %*% y
yHat

fit = lm(y~x)
names(fit)
myFittedValues = fitted.values(fit)
myFittedValues
plot(fit)



myNormalSample = rnorm(n=100)
myCauchySample = rcauchy(n=100)
qqnorm(myCauchySample)

image(pMatrix)

library(lattice)

mySize = 100
x0 = rep(1, times=mySize)
x1 = rnorm(n=mySize)
x2 = rnorm(n=mySize)


x1 = sort(x1)
X = matrix(c(x0, x1), nrow = mySize, ncol = 2)
X
hMatrix = X %*% solve(t(X) %*% X) %*% t(X)
wireframe(hMatrix, drape = T)


Xbig = matrix(c(x0, x1, x2), nrow = mySize, ncol = 3)
Xbig
hMatrixbig = Xbig %*% solve(t(Xbig) %*% Xbig) %*% t(Xbig)
wireframe(hMatrixbig, drape = T)

df = data.frame(y, x0, x1, x2)
cor(df)
