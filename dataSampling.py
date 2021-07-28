import csv 
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
temp=df["temp"].to_list()

mean= statistics.mean(temp)
median=statistics.median(temp)
stdDev=statistics.stdev(temp)
mode=statistics.mode(temp)

#fig=ff.create_distplot([temp],["temp"],show_hist=False)
#fig.show()

print(mean,stdDev)

dataSet= []
for i in range (0,100):
    randIndex=random.randint(0,len(temp))
    value=temp[randIndex]
    dataSet.append(value)

sampleMean=statistics.mean(dataSet)
sampleStdDev=statistics.stdev(dataSet)

print(sampleMean,sampleStdDev)

