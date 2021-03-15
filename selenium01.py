from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

searcH=input("search something you want :")
urL="https://24h.pchome.com.tw/"
user_agent ="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
opS=webdriver.ChromeOptions()
opS.add_argument("--user-agent=%s" % user_agent)
# hL=webdriver.ChromeOptions()
# hL.add_argument("headless")
weB=webdriver.Chrome(options=opS) #options=hL
weB.get(urL)

keyWord=weB.find_element_by_xpath('//*[@id="keyword"]') #搜尋欄參數
keyWord.send_keys(searcH)
keyWord.send_keys(Keys.ENTER)



nuM=1
for v in range(10):
    souP=weB.find_elements_by_class_name("prod_name")
    for i in souP:
        print(nuM,"--",i.text)
        nuM+=1
    weB.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.3)
    

