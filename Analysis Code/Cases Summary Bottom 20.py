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
result = dataFromCsv.sort_values(['totalConfirmed'], ascending= True)

treatmentCase = result['totalConfirmed'][0:20] - (result['totalDeaths'][0:20] + result['totalRecovered'][0:20])
print(treatmentCase)

ax1.barh(result['id'][0:20],result['totalDeaths'][0:20], label='Number of Death Cases', color='#8B0000', left = treatmentCase+ result['totalRecovered'][0:20])
ax1.barh(result['id'][0:20],result['totalRecovered'][0:20],left = treatmentCase, label='Number of Recovered Cases', color='#1E90FF')
ax1.barh(result['id'][0:20],treatmentCase[0:20], label='Number of Corona Cases', color='#CD5C5C')
ax1.set_xticks([0,2,4,6,8,10,12,14,16])
ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick

plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Cases Summary of Covid-19(Bottom 20)")
plt.legend()
plt.subplots_adjust(left=0.35, bottom=0.15, right=0.94, top=0.90, wspace=0.4, hspace=0)
plt.show()
##fig.savefig('caseSummaryBottom20.png') # Saving the Graph in figure color



