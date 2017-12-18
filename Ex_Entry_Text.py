#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_Entry_Text.py 
@time: 2017/12/15 20:32 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

e = tk.Entry(window, show=None)
# e = tk.Entry(window, show="*")
e.pack()

def insert_point():
    var = e.get()
    t.insert("insert", var)

def insert_end():
    var = e.get()
    # t.insert("end", var)
    t.insert("2.3", var)

b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end", width=15, height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()