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
print(dataFromCsv.columns)

totalDeath = dataFromCsv['totalDeaths'].sum()
totalRecovered = dataFromCsv['totalRecovered'].sum()
totalUnderTreatment = dataFromCsv['totalConfirmed'].sum() - (totalDeath + totalRecovered) 

slices = [totalUnderTreatment,totalDeath,totalRecovered]
activities = ['Total Under Treatment','Total Death','Total Recovered']
cols = ['#CD5C5C','#8B0000','#1E90FF']
ax1.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90, #Starting angle point
        shadow= True,
        explode=(0.1,0.1,.1), #Slice out (amount of explotion sleeping, ammount of eating,..)
        autopct='%1.1f%%') # Adds the percentage

plt.title('Case Summary Proportion')
plt.show()
