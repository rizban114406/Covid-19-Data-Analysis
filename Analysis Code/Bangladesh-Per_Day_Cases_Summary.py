import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('ggplot')
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerDayCaseSummaryBD.csv')

fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
plt.title("Bangladesh Per Day Cases")
plt.ylabel('Death')

ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax1) # sharex = ax1 meaning its sharing X axis with ax1
plt.ylabel('Positive Cases')

ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
plt.ylabel('Recovered')

ax1.plot(dataFromCsv['Date'],dataFromCsv['Death'],'-',linewidth=2, label='Confirmed Death Cases',color = '#DC143C' )
##ax1.fill_between(dataFromCsv['Date'], dataFromCsv['Death'], 0, facecolor='#DC143C', alpha=1)
ax1.bar(dataFromCsv['Date'],dataFromCsv['Death'], label='Number of Cases', color='#DC143C',alpha = 0.5)


ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='lower'))

ax2.plot(dataFromCsv['Date'],dataFromCsv['Case'],'-',linewidth=2, label='Confirmed Cases',color = '#4169E1')
ax2.bar(dataFromCsv['Date'],dataFromCsv['Case'], label='Number of Death Cases', color='#4169E1',alpha = 0.5)


ax3.plot(dataFromCsv['Date'],dataFromCsv['Recovered'],'-',linewidth=2, label='Confirmed Recovered Cases',color = '#FF7F50' )
ax3.bar(dataFromCsv['Date'],dataFromCsv['Recovered'], label='Number of Cases', color='#FF7F50',alpha = 0.5)
ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='lower'))

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)

for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
for i in ax1.patches:
    if (i.get_height() != 0):
        ax1.text(i.get_x(), i.get_height()+2, \
                str(i.get_height()), fontsize=12,
                    color='#4B0082',rotation=85)

for i in ax2.patches:
    if (i.get_height() != 0):
        ax2.text(i.get_x(), i.get_height()+8, \
                str(i.get_height()), fontsize=12,
                    color='#4B0082',rotation=85)

for i in ax3.patches:
    if (i.get_height() != 0):
        ax3.text(i.get_x(), i.get_height()+1, \
                str(i.get_height()), fontsize=12,
                    color='#4B0082',rotation=85)

plt.show()
