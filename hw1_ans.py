test = 2+3 # 答案存在指定test物件
test # 最後一行打指定物件名稱
import random
x=[random.randint(0,100) for i in range(0,12)]
x
x0_str=str(x[0])
x0_str
x_str=[str(x[i]) for i in range(0,len(x))]
x_str
x6_logi=x[6]<50
x6_logi
x_logi=[x[i]<50 for i in range(0,len(x))]
x_logi
num_false=x_logi.count(False)
num_false
import pandas as pd
df_business=pd.read_csv("http://data.gcis.nat.gov.tw/od/file?oid=340B4FDD-880E-4287-9289-F32782F792B8")
dict_business=df_business.to_dict()
address=list(dict_business['公司所在地'].values())
num_taoyuan=["桃園市" in address[i] for i in range(0,len(address))].count(True)
num_taoyuan
capital=list(dict_business['資本額'].values())
logi_largeCapital=[capital[i]>500000 for i in range(0,len(capital))]
num_largeCapital=logi_largeCapital.count(True)
num_largeCapital
import requests
response=requests.get("https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=3")
danceInfo=response.json()
numDance=len(danceInfo)
numDance
title1=danceInfo[0]['title']
title1
local1=danceInfo[0]['showInfo'][0]['location']
local1
time1=danceInfo[0]['showInfo'][0]['time']
time1
## 解答一: 當showInfo不唯一但只考慮每個showInfo的第一個
danceInfoList=[{
'title': danceInfo[i]['title'], 
'time': danceInfo[i]['showInfo'][0]['time'], 
'location': danceInfo[i]['showInfo'][0]['location']
} for i in range(0,len(danceInfo))]
danceInfoList

## 解答二：
danceInfoList2=list([])
for i in range(len(danceInfo)):
    title_i=danceInfo[i]['title']
    for j in range(len(danceInfo[i]['showInfo'])):
        time_ij=danceInfo[i]['showInfo'][j]['time']
        location_ij=danceInfo[i]['showInfo'][j]['location']
        danceInfoList2.append({
        'title': title_i,
        'time': time_ij,
        'location': location_ij
        })


## 解答一: 當showInfo不唯一但只考慮每個showInfo的第一個
danceInfoStr=['【{title}】將於{time}在{location}演出'.format(
title=danceInfoList[i]['title'],
time=danceInfoList[i]['time'],
location=danceInfoList[i]['location']) for i in range(0,len(danceInfoList))]
danceInfoStr

## 解答二： 
danceInfoStr2=['【{title}】將於{time}在{location}演出'.format(
title=danceInfoList2[i]['title'],
time=danceInfoList2[i]['time'],
location=danceInfoList2[i]['location']) for i in range(0,len(danceInfoList2))]
danceInfoStr2
