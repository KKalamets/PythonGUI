# Ülesanne 05
# Python GUI
# Kert Kalamets
# 15.03.2022

from tkinter import *
import tkinter.ttk

aken = Tk()
aken.title('käibemaksukalkulaator')
aken.geometry('240x130')
aken.resizable(0,0)

kmp = 0
km = 0
kmhind = 0

silt1 = Label(aken, text='Hind Käibemaksuta:' )
silt1.grid(row=0, column=0)
silt2 = Label(aken, text='Käibemaks:')
silt2.grid(row=5, column=0)
silt4 = Label(aken, text='Hind käibemaksuga:')
silt4.grid(row=6, column=0)
sisend1 = Entry(aken)
sisend1.grid(row=0, column=1, sticky=E+W)
sep = ttk.Separator(aken,orient='horizontal')
sep.grid(row=4,column=0, columnspan=2, sticky=E+W, padx=5)
def Arvuta():
    global kmp
    global km
    hind = float(sisend1.get())
    kmp = float(protsent.get())
    km = hind*(kmp/100)
    uushind = hind+kmp
    silt3 = Label(aken, text=(km))
    silt3.grid(row=5, column=1)
    silt5 = Label(aken, text=uushind)
    silt5.grid(row=6, column=1)

protsent = IntVar()
valik = Radiobutton(aken, text='20%', variable=protsent, value=20, command=Arvuta)
valik.grid(row=2,column=0)
valik = Radiobutton(aken, text='9%', variable=protsent, value=9, command=Arvuta)
valik.grid(row=3,column=0)
aken.mainloop()