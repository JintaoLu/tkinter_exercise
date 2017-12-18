#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_MenuBar.py 
@time: 2017/12/17 15:28 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

label = tk.Label(window, bg="yellow", width=30, text="empty")
label.pack()

counter = 0
def do_job():
    global counter
    label.config(text="do " + str(counter))
    counter += 1

menubar = tk.Menu(window)
fileMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=do_job)
fileMenu.add_command(label="open", command=do_job)
fileMenu.add_command(label="save", command=do_job)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

editMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=do_job)
editMenu.add_command(label="copy", command=do_job)
editMenu.add_command(label="paste", command=do_job)

subMenu = tk.Menu(fileMenu)
fileMenu.add_cascade(label="Import", menu=subMenu, underline=0)
subMenu.add_command(label="submenu1", command=do_job)
subMenu.add_command(label="submenu2", command=do_job)

window.config(menu=menubar)
window.mainloop()