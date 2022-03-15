# ülesanne 3
# Python GUI
# Kert Kalamets
# 15.03.2022

from tkinter import *

aken = Tk()
aken.title('Kert Kalamets - ülesanne 3')
aken.resizable(0,0)
tekst = Label(aken, text = 'Nimi: Kert Kalamets\nRühm: IT21\n2022', font = 'Tahoma 16 bold italic', bg = 'red', fg ='blue', padx = 30, pady = 10).pack()

aken.mainloop()