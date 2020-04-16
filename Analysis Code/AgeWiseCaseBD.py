import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)
style.use('fivethirtyeight')
ageRangeCaseBangladesh = pd.read_csv('../Analysis Data/ageRangeCaseBangladesh.csv')
df = ageRangeCaseBangladesh.iloc[:,1:]


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

slices = []
activities = []
for ranges in df['ageRange']:
    activities.append(ranges)
for ranges in df['noOfCase']:
    slices.append(ranges)
my_explode = (0, 0, 0,0.2,0,0,0)
color = ['#00FFFF','#556B2F','#FF4500','#800000','#708090','#4B0082','#FF1493']
wedges, texts,autopcts = ax1.pie(slices,
##                       labels=activities,
                       radius=1,
                       colors = color, 
                       startangle=60, #Starting angle point
                       pctdistance=1.22,
                       labeldistance=1.2,
                       explode=my_explode,
                       wedgeprops=dict(width=0.3, edgecolor='w'),
                       autopct=lambda pct: func(pct, slices)) # Adds the percentage
plt.setp(autopcts, **{'color':'#000080', 'weight':'bold', 'fontsize':10})

ax1.legend(wedges, activities,loc="upper right",
           bbox_to_anchor=(1, 0, 0.5, .5),
           prop={'size': 10})

plt.subplots_adjust(left=0.05, bottom=0.20, right=0.94, top=.75, wspace=0, hspace=0)
plt.show()
