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
dataFromCsv = pd.read_csv('../Analysis Data/covid_19_data.csv')
##result = dataFromCsv.sort_values(['totalConfirmed'], ascending= True)
print(dataFromCsv.columns)
caseHistory = dataFromCsv.groupby(by = 'ObservationDate',as_index=False).agg({'Confirmed' : pd.Series.sum})
deathHistory = dataFromCsv.groupby(by = 'ObservationDate',as_index=False).agg({'Deaths' : pd.Series.sum})
recoveredHistory = dataFromCsv.groupby(by = 'ObservationDate',as_index=False).agg({'Recovered' : pd.Series.sum})

##print(deathHistory)
##print(recoveredHistory)

ax1.plot(caseHistory['ObservationDate'],caseHistory['Confirmed'],'-',linewidth=3, label='Number of Confirmed Cases',color = '#0000CD' )
##bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
####lastValue = caseHistory['Confirmed'].tail(1)
##print(caseHistory['ObservationDate'].tail(1)+4)
##
##
##
##
##
##
##
##
##
##
##
##
##ax1.annotate(caseHistory['Confirmed'].tail(1), (caseHistory['ObservationDate'].tail(1), caseHistory['Confirmed'].tail(1)),
##            xytext = (caseHistory['ObservationDate'].tail(1)+4, caseHistory['Confirmed'].tail(1)), bbox=bbox_props)

ax1.plot(deathHistory['ObservationDate'],deathHistory['Deaths'],'-',linewidth=3, label='Number of Death Cases', color = '#FF0000')
ax1.plot(recoveredHistory['ObservationDate'],recoveredHistory['Recovered'],'-',linewidth=3, label='Number of Recovered Cases', color = '#008000')

ax1.fill_between(caseHistory['ObservationDate'], caseHistory['Confirmed'], caseHistory['Confirmed'][0], facecolor='#0000CD', alpha=0.3)
ax1.fill_between(deathHistory['ObservationDate'], deathHistory['Deaths'], deathHistory['Deaths'][0], facecolor='#FF0000', alpha=0.3)
ax1.fill_between(recoveredHistory['ObservationDate'], recoveredHistory['Recovered'], recoveredHistory['Recovered'][0], facecolor='#008000', alpha=0.3)

for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)

ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick
##for i in ax1.patches:
##    print(i)
##    ax1.text(i.get_x()+0.2, i.get_height()+10000, \
##            str(i.get_height()), fontsize=10,
##                color='dimgrey',rotation=85)
plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Trend Of Covid-19 Cases")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
