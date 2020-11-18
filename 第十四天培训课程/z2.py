#coding:utf-8
import re 
'''
re.sub() 用于替换字符串中的匹配项
re.sub(pattern,repl,string,count=0,flags=0)
pattern:正则中的模式字符串
repl:把匹配的替换成此字符串
string:用于匹配的字符串
count:替换的次数，默认为0即所有都替换
'''
phone = '2004-959-558 #这是一个外国的电话号码'
#删除phone中的注释部分
num1 = re.sub(r'#.*$','',phone) 
print('电话号码为:%s' %num1)
#把num1中非数字替换掉   \D为非数字  \d数字
num2 = re.sub(r'\D','',num1)
print('电话号码为:%s' %num2)
#count参数，设置替换的次数
str = 'aabbccddaabbcc'
#把a替换为数字1  sub(规则,替换的字符,用于匹配的字符,替换的次数)
print(re.sub(r'a','1',str,2))