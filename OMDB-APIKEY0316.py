'''
api for OMDB
'''

def _newPage(thisPage):     #使用這個自訂函式來取得每一頁的資料
    movieUrl=urlOMDB+movieName+"&apikey="+myKey+"&page="+str(thisPage)
    datA=json.loads(requests.get(movieUrl).text)    #取得的資料轉換成JSON檔的格式
    with open(movieName+"(s).json","a",encoding="utf-8") as filE:
        json.dump(datA,filE,ensure_ascii=False,indent=4)
    return(datA)


import requests
import json
import math
from selenium import webdriver 

urlOMDB="http://www.omdbapi.com/?s="    #參數改成[s]
myKey="52e16be"

moviE=input("請輸入英文電影名稱: ")
movieName="+".join(moviE.split())
#print(movieName)

movieUrl=urlOMDB+movieName+"&apikey="+myKey
dictFile=json.loads(requests.get(movieUrl).text)

totaL=int(dictFile["totalResults"])     #取得相關電影的總數
pageS=math.ceil(totaL/10)+1         #計算總頁數

weB=webdriver.Chrome()

if dictFile:
    countS=0
    print("==============================================")
    for myPage in range(1,pageS):
        dataS=_newPage(myPage)
        for iteM in dataS["Search"]:
            countS=countS+1
            print(str(countS)+"."+"---------------------------")
            print(iteM["Title"])
            print(iteM["Year"])
            print(iteM["imdbID"])
            print(iteM["Type"])
    print("==============================================")
    print("相關電影總共有: "+str(totaL)+" 部")   
else:
    print("找不到相關電影資訊!!")    
    
    
    
    
    
    
    