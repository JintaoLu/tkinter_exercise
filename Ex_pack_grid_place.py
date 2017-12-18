#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_pack_grid_place.py 
@time: 2017/12/17 16:44 
"""
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("my window")
window.geometry("300x200")

# tk.Label(window, text="top").pack(side='top')
# tk.Label(window, text="bottom").pack(side='bottom')
# tk.Label(window, text="left").pack(side='left')
# tk.Label(window, text="right").pack(side='right')

# for i in range(4):
#     for j in range(3):
#         # tk.Label(window, text="1").grid(row=i, column=j, padx=10, pady=10)
#         tk.Label(window, text="1").grid(row=i, column=j, ipadx=10, ipady=10)

tk.Label(window, text="place").place(x=10, y=100, anchor='sw')

window.mainloop()