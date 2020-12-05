# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:20:35 2020

@author: ryanl
"""

import turtle
tur = turtle.Turtle()
turtle.setup(500,500)
def rectangle():
    tur.forward(100)
    tur.right(90)
    tur.forward(50)
    tur.right(90)
    tur.forward(100)
    tur.right(90)
    tur.forward(50)
    tur.right(90)
tur.penup()
tur.goto(-400,400)
tur.fillcolor(0,0,0)   
tur.begin_fill()
rectangle() 
tur.end_fill()
tur.penup()
tur.goto(-400,350)
tur.fillcolor(1,0,0)   
tur.begin_fill()
rectangle() 
tur.end_fill()
tur.penup()
tur.goto(-400,300)
tur.fillcolor(1,1,0)   
tur.begin_fill()
rectangle() 
tur.end_fill()
turtle.done()
turtle.extionclick() 