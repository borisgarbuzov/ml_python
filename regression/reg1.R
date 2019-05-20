rm(list = ls())
# setwd("G:/mine/my_text/toronto_u/research/zhou/r/ml/ml_python/regression")
#setwd("~/ml_python/regression")
df = read.csv("data1.csv", header = T)
df
xyLm = lm(y~x, data = df)
xyLm
plot(df)
names(xyLm)
myResiduals = residuals(xyLm)
sum(myResiduals)
coef(xyLm)
effects(xyLm)
#rank(xyLm)
myFittedValues = fitted.values(xyLm)
xyLm$xlevels


# myXLevels = xlevels(xyLm)
# myXLevels
# rise = myFittedValues[2] - myFittedValues[1]
# rise
# run = myXLevels[2] - myXLevels[1]
# run
# slope = rise / run
# slope
# coefficients(xyLm)

myX = c(1, 2, 3)
xBar = mean(myX)
xBar
xCentered = myX - xBar
xCentered
sum(xCentered)

xyLm
newX = data.frame(x = 5)
predict(xyLm, newX)



## Predictions
x <- rnorm(15)
y <- x + rnorm(15)
plot(x, y)
valery = lm(y ~ x)
valery
yHats = predict(valery)
plot(x, yHats)
myResiduals = residuals(valery)
newX = data.frame(x=5.5)
predict(valery, newdata = newX)

new <- data.frame(x = seq(-3, 3, 0.5))
predict(lm(y ~ x), new)