#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_Scale.py 
@time: 2017/12/15 21:00 
"""
# !/usr/bin/env python
# encoding: utf-8

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_RadioButton.py 
@time: 2017/12/15 20:54 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

label = tk.Label(window, bg="yellow", width=20, text="empty")
label.pack()

def print_selection(v):
    label.config(text="you have selected " + v)


scale = tk.Scale(window, label="try me", from_=5, to=11,
                 orient=tk.HORIZONTAL, length=200, showvalue=True,
                 tickinterval=2, resolution=0.01, command=print_selection)
scale.pack()

window.mainloop()