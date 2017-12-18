#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_CkeckButton.py 
@time: 2017/12/17 15:05 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

label = tk.Label(window, bg="yellow", width=30, text="empty")
label.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        label.config(text="you have selected python ")
    elif (var1.get() == 0) & (var2.get() == 1):
        label.config(text="you have selected c++" )
    elif (var1.get() == 1) & (var2.get() == 1):
        label.config(text="you have selected both" )
    else:
        label.config(text="you have selected nothing")

var1 = tk.IntVar()
var2 = tk.IntVar()

ckeckButton1 = tk.Checkbutton(window, text="Python", variable=var1,
                              onvalue=1, offvalue=0, command=print_selection)
ckeckButton2 = tk.Checkbutton(window, text="C++", variable=var2,
                              onvalue=1, offvalue=0, command=print_selection)
ckeckButton1.pack()
ckeckButton2.pack()

window.mainloop()