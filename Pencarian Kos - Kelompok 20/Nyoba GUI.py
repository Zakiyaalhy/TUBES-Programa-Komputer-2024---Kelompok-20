# ASISTENSI
import customtkinter
from PIL import Image
import os
import tkinter as tk
from tkinter import *

def login_page():
    # global page1
    font_login = "Roboto Condensed"
    page1 = Tk()
    page1.title("Pencarian Kos Asik.py")
    page1.configure(bg="#D4EDF4")
    page1.geometry("900x600")
    page1.resizable(False, False)

    judul = Label(page1, text="Login Page",bg="white", font=(font_login, 35))
    judul.place(x=335,y=210)

    username = Entry(page1,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
    username.place(x=350,y=300)
    
    password = Entry(page1,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
    password.place(x=350,y=330)

    Button(page1,width=25,height=1,text="Login", fg="white",bg="#57a1f8").place(x=359,y=360)

    Button(page1,width=25,height=1,text="Register", fg="white",bg="#57a1f8").place(x=359,y=390)
    page1.mainloop()

login_page()
