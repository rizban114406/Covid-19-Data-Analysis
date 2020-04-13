import tabula
import re
import psutil,os
import bs4 as bs
import urllib.request
import urllib.parse
import os.path
from os import path
from datetime import date

main_url='http://iedcr.gov.bd/'
source = urllib.request.urlopen(main_url).read()
# print(source)
soup = bs.BeautifulSoup(source,'html.parser')
# print(soup)
script=soup.find_all('a',href = True)
fileName = str(date.today()) + '.pdf'
fileNameCsv = str(date.today()) + '.csv'
for links in soup.find_all('a',href = True):
    print(links['href'])
    if (len(links['href']) > 15 and len(links['href']) < 100 and ('.pdf' in str(links['href']))):
        link = urllib.parse.quote(links['href'])
        url = main_url + link
#         url = "https://iedcr.gov.bd/website/images/files/nCoV/Confirmed%20cases%20in%20Bangladesh_upto%20April%2012.pdf"
        print(url) 
        destination = './downloads/' + str(fileName)
        if path.exists(destination) == False:
            print("New Downloading File: {}".format(url))
#             print(len(links['href']))
            urllib.request.urlretrieve(url, destination)

### Read pdf into list of DataFrame
##df = tabula.read_pdf("2020-04-13.pdf", pages='all')
##
### Read remote pdf into list of DataFrame
##df2 = tabula.read_pdf("2020-04-13.pdf")

# convert PDF into CSV file
tabula.convert_into(fileName, fileNameCsv, output_format="csv", pages='all')

# convert all PDFs in a directory
##tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all)
