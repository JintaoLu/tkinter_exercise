#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_Canvas.py 
@time: 2017/12/17 15:14 
"""
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x200")

def moveit():
    canvas.move(rectangle, 0, 2)

canvas = tk.Canvas(window, bg="blue", height=100, width=200)
canvas.pack()
image_file = tk.PhotoImage(file="C:\\Users\\duoyi\\Desktop\\sip.gif")
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill="red")
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rectangle = canvas.create_rectangle(x0 + 30, y0 + 20, x1 + 20, y1 + 20)
button = tk.Button(window, text="move", command=moveit).pack()



window.mainloop()