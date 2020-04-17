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
style.use('ggplot')
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerDayCaseSummaryBD.csv')

totalCaseNumber = int(dataFromCsv['Case'].iloc[-1])

totalDeathNumber = int(dataFromCsv['Death'].iloc[-1])
    
totalRecoveredNumber = int(dataFromCsv['Recovered'].iloc[-1])

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

slices = [totalCaseNumber,totalDeathNumber,totalRecoveredNumber]
activities = ['Positive Cases','Death','Recovered']

cols = ['#4169E1','#DC143C','#FF7F50']
_,_,autopcts = ax1.pie(slices,
               labels=activities,
               colors=cols,
               pctdistance=.7,
               startangle=-75, #Starting angle point
               shadow= True,
               explode=(0,0.3,0), #Slice out (amount of explotion sleeping, ammount of eating,..)
##               autopct='%1.1f%%')
               autopct=lambda pct: func(pct, slices)) # Adds the percentage
plt.setp(autopcts, **{'color':'#FFFFFF', 'weight':'bold', 'fontsize':10})

plt.title('Bangladesh Case Summary Proportion Today')
plt.show()

