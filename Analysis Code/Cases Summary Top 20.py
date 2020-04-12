import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('seaborn-deep')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
dataFromCsv = pd.read_csv('../Analysis Data/internationalCovid19Status.csv')
print(dataFromCsv)
# print(dataFromCsv['totalConfirmed'])
treatmentCase = dataFromCsv['totalConfirmed'][0:20] - (dataFromCsv['totalDeaths'][0:20] + dataFromCsv['totalRecovered'][0:20])
print(treatmentCase)

ax1.barh(dataFromCsv['id'][0:20],dataFromCsv['totalDeaths'][0:20], label='Number of Death Cases', color='#8B0000', left = treatmentCase+ dataFromCsv['totalRecovered'][0:20])
ax1.barh(dataFromCsv['id'][0:20],dataFromCsv['totalRecovered'][0:20],left = treatmentCase, label='Number of Recovered Cases', color='#1E90FF')
ax1.barh(dataFromCsv['id'][0:20],treatmentCase[0:20], label='Number of Corona Cases', color='#CD5C5C')

##ax1.bar(dataFromCsv['id'][0:20],treatmentCase[0:20], label='Number of Corona Cases', color='#800000')
##ax1.bar(dataFromCsv['id'][0:20],dataFromCsv['totalRecovered'][0:20],bottom = treatmentCase[0:20], label='Number of Recovered Cases', color='c')
##ax1.bar(dataFromCsv['id'][0:20],dataFromCsv['totalDeaths'][0:20], label='Number of Death Cases', color='b')


# ax1.plot(data_file['Date'],data_file['Number of Cases'])
# # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
# # ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
for label in ax1.xaxis.get_ticklabels(): # loop to change the x axis label rotation
    label.set_rotation(90)
# ax1.grid(True)#, color='g', linest
ax1.spines['left'].set_color('c')#Making graph Left line color cyan
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick


plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Cases Summary of Covid-19")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.30, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()

