rm(list = ls())
# setwd("G:/mine/my_text/toronto_u/research/zhou/r/ml/ml_python/regression")
setwd("~/ml_python/regression")
df = read.csv("data1.csv")
df
xyLm = lm(df)
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





