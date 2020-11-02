#coding:utf-8
import time
'''
写一个方法:
通过输入0-6来得到今天是星期几？
如果参数不为0-6？
'''
def show_date(a):
    return{0:'星期一',
           1:'星期二',
           2:'星期三',
           3:'星期四',
           4:'星期五',
           5:'星期六',
           6:'星期天',
           }.get(a,'时间输入不正确！')
print('今天是 %s' %show_date(time.localtime()[6]))
           