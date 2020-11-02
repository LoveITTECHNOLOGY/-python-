#coding:utf-8
#整数的格式化输出
num = 14
#正常输出整型
print('num=%d' %num)
'''
%d %i %u都可以表示整数
%o 八进制
%x 十六进制
'''
print('%d,%i,%u' %(num,num,num))
print('%o,%x' %(num,num))
#整数的位数为1位，但是原数据超过1位时，按原数据输出
print('num=%1d' %num)
#如果原数据不足要显示的位数,补空格
print('num=%7d' %num)
#-表示左对齐(向后面补空格)
print('num=%-7d' %num)
#如果原数据位数不够，也可以补0
print('num=%07d' %num)
#取数据的前三位，如果不够，在前面补0
print('num=%.3d' %num)
# %x.y  当整数不够y位时，优先补0，但是不够x位，会在左侧补空格
print('num=%5.3d' %num)
print('num=%*.*d' %(6,4,num))