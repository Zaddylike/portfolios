'''
ues api for grab post-author ip address on ptt

202010
'''

import datetime
from selenium import webdriver
import json
import csv
import requests
import re
import pandas
import matplotlib.pyplot as plt

totaL=int(input("how many items do you want to search :"))
todaY1=datetime.date.today()
#print(todaY1)
todaY=str(todaY1).split("-")
# print(todaY)
if int(todaY[1])<10:
    todaY=str(int(todaY[1])) +"/"+ todaY[2]  
    #設定抓取今日文章的限制參數
else:
    todaY=todaY[1]+"/"+todaY[2]
    #print(todaY)
    
apiKey="c8116a5da96c86dc257f3e175c0e2353"

urL="https://www.ptt.cc/bbs/Gossiping/index.html"
    #cookieS={"over18:1"} 因為用click 故不需要用
headLess=webdriver.ChromeOptions()
headLess.add_argument("headless")
weB=webdriver.Chrome(options=headLess)
weB.get(urL)
btN1=weB.find_element_by_xpath("/html/body/div[2]/form/div[1]/button")
    #click botton
btN1.click()

continentS={}
citYS={}
countryS={}
limiT=5

csvFile=open("distribution of posters.csv","w",newline="",encoding="utf-8-sig")
writeR=csv.writer(csvFile)
writeR.writerow(["City","poster"])

while totaL>0:
    for i in weB.find_elements_by_class_name("r-ent"):
        if i.find_element_by_class_name("date").text != todaY:
            limiT = limiT - 1 
            if limiT== 0:
                break
        else:
            try:
                #print(i.find_element_by_tag_name("a").get_attribute("href"))
                posturL=i.find_element_by_tag_name("a").get_attribute("href")
                # print(posturL)
                cookieS={"over18":"1"}
                daT=requests.get(posturL,cookies=cookieS).text
                
                patterN="來自: \d+\.\d+\.\d+\.\d+"      #建立找尋ip的正規表示式
                macH=re.search(patterN,daT)             #把符合搜尋條件的資料放在macH    
                # print(macH)
                iP=macH.group(0).replace("來自: ","")
                # print(iP)
                
                ipstacK="http://api.ipstack.com/{}?access_key={}".format(iP,apiKey)
                ipdaT=requests.get(ipstacK).json()
                # print(ipdaT)
                # print(ipdaT["continent_name"])
                # print(ipdaT["country_name"])
                # print(ipdaT["city"])
                # 這邊開始用json來計算各國ip以便之後統計
                continenT=ipdaT["continent_name"]
                countrY=ipdaT["country_name"]
                citY=ipdaT["city"]

                
                if continenT not in continentS.keys():  
                    continentS[continenT]=1
                else:
                    continentS[continenT]=continentS[continenT]+1
                    
                if countrY not in countryS.keys():
                    countryS[countrY]=1
                else:
                    countryS[countrY]=countryS[countrY]+1
                    
                if citY not in citYS.keys():
                    citYS[citY]=1
                else:
                    citYS[citY]=citYS[citY]+1
                totaL= totaL-1
            except:
                continue
        if totaL== 0:
            break
for n,t in citYS.items():
    writeR.writerow([n,t]) #數據化分析用


print("Total search",totaL,"time")
print("Cintinent distribution of posters :")
for c,t in continentS.items():
    print(c,t)
    print("----------")
print()
print("Country distribution of posters :")
for c,t in countryS.items():   #印出nationS字典內的所有項目
    print(c,t)
    print("----------")
print()

print("Nation distribution of posters :")
for n,t in citYS.items():
    print(n,t)
    print("----------")

csvFile.close()
weB.close()

filE=pandas.read_csv("distribution of posters.csv")
plt.pie(filE["poster"]  ,                  
        labels = filE["City"],            
        autopct = "%1.1f%%",           
        # explode = separeted,       
        pctdistance = 0.6,              
        textprops = {"fontsize" : 12},  
        shadow=True)                 
plt.axis('equal')                                          
plt.title("distribution of posters", {"fontsize" : 18}) 
plt.legend(loc = "best")                                

plt.savefig("Pie chart of car accident.jpg", 
            bbox_inches='tight',               
            pad_inches=0.0)                 


















