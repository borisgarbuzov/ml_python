rm(list = ls())
setwd("G:/mine/my_text/toronto_u/research/zhou/r/ml/ml_python/regression")
df = read.csv("data1.csv")
df
xyLm = lm(df)
xyLm
plot(df)
