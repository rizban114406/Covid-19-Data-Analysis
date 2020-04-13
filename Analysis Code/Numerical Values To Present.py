import pandas as pd
import numpy as np

dataFromCsv = pd.read_csv('../Analysis Data/internationalCovid19Status.csv')
result = dataFromCsv.sort_values(['totalConfirmedEntryday'], ascending= True)
print(dataFromCsv.columns)

file = open('../Analysis Data/wordSummary.txt', 'r')
wordData = file.readline()
wordDataList = wordData.split('-')
file.close()

totalAffectedNumber = wordDataList[0]
print("Number of Total Infected World: {}".format(totalAffectedNumber))


totalDeathNumber = wordDataList[1]
print("Number of Total Death World: {}".format(totalDeathNumber))


totalRecoveredNumber = wordDataList[2]
print("Number of Total Recovered World: {}".format(totalRecoveredNumber))


totalAffectedNumberToday = wordDataList[5]
print("Number of Total Infected World Today: {}".format(totalAffectedNumberToday))


totalDeathNumberToday = wordDataList[4]
print("Number of Total Death World Today: {}".format(totalDeathNumberToday))


totalRecoveredNumberToday = wordDataList[3]
print("Number of Total Recovered World Today: {}".format(totalRecoveredNumberToday))


##numberOfAffectedCountries = wordDataList[0]
##print("Number of Affected Countries: {}".format(numberOfAffectedCountries))


numberOfCountriesNoCasesToday = 0
for values in dataFromCsv['totalConfirmedEntryday']:
    if values == 0:
        numberOfCountriesNoCasesToday = numberOfCountriesNoCasesToday + 1
print("Number of Countries No Covid-19 Case Today: {}".format(numberOfCountriesNoCasesToday))


numberOfCountriesNoDeathsToday = 0
for values in dataFromCsv['totalDeathsEntryday']:
    if values == 0:
        numberOfCountriesNoDeathsToday = numberOfCountriesNoDeathsToday + 1
print("Number of Countries No Death Case Today: {}".format(numberOfCountriesNoDeathsToday))


numberOfCountriesNoRecoveredToday = 0
for values in dataFromCsv['totalRecoveredEntryday']:
    if values == 0:
        numberOfCountriesNoRecoveredToday = numberOfCountriesNoRecoveredToday + 1
print("Number of Countries No Recovered Case Today: {}".format(numberOfCountriesNoRecoveredToday))


