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

positiveRatio = round((dataFromCsv['Case'] / dataFromCsv['Tested'])*100,2)
print(positiveRatio)

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

##ax1.plot(dataFromCsv['Day'],positiveRatio,'-',linewidth=2, label='Positive Cases Ratio',color = '#4169E1')
##ax1.fill_between(dataFromCsv['Day'],positiveRatio, 0, facecolor='#4169E1', alpha=.3)
ax1.bar(dataFromCsv['Day'],positiveRatio,label='Positive Cases Ratio', color='#4169E1',alpha = .7)

for i in ax1.patches:
    showData = str(i.get_height()) + "%"
    ax1.text(i.get_x()+.1, i.get_height()+1, \
             showData, fontsize=12,
             color='#4B0082',rotation=75)

import datetime
datetimeobject = datetime.datetime.strptime(str(dataFromCsv['Date'].iloc[1]),'%m/%d/%Y')
startDate = datetimeobject.strftime('%d-%b-%Y')
datetimeobject = datetime.datetime.strptime(str(dataFromCsv['Date'].iloc[-1]),'%m/%d/%Y')
endDate = datetimeobject.strftime('%d-%b-%Y')

xlabel = "Number of Days\n" + str(startDate) + ' UPTO ' + str(endDate)
plt.xlabel(xlabel)
plt.ylabel('Number of Cases')
plt.title("Per Day Covid-19 Test Positive Ratio")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
