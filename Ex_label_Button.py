#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_label_Button.py 
@time: 2017/12/15 20:15 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x100")

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg="green",
             font=("Arial", 12), width=15, height=2)
l.pack()

on_hit = True
def hit_me():
    global on_hit
    if on_hit == True:
        on_hit = False
        var.set("you hit me")
    else:
        on_hit = True
        var.set("")

b = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)
b.pack()

window.mainloop()