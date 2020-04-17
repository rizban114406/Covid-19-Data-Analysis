import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('ggplot')
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerDayCaseSummaryBD.csv')

totalCase = []
totalCaseNumber = 0
for data in dataFromCsv['Case']:
    totalCaseNumber = totalCaseNumber + int(data)
    totalCase.append(totalCaseNumber)

totalDeath = []
totalDeathNumber = 0
for data in dataFromCsv['Death']:
    totalDeathNumber = totalDeathNumber + int(data)
    totalDeath.append(totalDeathNumber)

totalRecovered = []
totalRecoveredNumber = 0
for data in dataFromCsv['Recovered']:
    totalRecoveredNumber = totalRecoveredNumber + int(data)
    totalRecovered.append(totalRecoveredNumber)
print(totalRecovered)

totalPatient = []
for i in range(0,len(totalCase)):   
    totalPatient.append(totalCase[i] - (totalDeath[i] + totalRecovered[i]))


fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
plt.title("Bangladesh Cases Summary Trend")
plt.ylabel('Death')

ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax1) # sharex = ax1 meaning its sharing X axis with ax1
plt.ylabel('Patients')

ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
plt.ylabel('Recovered')

ax1.plot(dataFromCsv['Day'],totalDeath,'-',linewidth=2, label='Deaths',color = '#DC143C' )
ax1.fill_between(dataFromCsv['Day'], totalDeath, 0, facecolor='#DC143C', alpha=.5)
ax1.bar(dataFromCsv['Day'],totalDeath, color='#DC143C',alpha = 0)


ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='lower'))

ax2.plot(dataFromCsv['Day'],totalPatient,'-',linewidth=2, label='Patients',color = '#4169E1')
ax2.bar(dataFromCsv['Day'],totalPatient, color='#4169E1',alpha = 0)
ax2.fill_between(dataFromCsv['Day'], totalPatient, 0, facecolor='#4169E1', alpha=.5)


ax3.plot(dataFromCsv['Day'],totalRecovered,'-',linewidth=2, label='Recovered',color = '#FF7F50' )
ax3.bar(dataFromCsv['Day'],totalRecovered, color='#FF7F50',alpha = 0)
ax3.fill_between(dataFromCsv['Day'], totalRecovered, 0, facecolor='#FF7F50', alpha=.5)
ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='lower'))

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)

bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
ax1.annotate(str(totalDeath[-1]), (dataFromCsv['Day'].iloc[-1]+.25, totalDeath[-1]),
            bbox=bbox_props, fontsize=12, color='#DC143C')
ax2.annotate(str(totalPatient[-1]), (dataFromCsv['Day'].iloc[-1]+.25, totalPatient[-1]),
            bbox=bbox_props, fontsize=12, color='#4169E1')
ax3.annotate(str(totalRecovered[-1]), (dataFromCsv['Day'].iloc[-1]+.25, totalRecovered[-1]),
            bbox=bbox_props, fontsize=12, color='#FF7F50')

for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
for i in ax1.patches:
    ax1.text(i.get_x(), i.get_height()+5, \
             str(i.get_height()), fontsize=12,
             color='#4B0082',rotation=85)

for i in ax2.patches:
    ax2.text(i.get_x(), i.get_height()+40, \
             str(i.get_height()), fontsize=12,
             color='#4B0082',rotation=85)

for i in ax3.patches:
    ax3.text(i.get_x(), i.get_height()+5, \
             str(i.get_height()), fontsize=12,
             color='#4B0082',rotation=85)

plt.show()
