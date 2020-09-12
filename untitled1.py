# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:25:50 2020

@author: ryanl
"""

import tkinter as tk
window = tk.Tk()
window.title("tk1")
def clickMe():
     tkinter.messagebox.showinfo(title,message="點珊小") 
label  = tk.label(window,text=="按我",bg="AEFDFF",FG"12345")
window.geometry("300x300")
label = tk.Label(window,text="my gui")
label.pack()
entry=tk.entry(window,width=21)
entry.pack()

button = tk.Button(window,text="按我",command = clickme)
button.pack()
window.mainloop()