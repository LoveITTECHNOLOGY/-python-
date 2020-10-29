#coding:utf-8
'''
*******
@*****   用户输入X    for i in range(X)
@@***                  i就是@的数量  2*(X-i)-1
@@@*                            2*3-1

*****
@***
@@*      用户输入3   
找行数与图形数量的关系

x = int(input('请输入行数：'))
for i in range(x):   #i的取值  0到(x-1)
    print('@'*i+'*'*(2*x-2*i-1))
'''

'''
九九乘法表
1X1=1
1X2=2 2X2=4
...
.................9X9=81
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'X',j,'=',i*j,'\t',end='')
    print()



