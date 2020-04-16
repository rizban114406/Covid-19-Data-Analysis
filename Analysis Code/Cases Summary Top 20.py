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

treatmentCase = result['totalConfirmed'][-10:] - (result['totalDeaths'][-10:] + result['totalRecovered'][-10:])
print(treatmentCase)

ax1.bar(result['id'][-10:],result['totalDeaths'][-10:], label='Number of Death Cases', color='#8B0000', left = treatmentCase+ result['totalRecovered'][-10:])
ax1.bar(result['id'][-10:],result['totalRecovered'][-10:],left = treatmentCase, label='Number of Recovered Cases', color='#1E90FF')
ax1.bar(result['id'][-10:],treatmentCase[-10:], label='Number of Corona Cases', color='#CD5C5C')
##ax1.bar(result['id'][-10:],treatmentCase[-10:], label='Number of Corona Cases', color='#CD5C5C')
##ax1.bar(result['id'][-10:],result['totalRecovered'][-10:], label='Number of Recovered Cases', color='#1E90FF')
##ax1.bar(result['id'][-10:],result['totalDeaths'][-10:], label='Number of Death Cases', color='#8B0000')

ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(2) # Left line thick

for i in ax1.patches:
    print(i)
    width, height = i.get_width(), i.get_height()
    x, y = i.get_xy()
    ax1.annotate('{:.0%}'.format(height), (x, y + height + 0.01),rotation=85)

plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.title("Cases Summary of Covid-19(Top 20)")
plt.legend()
plt.subplots_adjust(left=0.20, bottom=0.20, right=0.94, top=0.90, wspace=0.6, hspace=0)
plt.show()
