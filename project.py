import csv
import statistics
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("project.csv")
read_data=df["reading_time"].to_list()

population_mean = statistics.mean(read_data)

def random_set_of_values():
    data=[]
    for i in range(0,30):
        random_index = random.randint(0,len(read_data)-1)
        value = read_data[random_index]
        data.append(value)
    mean=statistics.mean(data)
    return mean

means=[]

for i in range(1,100):
    var = random_set_of_values()
    means.append(var)

samplemean = statistics.mean(means)
#print(population_mean)
#print(samplemean)

fig = ff.create_distplot([read_data], ["Reading Time"], show_hist=False)
fig.show()

std = statistics.stdev(read_data)
z_score = (population_mean-samplemean)/std
print("Standard Deviation: ")
print("Z-Score: " +str(z_score))

fstdst, fstded, sstdst, sstded, tstdst, tstded = population_mean-std, population_mean+std, population_mean-2*std, population_mean+2*std, population_mean-3*std, population_mean+3*std

f = [i for i in read_data if i>fstdst and i < fstded]
s = [i for i in read_data if i>sstdst and i < sstded]
t = [i for i in read_data if i>tstdst and i < tstded]

pf = len(f)*100/len(data)
ps = len(s)*100/len(data)
pt = len(t)*100/len(data)
