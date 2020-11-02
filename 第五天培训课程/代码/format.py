#coding:utf-8
#format函数的用法
#同时使用多种格式化，并用字典传参
print('My age is %(a)d,I like %(p)s,I have %(m).2f yuan.'
       %{'a':18,'p':'python','m':6.6666})
'''
对应字符串，新增了str.format() 函数，增强了字符串的格式化功能
'''
#不设置指定位置，按默认顺序传参
print("{} {}".format('hello','world'))
#设置传入参数的位置
print("{1} {0}".format('hello','world'))
#把foramt里的参数当做元组
print("{1} {0} {1} {0}".format('hello','world'))
#设置参数。类似字典  **dic表示字典
dic = {'name':'九江学院','add':'前进东路'}
print("学校名：{name},地址：{add}。".format(**dic))
#还可以传列表作为参数
list = ['九江学院','前进东路']
#0[0]  第一个是指format里的下标为0的参数
print("学校名：{0[0]},地址:{0[1]}".format(list))
