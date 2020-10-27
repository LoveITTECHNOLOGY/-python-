#coding:utf-8
#运算符 +-* 与普通运算一致
a,b,c = 2,4,5 #可以同时赋值
# 除法  / 得到浮点型    |    //得到整数部分
print(c/a)
print(c//a)
#  %取余    |   a**b   a的b次方
print(a**c)
# m=28 n=12 只用m和n，把m和n的值互换
m,n = 28,12
m = m+n 
n = m-n  # 此时n的值就是28
m = m-n  
#快速排序(递归)     冒泡排序