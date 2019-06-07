rm(list = ls())
x = c(1, 2, 3)
one = c(1, 1, 1)
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

y = c(1, 3, 2)
yHat = pMatrix %*% y
yHat

fit = lm(y~x)
names(fit)
myFittedValues = fitted.values(fit)
myFittedValues

myNormalSample = rnorm(n=100)
myCauchySample = rcauchy(n=100)
qqnorm(myCauchySample)




