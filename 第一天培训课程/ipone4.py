#coding:utf-8
from turtle import *
def round_rect(width,height,angle,rad):
    #宽，高，弧度，弧长
    for i in range(2):
        forward(height)
        #circle画圆
        circle(rad,angle)
        forward(width)
        circle(rad,angle)
setup(1300,800,0,0)
pensize(2)
speed(5)
#设置海龟的初始朝向
setheading(90)
shape('square')
pencolor('#F00') #F00红色
penup()
goto(202,-202)
pendown()
round_rect(244,484,90,30)
#设置画笔颜色为黑色
#屏幕
pencolor('#000')
penup()
goto(185,-150)
pendown()
begin_fill()
color('#000')
round_rect(270,380,90,0)
end_fill()
#上面的
penup()
color('#F00')
goto(80,265)
pendown()
begin_fill()
round_rect(60,4,90,0)
end_fill()
#home键
penup()
goto(75,-190)
pendown()
#circle(半径,弧长)
circle(25,360)
hideturtle()
done()
