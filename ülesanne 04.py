# ülesanne 04
# Python GUI
# Kert Kalamets
# 15.03.2022

from tkinter import *

aken = Tk()
aken.title('Kalkulaator')
aken.resizable(0,0)
aken.geometry('200x200')

tekst = Label(text='Siia kunagi vastus!',font='Tahoma 12')
tekst.grid(row=0, columnspan=4, padx=32, pady=2)

arv7 = Button(aken, text = '7')
arv7.grid(row=1, column=0, sticky=E+W, padx=2, pady=2)
arv8 = Button(aken, text = '8')
arv8.grid(row=1, column=1, sticky=E+W, padx=2, pady=2)
arv9 = Button(aken, text = '9')
arv9.grid(row=1, column=2, sticky=E+W, padx=2, pady=2)
nupp1 = Button(aken, text = '/')
nupp1.grid(row=1, column=3, sticky=E+W, padx=2, pady=2)
arv4 = Button(aken, text = '4')
arv4.grid(row=2, column=0, sticky=E+W, padx=2, pady=2)
arv5 = Button(aken, text = '5')
arv5.grid(row=2, column=1, sticky=E+W, padx=2, pady=2)
arv6 = Button(aken, text = '6')
arv6.grid(row=2, column=2, sticky=E+W, padx=2, pady=2)
nupp2 = Button(aken, text = '*')
nupp2.grid(row=2, column=3, sticky=E+W, padx=2, pady=2)
arv1 = Button(aken, text = '1')
arv1.grid(row=3, column=0, sticky=E+W, padx=2, pady=2)
arv2 = Button(aken, text = '2')
arv2.grid(row=3, column=1, sticky=E+W, padx=2, pady=2)
arv3 = Button(aken, text = '3')
arv3.grid(row=3, column=2, sticky=E+W, padx=2, pady=2)
nupp3 = Button(aken, text = '-')
nupp3.grid(row=3, column=3, sticky=E+W, padx=2, pady=2)
arv0 = Button(aken, text = '0')
arv0.grid(row=4, column=0, sticky=E+W, padx=2, pady=2)
nupp4 = Button(aken, text = ',')
nupp4.grid(row=4, column=1, sticky=E+W, padx=2, pady=2)
nupp5 = Button(aken, text = '=')
nupp5.grid(row=4, column=2, sticky=E+W, padx=2, pady=2)
nupp6 = Button(aken, text = '+')
nupp6.grid(row=4, column=3, sticky=E+W, padx=2, pady=2)
aken.mainloop()