import time
import datetime
import turtle
tur = turtle.Turtle()
tur.penup()
tur.goto(0,-200)
tur.pendown()
tur.begin_fill()
tur.fillcolor(0,1,1)
tur.circle(200)
tur.end_fill()
tur.penup()
tur.goto(0,0)
def minute(num):
    tur.penup()
    tur.forward(200)
    tur.write(num,font=("courier",12,"bold"))
    tur.back(200)
    tur.pendown()
tur.seth(90)
for j in range(1,60):
    tur.right(6)
    if j%5!=0:
        minute(".")
tur.seth(90) 
for k in range(1,13):
    tur.right(30)
    tur.penup()
    tur.forward(185)
    tur.pendown()
    tur.forward(15)
    tur.penup()
    tur.back(200)
    tur.pendown()
    
           
    
    
    
    
    
def writenum(num):
    tur.penup()    
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()
tur.seth(98)
for i in range(1,13):
    tur.right(30)
    writenum(i)
update=True
updatesecond=True

while True:
    now=datetime.datetime.now()
    h=now.hour%12
    m=now.minute
    s=now.second
    if update:
        hour=turtle.Turtle()
        hour.seth(90)
        hour.right(h*30+m/60*30)
        hour.forward(100)
        
        minute=turtle.Turtle()
        minute.seth(90)
        minute.right(m*6)
        minute.forward(150)
        update=False
        
    if updatesecond:
        second=turtle.Turtle()
        second.seth(90)
        second.right(s*6)
        second.forward(180)
        updatesecond=False
    time.sleep(1)
    newm=datetime.datetime.now()  
    nm=newm.minute
    updatesecond=True
    second.clear()
    second.reset()
    if nm!=m:
       update=True
       hour.clear()
       hour.reset()
       minute.clear()
       minute.reset()
    
        
        
        
        
turtle.done()
turtle.exitonclick()