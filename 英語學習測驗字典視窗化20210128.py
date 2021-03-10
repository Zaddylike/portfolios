'''
英語學習測驗字典
'''
import os
import json
import random
import time
import tkinter as tk
import tkinter.messagebox
def _engtest():
    englishList=[]
    timE=10
    while True:
        quatioN=random.sample(englishDict.items(),1)
        if quatioN not in englishList:
            timE=timE-1
            englishList.append(quatioN)
            return quatioN
        else:
            continue
        if timE==0:
            break
def _addWord():
    englishDict[enteR.get()]=enteR1.get()
    enteR.delete(0,tk.END)
    enteR1.delete(0,tk.END)
    enteR1.focus()
def _searchWord():
    if enteR2.get() in englishDict:
        lB3["text"]="中文是:",englishDict.get(enteR2.get()) #englishDict.get(enteR2.get()) englishDict[enteR2.get()]
    else:
        lB3["text"]="沒有這個單字喔"
def _deleteWord():
    if enteR2.get() in englishDict:
        del englishDict[enteR2.get()]
        lB3["text"]=enteR2.get()+"已刪除"
        enteR2.delete(0,tk.END)
    else:
        lB3["text"]="沒有這個單字耶"
        enteR2.delete(0,tk.END)
def _testWord():
    if enteR3.get()==_engtest()[0][1]:
        lB5["text"]="correct"
        
        enteR3.delete(0,tk.END)
    else:
        lB5["text"]="wrong"
        lB5eng["text"]=_engtest()[0][0]
        enteR3.delete(0,tk.END)
def _nexttestWord():
    enteR3.delete(0,tk.END)
    lB5["text"]=""
    lB5eng["text"]=_engtest()[0][0]

def _hit1():
    global enteR,enteR1
    addWin=tk.Toplevel(wiN)
    addWin.geometry("400x500+520+120")
    addWin.title("add word")
    lB2=tk.Label(addWin,text="請輸入英文",bg="black",fg="white",font=("airal",16),width=10,height=2)
    lB2.pack()
    enteR=tk.Entry(addWin,font=("airal",16),bd=5)
    enteR.pack()
    lB3=tk.Label(addWin,text="請輸入中文",bg="black",fg="white",font=("airal",16),width=10,height=2)
    lB3.pack()
    enteR1=tk.Entry(addWin,font=("airal",16),bd=5)
    enteR1.pack()
    btN3=tk.Button(addWin,width=10,height=2,bd=5,text="輸入",bg="white",fg="black",command=_addWord)
    btN3.pack()
def _hit2():
    global enteR2,lB3
    searchWin=tk.Toplevel(wiN)
    searchWin.geometry("400x500+520+120")
    searchWin.title("search word")
    lB4=tk.Label(searchWin,text="請輸入英文",bg="black",fg="white",font=("airal",16),width=10,height=2)
    lB4.pack()
    enteR2=tk.Entry(searchWin,font=("airal",16),bd=5)
    enteR2.pack()
    lB3=tk.Label(searchWin,bg="black",fg="white",font=("airal",16),width=10,height=2)
    lB3.pack()
    btN4=tk.Button(searchWin,width=10,height=2,bd=5,text="查詢",bg="white",fg="black",command=_searchWord)
    btN4.pack()
    btN5=tk.Button(searchWin,width=10,height=2,bd=5,text="刪除",bg="white",fg="black",command=_deleteWord)
    btN5.pack()
def _hit3():
    global quatioN,englishList,timE,lB5eng,enteR3,lB5
    testWin=tk.Toplevel(wiN)
    testWin.geometry("400x500+520+120")
    testWin.title("test")
    timE=10

    lB5eng=tk.Label(testWin,bg="black",fg="white",font=("airal",16),width=10,height=2)
    lB5eng.pack()
    lB5eng["text"]=_engtest()[0][0]
    enteR3=tk.Entry(testWin,font=("airal",16),bd=5)
    enteR3.pack()
    lB5=tk.Label(testWin,bg="black",fg="white",font=("airal",16),width=10,height=2)
    lB5.pack()
    btN6=tk.Button(testWin,width=10,height=2,bd=5,text="輸入",command=_testWord)
    btN6.pack()
    btN7=tk.Button(testWin,width=10,height=2,bd=5,text="下一題",command=_nexttestWord)
    btN7.pack()

def _endWin():
    with open("english word.json","w",encoding="utf-8") as filE:
        json.dump(englishDict,filE,ensure_ascii=False,indent=4)
    enD=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if enD:
        wiN.destroy()
    

#--------------------------------------------------------------
if os.path.isfile("english word.json"):
    with open("english word.json","r",encoding="utf-8") as filE:
        englishDict=json.load(filE)
else:
    englishDict={}
    
wiN=tk.Tk()
wiN.title("english dictonary & test")
wiN.geometry("400x500+500+100")
wiN.resizable(width=False,height=False)

lb=tk.Label(wiN,text="英語字典",width=20,height=4,bg="black",fg="white",font=("arial",16))
lb.pack()
btN3=tk.Button(wiN,text="結束程式",fg="red",font=("Arial",16),width=10,height=2,command=_endWin)
btN3.pack(side=tk.BOTTOM)
btN2=tk.Button(wiN,text="英文測驗",fg="blue",font=("Arial",16),width=10,height=2,command=_hit3)
btN2.pack(side=tk.BOTTOM)
btN1=tk.Button(wiN,text="查詢及刪除",fg="blue",font=("Arial",16),width=10,height=2,command=_hit2)
btN1.pack(side=tk.BOTTOM)
btN=tk.Button(wiN,text="新增及查詢",fg="green",font=("Arial",16),width=10,height=2,command=_hit1)
btN.pack(side=tk.BOTTOM)




    
wiN.mainloop()


with open("english word.json","w",encoding="utf-8") as filE:
    json.dump(englishDict,filE,ensure_ascii=False,indent=4)
            
        

        



