# ülesanne 06
# Python GUI
# Kert Kalamets
# 15.03.2022

from tkinter import *

aken = Tk()
aken.title('ülesanne 06')
aken.geometry('400x400')
aken.resizable(0,0)

louend = Canvas(aken, width=400, height=400)
louend.pack()
louend.create_rectangle(20,20,160,110, fill='red', outline='red')
louend.create_rectangle(60,20,75,110, fill='white', outline='white')
louend.create_rectangle(20,57,160,75, fill='white',outline='white')

pilt = PhotoImage(file='Taani.png')
louend.create_image(0,120, anchor=NW, image=pilt)




aken.mainloop()