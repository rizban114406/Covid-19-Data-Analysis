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
print(result.date.iat[-1])
ax1.plot(result.day,result.case, label='Number of Cases', color='#EB0706')
ax1.fill_between(result.day,result.case, facecolor='#EB0706', alpha=0.3)
for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(0)


ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(5) # Left line thick



plt.xlabel(result.date.iat[0]+' '+' to '+' '+result.date.iat[-1])
plt.ylabel('Positive case')
plt.title("Positive cases from day -1")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.43, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()


