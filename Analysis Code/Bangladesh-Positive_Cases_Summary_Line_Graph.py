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

totalCase = []
totalDeath = []
totalRecovered = []

totalCaseNumber = 0
totalDeathNumber = 0
totalRecoveredNumber = 0

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
for data in dataFromCsv['Case']:
    totalCaseNumber = totalCaseNumber + int(data)
    totalCase.append(totalCaseNumber)
print(totalCase)

ax1.plot(dataFromCsv['Day'],totalCase,'-',linewidth=2, label='Positive Cases',color = '#4169E1')
ax1.fill_between(dataFromCsv['Day'],totalCase, 0, facecolor='#4169E1', alpha=.3)
ax1.bar(dataFromCsv['Day'],totalCase, color='#4169E1',alpha = 0.8)

for i in ax1.patches:
    if (i.get_height() != 0):
        ax1.text(i.get_x(), i.get_height()+50, \
                str(i.get_height()), fontsize=12,
                    color='#4B0082',rotation=85)

xlabel = str(dataFromCsv['Date'].iloc[1]) + ' UPTO ' + str(dataFromCsv['Date'].iloc[-1])
plt.xlabel(xlabel)
plt.ylabel('Number of Cases')
plt.title("Trend Of Bangladesh Covid-19 Cases")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
