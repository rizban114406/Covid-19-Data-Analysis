import re
import psutil,os
import bs4 as bs
import urllib.request
import pandas as pd


main_url='https://www.iedcr.gov.bd/'
source = urllib.request.urlopen(main_url).read()
soup = bs.BeautifulSoup(source,'lxml')
data = []
table = soup.find('table')
table_body = table.find('tbody')
col=table.find_all('th')
col = [ele.text.strip() for ele in col]
data.append([ele for ele in col if ele])
rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
testCaseNo= pd.DataFrame(data)

testCaseNo.to_csv(r'./Analysis Data/testCaseNoBD.csv')
print('TestCaseNoBD.csv created')
