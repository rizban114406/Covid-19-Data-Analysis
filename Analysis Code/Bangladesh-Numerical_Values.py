
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style

print(plt.style.available)
style.use('fivethirtyeight')
dataFromCsv = pd.read_csv('../Analysis Data/covid-19-PerDayCaseSummaryBD.csv')
print(dataFromCsv.columns)

totalCases = dataFromCsv['Case'].sum()
print("Corona Positive Cases: {}".format(totalCases))

totalDeath = dataFromCsv['Death'].sum()
print("Corona Death Cases: {}".format(totalDeath))

totalRecovered = dataFromCsv['Recovered'].sum()
print("Corona Recovered Cases: {}".format(totalRecovered))

totalTest = dataFromCsv['Tested'].sum()
print("Corona Tested Total: {}".format(totalTest))

deathRate = round((totalDeath / totalCases) * 100,3)
print("Corona Death Rate(%): {}".format(deathRate))

recoverdRate = round((totalRecovered / totalCases) * 100,3)
print("Corona Recovered Rate(%): {}".format(recoverdRate))

positiveRate = round((totalCases / totalTest) * 100,3)
print("Corona Positive Rate(%): {}".format(positiveRate))



totalCasesToday = dataFromCsv['Case'].iloc[-1]
print("Corona Positive Cases 24 Hours: {}".format(totalCasesToday))

totalDeathToday = dataFromCsv['Death'].iloc[-1]
print("Corona Death Cases 24 Hours: {}".format(totalDeathToday))

totalRecoveredToday = dataFromCsv['Recovered'].iloc[-1]
print("Corona Recovered Cases 24 Hours: {}".format(totalRecoveredToday))

totalTestedToday = dataFromCsv['Tested'].iloc[-1]
print("Corona Tested 24 Hours: {}".format(totalTestedToday))

positiveRateToday = round((totalCasesToday / totalTestedToday) * 100,3)
print("Corona Positive Rate(%) 24 Hours: {}".format(positiveRateToday))





