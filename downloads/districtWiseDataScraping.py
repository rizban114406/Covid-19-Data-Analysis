import tabula
import pandas as pd
import re
import requests

url = 'https://www.iedcr.gov.bd/website/images/files/nCoV/Confirmed%20cases%20in%20Bangladesh_upto%20April%2011_2020.pdf'
myfile = requests.get(url)
print(myfile.content)
open('iedcr.pdf', 'wb').write(myfile.content)
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
df = tabula.read_pdf("iedcr.pdf", encoding='utf-8',pages=1)
df
for x in df:
    s=str(x)

#df.to_csv('output.csv', encoding='utf-8')
#print(file)
s = re.sub(' +',',',s)
s = re.sub('NaN+',',',s)
s = re.sub(',+',' ',s)
s = StringIO(s)
with open('./Analysis Data/DistrictWiseCase.csv', 'w+') as f:
    f.write('0,City,case\n')
    for line in s:
        res = len(line.split())
        if res<5:
            if res==4:
                string = line.split(" ")
                string.pop(1)
                line=' '.join(string)
            line = re.sub(' +',',',line)
            f.write(line)
            
        

print("Two file created,DistrictWiseCase.csv & iedcr.pdf")

print('finished')

