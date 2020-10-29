#coding:utf-8
a = int(input('请输入第一个数'))
b = int(input('请输入第二个数'))
c = int(input('请输入第三个数'))
d = int(input('请输入第四个数'))
maxN = a  #假设a为最大的
if b > maxN:
    maxN = b
if c > maxN:
    maxN = c
if d > maxN:
    maxN = d
print('最大值为:',maxN)
'''
max(list) min(list) 得到列表中最值
'''