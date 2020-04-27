import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('fivethirtyeight')

caseBangladesh = pd.read_csv('../Analysis Data/covid-19-PerDayCaseSummaryBD.csv')
# style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
result = caseBangladesh.sort_values(['Tested'], ascending= True)

ax1.plot(result.Tested,result.Case,linewidth=2, label='Positive Cases', color='#EB2425')
##ax1.bar(result.Tested,result.Case, color='#FF7F50',alpha = .7)
ax1.fill_between(result.Tested,result.Case, facecolor='#407EB0', alpha=0.3)
ax1.xaxis.set_major_locator(mticker.MaxNLocator(15))
# for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
#     label.set_rotation(0)


ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(5) # Left line thick


import datetime
datetimeobject = datetime.datetime.strptime(str(caseBangladesh['Date'].iloc[1]),'%m/%d/%Y')
startDate = datetimeobject.strftime('%d-%b-%Y')
datetimeobject = datetime.datetime.strptime(str(caseBangladesh['Date'].iloc[-1]),'%m/%d/%Y')
endDate = datetimeobject.strftime('%d-%b-%Y')
xlabel = 'Number of Tests\n' + str(startDate) + ' UPTO ' + str(endDate)
plt.xlabel(xlabel)
plt.ylabel('Number of Cases')
plt.title("Tested Vs Positive Cases")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
