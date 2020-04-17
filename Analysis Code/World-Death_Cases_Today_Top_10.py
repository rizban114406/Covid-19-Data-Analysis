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
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerCountryCaseSummary.csv')
result = dataFromCsv.sort_values(['totalDeathsEntryday'], ascending= True)
print(dataFromCsv.columns)
ax1.barh(result['id'][-10:],result['totalDeathsEntryday'][-10:], label='Confirmed Death Cases Today', color='#800000')

for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)


ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick
for i in ax1.patches:
    print(i)
    ax1.text(i.get_width()+10, i.get_y()+0.2, \
            str(i.get_width()), fontsize=10,
                color='dimgrey',rotation=0)
plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Confirmed Covid-19 Death Cases Today(Top 10)")
plt.legend()
plt.subplots_adjust(left=0.20, bottom=0.25, right=0.94, top=.85, wspace=0.2, hspace=0)
plt.show()
