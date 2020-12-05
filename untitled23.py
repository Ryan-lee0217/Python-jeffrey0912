# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:16:22 2020

@author: ryanl
"""

import tkinter as tk
window = tk.Tk()
window.geometry("300x300")
tk.Label(window,text="place").place(x=0,y=0)
tk.Label(window,text="place").place(x=150,y=150)
tk.Label(window,text="place").place(x=260,y=260)
tk.Label(window,text="place").place(x=300,y=300)
window.mainloop()