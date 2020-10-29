#coding:utf-8
x = float(input('请输入横坐标：'))
y = float(input('请输入纵坐标：'))
if x==0 and y==0:
    print('在原点')
elif x==0 and y!=0:
    print('在Y轴上')
elif x!=0 and y==0:
    print('在X轴上')
elif x<0:
    if y<0:
        print('第三象限')
    else:
        print('第二象限')
elif x>0:
    if y<0:
        print('第四象限')
    else:
        print('第一象限') 
        