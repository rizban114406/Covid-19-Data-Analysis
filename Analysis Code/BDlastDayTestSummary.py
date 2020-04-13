import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)
CoronaTestCaseNo = pd.read_csv('../Analysis Data/CoronaTestCaseNo.csv')
df = pd.Series([int(CoronaTestCaseNo.iloc[3,4]),int(CoronaTestCaseNo.iloc[1,4])])
df.index=['Positive','Test_Conducted']
slices=int(CoronaTestCaseNo.iloc[3,4])+int(CoronaTestCaseNo.iloc[1,4])
my_explode=(0,0.2)

df.plot.pie(subplots=True,figsize=(10, 10),shadow= True,
            title="LastDay -- Positive vs Test_Conducted",
            colors=['#8B0000','#CD5C5C'],
            explode=my_explode, startangle=90,
            autopct=lambda pct: func(pct, slices))
plt.show()
