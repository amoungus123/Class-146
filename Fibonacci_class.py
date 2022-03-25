# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:26:35 2022

@author: pulle
"""

from  tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("600x100")

label_series = Label(root, text="Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_flower['text'] = "Flower is fully blossmed"
        label_spiral["text"] = " Spirals in the Right Direction are " + str(first_no) + " and Spirals in the Left Direction are " + str(second_no) + " /n. Total Spirals are " + str(sum)
        
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_flower.pack()
label_series.pack()
label_spiral.pack()

root.mainloop()