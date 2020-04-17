import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
# style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-InternationCaseSummary.csv')
##result = dataFromCsv.sort_values(['totalConfirmed'], ascending= True)
print(dataFromCsv.columns)
##caseHistory = dataFromCsv.groupby(by = 'ObservationDate',as_index=False).agg({'Confirmed' : pd.Series.sum})
##deathHistory = dataFromCsv.groupby(by = 'ObservationDate',as_index=False).agg({'Deaths' : pd.Series.sum})
##recoveredHistory = dataFromCsv.groupby(by = 'ObservationDate',as_index=False).agg({'Recovered' : pd.Series.sum})

##print(deathHistory)
##print(caseHistory['ObservationDate'])

ax1.plot_date(dataFromCsv['ObservationDate'],dataFromCsv['Confirmed'],'-',linewidth=2, label='Number of Confirmed Cases',color = '#0000FF' )
bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
ax1.annotate(str(dataFromCsv['Confirmed'].iloc[-1]), (dataFromCsv['ObservationDate'].iloc[-1], dataFromCsv['Confirmed'].iloc[-1]),
            bbox=bbox_props)
ax1.annotate(str(dataFromCsv['Deaths'].iloc[-1]), (dataFromCsv['ObservationDate'].iloc[-1], dataFromCsv['Deaths'].iloc[-1]),
            bbox=bbox_props)
ax1.annotate(str(dataFromCsv['Recovered'].iloc[-1]), (dataFromCsv['ObservationDate'].iloc[-1], dataFromCsv['Recovered'].iloc[-1]),
            bbox=bbox_props)

##xytext = (int(caseHistory['ObservationDate'].iloc[-1]+4), int(caseHistory['Confirmed'].iloc[-1]))
 #making the ticklabels of ax3 to date 
##ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(15))

ax1.plot(dataFromCsv['ObservationDate'],dataFromCsv['Deaths'],'-',linewidth=2, label='Number of Death Cases', color = '#FF0000')
ax1.plot(dataFromCsv['ObservationDate'],dataFromCsv['Recovered'],'-',linewidth=2, label='Number of Recovered Cases', color = '#008000')

ax1.fill_between(dataFromCsv['ObservationDate'], dataFromCsv['Confirmed'], dataFromCsv['Confirmed'][0], facecolor='#0000FF', alpha=0.3)
ax1.fill_between(dataFromCsv['ObservationDate'], dataFromCsv['Deaths'], dataFromCsv['Deaths'][0], facecolor='#FF0000', alpha=0.3)
ax1.fill_between(dataFromCsv['ObservationDate'], dataFromCsv['Recovered'], dataFromCsv['Recovered'][0], facecolor='#008000', alpha=0.3)

for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(45)

ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(2) # Left line thick

xlabel = str(dataFromCsv['ObservationDate'].iloc[1]) + ' UPTO ' + str(dataFromCsv['ObservationDate'].iloc[-1])
plt.xlabel(xlabel)
plt.ylabel('Number of Cases')
plt.title("Trend Of Covid-19 Cases")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
