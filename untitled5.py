# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:26:56 2020

@author: ryanl
"""

import tkinter as tk
window = tk.Tk()
window.geometry("300x300")
tk.Label(window,text="pack").pack(side="top")
tk.Label(window,text="pack").pack(side="bottom")
tk.Label(window,text="pack").pack(side="left")
tk.Label(window,text="pack").pack(side="right")
window.mainloop()