import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)
ageRangeCaseBangladesh = pd.read_csv('../Analysis Data/ageRangeCaseBangladesh.csv')
df = ageRangeCaseBangladesh.iloc[:,1:]
dd=[df.noOfCase]
slices=dd
df.set_index(['ageRange'],inplace=True)
df.columns=['Age_Range VS No_Of_Case']
my_explode = (0, 0, 0,0.2,0,0,0)
df.plot.pie(subplots=True,figsize=(10, 10),shadow= True, explode=my_explode, startangle=90,autopct=lambda pct: func(pct, slices)) # Adds the percentage)
plt.show()
