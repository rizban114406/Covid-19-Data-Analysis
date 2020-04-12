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

ax1.bar(result['id'][-20:],result['totalConfirmed'][-20:], label='Number of Cases', color='#800000')

for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)


ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick

plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Number of Confirmed Covid-19 Cases(Top 20)")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.30, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
