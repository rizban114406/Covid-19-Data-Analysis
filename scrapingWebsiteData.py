import re
import psutil,os
import bs4 as bs
import urllib.request
import re

main_url='http://119.40.84.187/surveillance/'
source = urllib.request.urlopen(main_url).read()
soup = bs.BeautifulSoup(source,'lxml')
script=soup.find_all('script')
# print(script)

scrappedLines = []
for lines in script:
    data = (str(lines)).replace('\r','')
#     data = (str(data)).replace(' ','')
    scrappedLines.append(data)
# print(scrappedLines)
# print(len(scrappedLines))



file = open("scrap.txt", 'w+')
for lines in scrappedLines:
#     print(lines)
#     print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    if "['Date', 'Number of Patients']," in lines:
        data = (str(lines)).replace(' ','')
        file.write(data)
file.close()



file = open('scrap.txt','r')
template = file.readlines()
file.close()
while '\n' in template: template.remove('\n')
#print(len(template))
#print(template)

index = -1
dataFlag = 0

dateNumberofPatient = []
agegroupNumber = []
historyNumber = []
genderNumber = []
while(index < len(template)-1):
    index = index + 1
    template[index] = (template[index]).replace('\n','')
    print(template[index])
    print(dataFlag)
#    print("bbbbbbbbbbbbbbbbbbbbbbbb")
# Initialize Flag
    if "['Date','NumberofPatients']," in template[index]:
        dataFlag = 1
        continue
    elif "['AgeGroup','NumberofPatients']," in template[index]:
        dataFlag = 2
        continue
    elif "['History','NoofCase',{role:'style'}]," in template[index]:
        dataFlag = 3
        continue
    elif "['Gender','NoofCase',{role:'style'}]," in template[index]:
        dataFlag = 4
        continue

# Fetching the Data 
    if dataFlag == 1:
        if "]);" in template[index]:
            dataFlag = 0
            continue
        else:           
            splitLine = template[index].split(',')
            entryDate = splitLine[0][2:-1]
            number = splitLine[1][:-1]
            dateNumberofPatient.append([entryDate,number])
            continue
    if dataFlag == 2:
        if "]);" in template[index]:
            dataFlag = 0
            continue
        else:           
            splitLine = template[index].split(',')
            ageGroup = splitLine[0][2:-1]
            number = splitLine[1][:-1]
            agegroupNumber.append([ageGroup,number])
            continue
    if dataFlag == 3:
        if "]);" in template[index]:
            dataFlag = 0
            continue
        else:           
            splitLine = template[index].split(',')
            history = splitLine[0][2:-1]
            number = splitLine[1]
            historyNumber.append([history,number])
            continue
    if dataFlag == 4:
        if "]);" in template[index]:
            dataFlag = 0
            continue
        else:           
            splitLine = template[index].split(',')
            gender = splitLine[0][2:-1]
            number = splitLine[1]
            genderNumber.append([gender,number])
            continue

    
    print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
print(dateNumberofPatient)
print(agegroupNumber)
print(historyNumber)
print(genderNumber)
