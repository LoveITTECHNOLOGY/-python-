#coding:utf-8
import math
#math.pi 就是圆周率  %f指的是浮点数 默认保留6位小数 
print('打印浮点数圆周率PI=%f' %math.pi)
#指定打印的小数位数
print('保留三位小数PI=%.3f' %math.pi)
#指定占位符的宽度，输出数据占9位，小数点也算一位，不足的在前面补空格
print('输出数据占9位PI=%9f' %math.pi)
#输出6位数据，小数点后两位
print('输出数据占6位，小数点后2位PI=%6.2fPI=%6.2f' %(math.pi,math.pi))
#使用 - 号控制对齐方式  %-6.2f 指的是左对齐
print('输出数据左对齐PI=%-6.2fPI=%-6.2f' %(math.pi,math.pi))
#不足的位数补0   0X.  小数点后不显示数据，不够位数补0
print('小数点后不显示数据，不够7位补0,PI=%07.f' %math.pi)
#结合使用
print('数据占6位，小数点后保留3位，PI=%0*.*f' %(6,3,math.pi))