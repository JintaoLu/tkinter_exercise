#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_ListBox.py 
@time: 2017/12/15 20:44 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

var1 = tk.StringVar()
label = tk.Label(window, bg="yellow", width=4, textvariable=var1)
label.pack()

def print_selection():
    value = listBox.get(listBox.curselection())
    var1.set(value)

button = tk.Button(window, text="print selection",
                   width=15, height=2, command=print_selection)
button.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))

listBox = tk.Listbox(window, listvariable=var2)
listBox.pack()
list_items = [1, 2, 3, 4]
for item in list_items:
    listBox.insert("end", item)
listBox.insert(1, "first")
listBox.insert(2, "second")
listBox.delete(2)

window.mainloop()
