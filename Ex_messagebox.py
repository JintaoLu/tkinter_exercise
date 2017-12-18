#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_messagebox.py 
@time: 2017/12/17 16:26 
"""
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("my window")
window.geometry("300x200")

def hit_me():
    # messagebox.showinfo(title="hello", message="hahaha")
    # messagebox.showwarning(title="hello", message="hahaha")
    # messagebox.showerror(title="hello", message="hahaha")
    # print(messagebox.askquestion(title="hello", message="hahaha")) #return 'yes' 'no'
    # print(messagebox.askyesno(title="hello", message="hahaha")) #return True/False
    print(messagebox.askokcancel(title="hello", message="hahaha")) #return True/False

button = tk.Button(window, text="hit me", command=hit_me).pack()

window.mainloop()