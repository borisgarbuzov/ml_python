rm(list = ls())
# setwd("G:/mine/my_text/toronto_u/research/zhou/r/ml/ml_python/regression")
setwd("~/ml_python/regression")
df = read.csv("data1.csv", header = T)
df
xyLm = lm(y~x, data = df)
xyLm
plot(df)
plot(xyLm)


names(xyLm)
myResiduals = residuals(xyLm)
sum(myResiduals)
coef(xyLm)
effects(xyLm)
#rank(xyLm)
myFittedValues = fitted.values(xyLm)
xyLm$xlevels
summary(xyLm)

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


2*(1-pnorm (q=1.11))
(0.5-0.36650)*2


y = c(1, 2, 3, 4, 5, 6, 7, 8)
x = c(1, 1, 2, 2, 3, 3, 4, 4)
fitObject = lm (y~x)
anova(fitObject)

factorX = as.factor(x)
fitFactorObject = lm (y~factorX)
anova(fitFactorObject)

y = c(1, 2, 3, 4, 5, 6, 7, 8)
x = c(0, 0, 0, 0, 1, 1, 1, 1)
xyLm = lm(y~x, data = df)
xyLm
plot(y~x)
plot(xyLm)
boxplot(y~x)

rm(list = ls())
n = 200
sigma = 30
e = rnorm(n=n, mean=0, sd = sigma)
e
plot(e)
x = 1:n
b0 = 7
b1 = -2
yHat = b0 + b1*x 
yHat
plot(yHat)
y = yHat + e
y
plot(y)


fit = lm(y~x)
fit
# plot(fit)
myResiduals = residuals(fit)
myResiduals
plot(myResiduals, col = "blue")
plot(e, col = "red")
e
plot(e~myResiduals)
plot(y~x)
abline(lm(y ~ x))
summary(fit)
summary(y)
mean(x)
