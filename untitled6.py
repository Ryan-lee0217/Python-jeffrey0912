# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:24:58 2020

@author: ryanl
"""

from pytube import Youtube
progress=0
def progress(sream,chunk,bytes_remaining):
        size=stream.filesize
        global progress
        preprogress=progress
        currentprogress=int((size-bytes remaining)*100/size)
        progress=currentprogress
        if preprogress!-progress:
         print("目前進度:"+str(currentprogress)+"%")
        if preprogress==100
            print("下載完成")
        




        
yt = YouTube("https://www.youtube.com/watch?v=9ZrAYxWPN6c&list=RD9ZrAYxWPN6c&start_radio=1")
stream = yt.streams.first()
stream.download('C:\\Users\\ryanl\\OneDrive\\桌面\AE402',"sound de la police")