import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
# style.use('fivethirtyeight')

caseBangladesh = pd.read_csv('../Analysis Data/bdPerDayCase.csv')
# style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
result = caseBangladesh.sort_values(['tested'], ascending= True)

ax1.plot(result.tested,result.Case, label='Positive Cases', color='#EB2425')

ax1.fill_between(result.tested,result.Case, facecolor='#407EB0', alpha=0.3)

# for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
#     label.set_rotation(0)


ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(5) # Left line thick



plt.xlabel('Test Conducted')
plt.ylabel('Positive Cases')
plt.title("Positive vs Test Conducted")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.43, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
