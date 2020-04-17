import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('fivethirtyeight')
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerDayCaseSummaryBD.csv')
print(dataFromCsv.columns)

totalDeath = []
totalDeathNumber = 0

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

for data in dataFromCsv['Death']:
    totalDeathNumber = totalDeathNumber + int(data)
    totalDeath.append(totalDeathNumber)
##print(totalDeath)

ax1.plot(dataFromCsv['Day'],totalDeath,'-',linewidth=2, label='Death Cases',color = '#DC143C' )
ax1.fill_between(dataFromCsv['Day'],totalDeath, 0, facecolor='#DC143C', alpha=.3)
ax1.bar(dataFromCsv['Day'],totalDeath, color='#DC143C',alpha = 0)

for i in ax1.patches:
    ax1.text(i.get_x(), i.get_height()+2, \
             str(i.get_height()), fontsize=12,
             color='#4B0082',rotation=85)

xlabel = str(dataFromCsv['Date'].iloc[1]) + ' UPTO ' + str(dataFromCsv['Date'].iloc[-1])
plt.xlabel(xlabel)
plt.ylabel('Number of Cases')
plt.title("Trend Of Bangladesh Covid-19 Death Cases")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
