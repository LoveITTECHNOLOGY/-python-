#coding:utf-8
from turtle import *
#设置画布的大小和初识位置
#setup(宽，高，横坐标，纵坐标) 默认位置是屏幕中央
setup(800,600)
#设置画笔的粗细
pensize(10)
#设置画笔的类型
shape('turtle')
#设置画笔的大小
shapesize(1,1,1)
#设置画笔的颜色和填充色
color('yellow','blue')
#设置画笔的初识位置
home()
#设置开始填充的位置
begin_fill()
#forward() 朝着海龟的头的方向移动XX像素
forward(100)
'''
#改变转向
right(120)
forward(100)
right(120)
forward(100)
'''
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
#设置结束填充的位置
end_fill()
#画布会停留在最后
done()