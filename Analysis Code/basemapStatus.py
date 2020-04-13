import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('seaborn')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
dataFromCsv = pd.read_csv('../Analysis Data/internationalCovid19Status.csv')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
##
##['Unnamed: 0', 'id', 'displayName', 'totalConfirmed', 'totalDeaths',
##       'totalRecovered', 'totalRecoveredEntryday', 'totalDeathsEntryday',
##       'totalConfirmedEntryday', 'entryDatetime', 'lattitude', 'longitude',
##       'parentId']
#full Map
m = Basemap(projection='mill',
            llcrnrlat = -90, #lower left corner lat value (South value)
            llcrnrlon = -180, #lower left corner long value(West Value)
            urcrnrlat = 90,  #upper right corner lat value(North Value)
            urcrnrlon = 180,  #upper right corner long value(East Value
            resolution='l')
m.drawcoastlines() # to draw all costal lines
m.drawcountries()

xs = []
ys = []
NYClat, NYClon = 40.7127, -74.0059 #Lat Long
xpt, ypt = m(NYClon, NYClat) # Flipped for use
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'c*', markersize=15)

plt.title('Basemap Tutorial')
plt.show()
