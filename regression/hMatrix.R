rm(list = ls())
x = c(1, 2, 3)
one = c(1, 1, 1)
X = as.matrix(cbind(one, x))
X
XtX = t(X) %*% X
XtXinv = solve(XtX)
XtXinv %*% XtX
X %*% solve(t(X) %*% X) 
