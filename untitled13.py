# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:33:31 2020

@author: ryanl
"""

import turtle
tur = turtle.Turtle()
turtle.setup(500,500)
tur.penup()

tur.goto(-100,100)
tur.pendown()
tur.fillcolor("#750000")
tur.begin_fill()

for i in range(4):
    tur.forward(100)
    tur.right(90)
tur.end_fill()
turtle.done()
turtle.extionclick()            