import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

dataFromCsv = pd.read_csv('../Analysis Data/internationalCovid19Status.csv')
numberOfAffectedCountries = dataFromCsv['id'].nunique()
numberOfCountriesNoDeathsToday = 0
for values in dataFromCsv['totalDeathsEntryday']:
    if values == 0:
        numberOfCountriesNoDeathsToday = numberOfCountriesNoDeathsToday + 1
print("Number of Countries No Death Case Today: {}".format(numberOfCountriesNoDeathsToday))

print(plt.style.available)
##style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

slices = [numberOfAffectedCountries,numberOfCountriesNoDeathsToday]
activities = ['Death Cases','No Death Cases']
cols = ['#CD5C5C','#8B0000']
ax1.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90, #Starting angle point
        shadow= True,
        explode=(0.05,0.05), #Slice out (amount of explotion sleeping, ammount of eating,..)
        autopct='%1.1f%%')
##        autopct=lambda pct: func(pct, slices)) # Adds the percentage

for i in ax1.patches:
    print(i)

plt.title('Countries Death Cases Faced Today')
plt.show()

