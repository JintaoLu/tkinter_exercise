#!/usr/bin/env python  
# encoding: utf-8 

""" 
@version: v1.0 
@author: Jinato 
@file: Ex_loginWindow.py 
@time: 2017/12/17 16:51 
"""
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title("Welcom to Python")
window.geometry("900x500")

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
imageFile = tk.PhotoImage(file="C:\\Users\\duoyi\\Desktop\\sip.gif")
image = canvas.create_image(0, 0, anchor='nw', image=imageFile)
canvas.pack(side='top')

# user info
tk.Label(window, text="User name:").place(x=250, y=250)
tk.Label(window, text="Password:").place(x=250, y=290)

var_user_name = tk.StringVar()
var_user_name.set("example@python.com")
var_user_pwd = tk.StringVar()
entry_user_name = tk.Entry(window, textvariable=var_user_name).place(x=330, y=250)
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, show="*").place(x=330, y=290)

def usr_login():
    usr_name = var_user_name.get()
    usr_pwd = var_user_pwd.get()
    try:
        with open("usrs_info.pickle", 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {"admin": "admin"}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd in usrs_info[usr_name]:
            messagebox.showinfo(title="Welcome", message="how are you?" + usr_name)
        else:
            messagebox.showerror(message="Error, your password is wrong, try agian")
    else:
        is_sign_up = messagebox.askyesno(title="Welcome", message="You have not sign up yet.Sign up now?")
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sing_to_python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open("usrs_info.pickle", "rb") as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            messagebox.showerror(title="Error", message="Password and confirm password must be the same!")
        elif nn in exist_usr_info:
            messagebox.showerror(title="Error", message="The user has already signed up!")
        else:
            exist_usr_info[nn] = np
            with open("usrs_info.pickle", 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            messagebox.showinfo(title="Welcome", message="You have successfully signed up!")
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x300")
    window_sign_up.title("Sign up window")

    new_name = tk.StringVar()
    new_name.set("example@python.com")
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text="User name:").place(x=10, y=50)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=50)
    tk.Label(window_sign_up, text="password:").place(x=10, y=90)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show="*").place(x=150, y=90)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text="Confirm password:").place(x=10, y=130)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show="*").place(x=150, y=130)
    btn_sign_up_confirm = tk.Button(window_sign_up, text="Sign Up", command=sing_to_python).place(x=150, y=170)


# login and sign up button
btn_login = tk.Button(window, text="Login", command=usr_login).place(x=290, y=330)
btn_sign_up = tk.Button(window, text="Sign Up", command=usr_sign_up).place(x=380, y=330)


window.mainloop()