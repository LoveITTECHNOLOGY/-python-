#coding:utf-8
'''
654321
1.   65432  +   1
2.   6543   +   12
3.   654    +   123
'''
num = int(input('请输入一个数'))
re = 0 #存放最后输出的结果
while num>0:
    wei =  num%10  #得到原数据的尾数
    num = (num//10) #原数据减一位
    re  = re*10 + wei
print(re)