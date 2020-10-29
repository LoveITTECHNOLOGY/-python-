#coding:utf-8
import random #随机数模块
'''
随机生成4个有顺序的数(0-9)，让用户猜，
提示用户有几个数字位置和数值都对了
有几个只有数字对了，位置不对
'''
#a = random.randint(0,9)  #随机生成整数 两边都能等
list = [] #定义随机生成四个数的列表
while len(list)!=4:
    a = random.randint(0,9)
    if a not in list:
        list.append(a)
print(list)
num = input('请输入你猜的数字:') #四位数字的字符串
ulist = []  #存放用户猜的四个数字
for i in num:
    ulist.append(int(i))
print(ulist)
#count数值有几个正确
countAll = 0 #计数
for i in list:
    if i in ulist:
        countAll+=1
    

    



