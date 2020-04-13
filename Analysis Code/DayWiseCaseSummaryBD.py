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
dataFromCsv = pd.read_csv('../Analysis Data/caseBangladesh.csv')
result = dataFromCsv

ax1.bar(result.day,result.case, label='Number of Cases', color='#800000')

for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)


ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(5) # Left line thick

for i in ax1.patches:
    print(i)
    ax1.text(i.get_x(), i.get_height()+5, \
            str(i.get_height()), fontsize=7,
                color='black',rotation=00)

plt.xlabel('Day')
plt.ylabel('Positive case')
plt.title("Positive cases from day -1")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.43, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()


