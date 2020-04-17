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

totalRecovered = []
totalRecoveredNumber = 0

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

for data in dataFromCsv['Recovered']:
    totalRecoveredNumber = totalRecoveredNumber + int(data)
    totalRecovered.append(totalRecoveredNumber)
print(totalRecovered)

ax1.plot(dataFromCsv['Day'],totalRecovered,'-',linewidth=2, label='Recovered Cases',color = '#FF7F50' )
ax1.fill_between(dataFromCsv['Day'],totalRecovered, 0, facecolor='#FF7F50', alpha=.3)
ax1.bar(dataFromCsv['Day'],totalRecovered, color='#FF7F50',alpha = 0)


for i in ax1.patches:
    ax1.text(i.get_x(), i.get_height()+2, \
             str(i.get_height()), fontsize=12,
             color='#4B0082',rotation=85)

##
##bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
##ax1.annotate(str(totalRecovered[-1]), (int(dataFromCsv['Day'].iloc[-1]), int(totalRecovered[-1])),
##            bbox=bbox_props, color = '#FF7F50')

xlabel = str(dataFromCsv['Date'].iloc[1]) + ' UPTO ' + str(dataFromCsv['Date'].iloc[-1])
plt.xlabel(xlabel)
plt.ylabel('Number of Cases')
plt.title("Trend Of Bangladesh Covid-19 Recovered Cases")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
