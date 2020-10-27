#coding:utf-8
'''
Python中字符串用单引号或双引号括起来
\ 转义符       \n 换行
'''
str = 'happy'
print(str)
#str[index] 可以通过下标获取某个字符
print(str[3])
#字符串是不可变数据类型  
#str[1] = 'm'  报错
print(str[0:3])  #获取某些字符 ，左闭右开
#还可以反着来
print(str[0:-1])
#不指定最后一个 ,取到最后
print(str[2:])
# str*2
print(str*2)
# 字符串的加法就是做字符串拼接
# \n 换行符    如果要打印\  需要加一个\ 
str1 = 'eve\ning'
print(str1)
print(r'eve\ning')  # r'str'  打印字符串本身，不转义
# \ 续行符   换行的内容会在同一行出现
# 续行符后不能出现其他字符
print('a'\
      'b'\
      'sss')
