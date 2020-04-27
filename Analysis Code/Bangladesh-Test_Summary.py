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
##style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
CoronaTestCaseNo = pd.read_csv('../Analysis Data/covid-19-TestResultsBD.csv')
print(CoronaTestCaseNo)

postitiveCases = int(CoronaTestCaseNo['Total'].iloc[3])
negativeCases = int(CoronaTestCaseNo['Total'].iloc[1]) - postitiveCases
slices = [postitiveCases,negativeCases]
activities = ['Covid-19 Positive','Covid-19 Negative']

cols = ['#DC143C','#4169E1']
wedges, texts,autopcts = ax1.pie(slices,
##               labels=activities,
               radius=1,
               labeldistance=1.2,         
               colors=cols,
               pctdistance=.85,
               startangle=90, #Starting angle point
               shadow= True,
               wedgeprops=dict(width=0.3, edgecolor='w'),
               explode=(0,.2), #Slice out (amount of explotion sleeping, ammount of eating,..)
               autopct='%1.1f%%')
##               autopct=lambda pct: func(pct, slices)) # Adds the percentage

plt.setp(autopcts, **{'color':'#FFFFFF', 'weight':'bold', 'fontsize':12})

ax1.legend(activities,loc="best",
           bbox_to_anchor=(0.85, 0.5, 0.5, 0.5),
           prop={'size': 12},)


plt.title('Bangladesh Covid-19 Test Result')
plt.show()
