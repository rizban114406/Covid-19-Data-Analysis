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
# print(dataFromCsv['id'])
# print(dataFromCsv['totalConfirmed'])

ax1.bar(dataFromCsv['id'][-20:],dataFromCsv['totalConfirmed'][-20:], label='Number of Cases', color='#800000')

# ax1.plot(data_file['Date'],data_file['Number of Cases'])
# # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
# # ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)
# ax1.grid(True)#, color='g', linest
ax1.set_yticks([0,2,4,6,8,10,12,14,16])
ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick


plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Number of Confirmed Covid-19 Cases(Bottom 20)")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.43, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()

