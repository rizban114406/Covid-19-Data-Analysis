import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:d}".format(absolute)

print(plt.style.available)
##style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
CoronaTestCaseNo = pd.read_csv('../Analysis Data/covid-19-TestResultsBD.csv')
print(CoronaTestCaseNo)

postitiveCases = int(CoronaTestCaseNo['Total'].iloc[3])
testCases = int(CoronaTestCaseNo['Total'].iloc[1])
slices = [postitiveCases,testCases]
activities = ['Covid-19 Positive','Total Tested']

cols = ['#DC143C','#4169E1']
wedges, texts,autopcts = ax1.pie(slices,
##               labels=activities,
               colors=cols,
               pctdistance=.7,
               startangle=-75, #Starting angle point
               shadow= True,
               explode=(0,.2), #Slice out (amount of explotion sleeping, ammount of eating,..)
##               autopct='%1.1f%%')
               autopct=lambda pct: func(pct, slices)) # Adds the percentage

plt.setp(autopcts, **{'color':'#FFFFFF', 'weight':'bold', 'fontsize':12})

ax1.legend(activities,loc="best",
           bbox_to_anchor=(0.85, 0.5, 0.5, 0.5),
           prop={'size': 12},)


plt.title('Bangladesh Tested vs Positive Case')
plt.show()
