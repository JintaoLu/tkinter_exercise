#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_Frame.py 
@time: 2017/12/17 15:56 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

label = tk.Label(window, bg="yellow", width=30, text="on the window")
label.pack()

frm = tk.Frame(window, bg="blue").pack()
frm_l = tk.Frame(frm)
frm_l.pack(side="left")
frm_r = tk.Frame(frm, bg="red")
frm_r.pack(side="right")

tk.Label(frm_l, bg="blue", text="on the frm_l1 ba ba").pack()
tk.Label(frm_l, bg="yellow", text="on the frm_l2").pack()
tk.Label(frm_r, bg="red", text="on the frm_r1").pack()

window.mainloop()