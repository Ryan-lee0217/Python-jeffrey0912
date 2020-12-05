# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:57:01 2020

@author: ryanl
"""
import tkinter as tk

window = tk.Tk()
def onClick():
    global var
    var.set(entry.get())
progress=0    
def progress(sream,chunk,bytes_remaining):
        size=stream.filesize
        global progress
        preprogress=progress
        currentprogress=int((size-bytes remaining)*100/size)
        progress=currentprogress
        if preprogress!-progress:
         print("目前進度:"+str(currentprogress)+"%")
        if preprogress==100:
    yt = YouTube(var.get(),on_progress_callback=showProgress)
    stream = yt.streams.first()
    stream.download('C:\\Users\\ryanl\\OneDrive\\桌面\AE402',"sound de la police")
window.title("scale尺度")
label = tk.Label(window,text="輸入")
label.pack()
var = tk.stringVar
entry=tk.Entry(window,width=21)
entry.pack()
button = tk.Button(window,text="按我")
button.pack()
scale = tk.Scale(window,label="進度條",orient=tk.HORIZONTAL,length=200)
scale.pack()
window.mainloop()
 