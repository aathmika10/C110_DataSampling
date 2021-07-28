import csv 
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
temp=df["temp"].to_list()

def randomMean(counter):
    dataSet=[]
    for i in range (0,counter):
        randIndex=random.randint(0,len(temp)-1)
        value=temp[randIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanList= []
    for i in range(0,1000):
        set_of_means= randomMean(100)
        meanList.append(set_of_means)
    showFig(meanList)
    mean = statistics.mean(meanList)
    print("Mean of sampling distribution :-",mean )

setup()

population_mean = statistics.mean(temp)
print("population mean:- ", population_mean)


def standard_deviation():
    meanList = []
    for i in range(0,1000):
        set_of_means= randomMean(100)
        meanList.append(set_of_means)
    std_deviation = statistics.stdev(meanList)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()
