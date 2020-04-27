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

iedrcCases = int(CoronaTestCaseNo['Lab'].iloc[0])
otherCases = int(CoronaTestCaseNo['OLab'].iloc[0])
slices = [iedrcCases,otherCases]
activities = ['In IEDCR','In Other Labs']

cols = ['#FF6347','#000080']
wedges, texts,autopcts = ax1.pie(slices,
##               labels=activities,
               colors=cols,
               pctdistance=.7,
               startangle=-75, #Starting angle point
               shadow= True,
               explode=(0,.2), #Slice out (amount of explotion sleeping, ammount of eating,..)
               autopct='%1.1f%%')
##               autopct=lambda pct: func(pct, slices)) # Adds the percentage

plt.setp(autopcts, **{'color':'#FFFFFF', 'weight':'bold', 'fontsize':12})

ax1.legend(activities,loc="best",
           bbox_to_anchor=(0.85, 0.5, 0.5, 0.5),
           prop={'size': 12},)


plt.title('Tests Conducted In')
plt.show()
