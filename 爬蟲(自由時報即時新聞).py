'''
tkinter示範程式--listbox+scrollbar的應用
'''
import tkinter as tk


def _hit1():
    urL="https://news.ltn.com.tw/list/breakingnews"
    rQ=requests.get(urL).text
    souP=BeautifulSoup(rQ,"html5lib")
    souP1=souP.find("div","whitecon boxTitle")
    for mysouP in souP1.find_all("li"):
        try:
            listBox.insert(tk.END,mysouP.span.text.strip())
            listBox.insert(tk.END,mysouP.p.text.strip())
            listBox.insert(tk.END,mysouP.a["href"].strip())
            listBox.insert(tk.END,"-----------------------")
        except:
            continue


def _hit2():
    wiN.title(listBox.get(listBox.curselection()))
#--------------------------------------------------
import requests
from bs4 import BeautifulSoup
import json 
import tkinter as tk
#--------------------------------------------------

#--------------------------------------------------

wiN = tk.Tk()
wiN.title("Welcome!!!")
wiN.geometry("600x500")

#enteR.pack()
btN1 = tk.Button(wiN, text="加入!!",fg="green", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN, text="顯示成標題!!",fg="blue", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 

sBar=tk.Scrollbar(wiN)
sBar.pack(side=tk.RIGHT,fill=tk.Y)

listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set)
listBox.pack(side=tk.BOTTOM,fill=tk.BOTH)
sBar.config(command=listBox.yview)

wiN.mainloop()

