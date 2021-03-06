import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

print(plt.style.available)
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

file = open('../Analysis Data/wordSummary.txt', 'r')
wordData = file.readline()
wordDataList = wordData.split('-')
print(wordDataList)
file.close()

totalDeath = int(wordDataList[4])
totalRecovered = int(wordDataList[5])
totalCase = int(wordDataList[3]) 

slices = [totalCase,totalDeath,totalRecovered]
activities = ['Positive Cases','Total Death','Total Recovered']
cols = ['#4169E1','#DC143C','#FF7F50']
_,_,autopcts = ax1.pie(slices,
                       labels=activities,
                       colors=cols,
                       pctdistance=.7,
                       startangle=90, #Starting angle point
                       shadow= True,
                       explode=(0.00,0.00,0.1), #Slice out (amount of explotion sleeping, ammount of eating,..)
                ##        autopct='%1.1f%%'
                       autopct=lambda pct: func(pct, slices)) # Adds the percentage
plt.setp(autopcts, **{'color':'white', 'weight':'bold', 'fontsize':10})

plt.title('Case Summary Proportion Today')
plt.show()
