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
xPlus = solve(t(X)) %*% t(X)

pMatrix = X %*% xPlus
pMatrix


