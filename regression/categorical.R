y = c(2, 1, 0, 9, 2)
x1 = c(1, 2, 3, 4, 5)
x2 = c("christian", "muslim", "muslim", "atheist", "christian")
x2c = c(1, 0, 0, 0, 1)
x2m = c(0, 1, 1, 0, 0)
x2a = c(0, 0, 0, 1, 0)
x2c + x2m + x2a
myFit = lm (y ~ x1 + x2a + x2m + x2c)
summary(myFit)

# xDf = data.frame(x2a, x2m, x2c)
# xDf
# myFitOfDf = lm(y ~ xDf)
# summary(myFitOfDf)

