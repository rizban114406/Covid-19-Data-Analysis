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
dataFromCsv = pd.read_csv('../Analysis Data/internationalCovid19Status.csv')
result = dataFromCsv.sort_values(['totalConfirmed'], ascending= True)

ax1.bar(result['id'][0:20],result['totalConfirmed'][0:20], label='Number of Cases', color='#800000')

for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)

ax1.set_yticks([0,2,4,6,8,10,12,14,16])
ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick

for i in ax1.patches:
    print(i)
    ax1.text(i.get_x()+0.2, i.get_height()+.5, \
            str(i.get_height()), fontsize=10,
                color='dimgrey',rotation=0)

plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Number of Confirmed Covid-19 Cases(Bottom 20)")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.43, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()

