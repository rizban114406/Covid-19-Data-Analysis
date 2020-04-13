import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib import style
print(plt.style.available)
style.use('seaborn-deep')
fig = plt.figure(figsize=(10,7))
ax1 = plt.subplot2grid((1, 1), (0, 0), rowspan=2)
dataFromCsv = pd.read_csv('../Analysis Data/DistrictWiseCase.csv')
result = dataFromCsv.sort_values(['case'], ascending= True)
case=result.case
print(case)
ax1.barh(result.City,case, label='Number of Corona Cases', color='#CD5C5C')
for i in ax1.patches:
    print(i)
    ax1.text(i.get_x()+i.get_width()+5, i.get_y(), \
            str(i.get_width()), fontsize=7,
                color='grey',rotation=0)
plt.xlabel('Number of Cases')
plt.ylabel('District')
plt.title("Cases Summary of Covid-19(Bangladesh-District_Wise)")
plt.legend()
plt.subplots_adjust(left=0.35, bottom=0.15, right=0.94, top=0.90, wspace=0, hspace=0.4)
plt.show()
