import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style

print(plt.style.available)
##style.use('seaborn-deep')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerCountryCaseSummary.csv')
result = dataFromCsv.sort_values(['totalConfirmed'], ascending= True)
##print(dataFromCsv.columns)
treatmentCase = result['totalConfirmed'][0:10] - (result['totalDeaths'][0:10] + result['totalRecovered'][0:10])
print(treatmentCase)

##ax1.barh(result['id'][0:10],result['totalDeaths'][0:10], label='Number of Death Cases', color='#8B0000', left = treatmentCase+ result['totalRecovered'][0:10])
##ax1.barh(result['id'][0:10],result['totalRecovered'][0:10],left = treatmentCase, label='Number of Recovered Cases', color='#1E90FF')
##ax1.barh(result['id'][0:10],treatmentCase[0:10], label='Number of Corona Cases', color='#CD5C5C')
##ax1.set_xticks([0,2,4,6,8,10,12,14,16])

X = np.arange(1,len(treatmentCase)+1)
ax1.bar(X + 0.00,treatmentCase, label='Under Treatment Cases', color='#800000',width = 0.30)
ax1.bar(X + 0.30,result['totalDeaths'][0:10], label='Death Cases', color='#1E90FF',width = 0.30)
ax1.bar(X - 0.30,result['totalRecovered'][0:10], label='Recovered Cases', color='#CD5C5C',width = 0.30)

ax1.set_yticks([i for i in range(0,int(result['totalConfirmed'][0:10].iloc[-1])+3)])
##ax1.yaxis.set_major_locator(mticker.MaxNLocator(10))
country = result['id'][0:10].tolist()

ax1.spines['right'].set_visible(False)# No right line
ax1.spines['top'].set_visible(False)# No top line
ax1.spines['left'].set_linewidth(3) # Left line thick

for i in ax1.patches:
    print(i)
    if (i.get_height() != 0):
        ax1.text(i.get_x(), i.get_height()+.2, \
                str(i.get_height()), fontsize=10,
                    color='dimgrey',rotation=85)
    
plt.xlabel('Country')
plt.xticks(X,country,rotation = 45)
plt.ylabel('Number of Cases')
plt.title("Cases Summary of Covid-19(Bottom 10)")
plt.legend()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.94, top=0.90, wspace=0.4, hspace=0)
plt.show()
##fig.savefig('caseSummaryBottom20.png') # Saving the Graph in figure color



