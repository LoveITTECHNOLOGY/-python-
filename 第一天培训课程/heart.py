#coding:utf-8
from turtle import *
setup(800,600,200,100)
color('red','pink')
speed(9)
shape('circle')
shapesize(1,1,1)
begin_fill()
left(140)
forward(112)
#画圆
# for i in range(360):
#     right(1)
#     forward(1)
for i in range(200):
    right(1)
    forward(1)
left(120)
for i in range(200):
    right(1)
    forward(1)
forward(112)
end_fill()
penup()
goto(450,260)
pendown()
begin_fill()
left(140)
forward(112)
for i in range(200):
    right(1)
    forward(1)
left(120)
for i in range(200):
    right(1)
    forward(1)
forward(112)
end_fill()
done()