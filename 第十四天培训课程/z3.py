#coding:utf-8
import re 
'''
组的概念：
模式字符串的规则都会去进行查找，
但是只有小括号中的内容会被获取，
每次获取的字符形成一个元组，小括号中的内容就是元组的元素
'''
str = 'aa11aa,bb22bb,cc33,dd44dd,ee55ff'
#查找 :字母数字字母  但是我只获取字母
#print(re.findall(r'([a-z]+)(\d+)[a-z]+',str))
strList = re.findall(r'([a-z]+)(\d+)[a-z]+',str)
#print(strList[0][0]) 通过python数据类型的特点去获取其中的元素
# 正则规则像函数一样存储起来重复使用
# ?P<name>规则     ?P<n1>[a-z]    ?P=n1 相当于写了[a-z]
st = re.findall(r'(?P<n1>[a-z]+)\d+(?P=n1)',str)
#re.search()结合?P<name>可以指定输出某些name的字符串
#以字典的形式输出   name:匹配的字符串
str2 = '360103199104150730'
res = re.search(r'(?P<province>\d{2})(?P<city>\d{2})\d{2}(?P<year>\d{4})\d{8}',str2)
#匹配到的字符串的  groupdict()  把得到的字符串通过字典形式输出
print(res.groupdict())
'''
re.compile方法，可以将正则表达式的字符串编译为Pattern对象
从而重复使用这个规则
'''
rule = r'([a-z]+)\d+([a-z]+)'  #此时只是字符串
compile_rule = re.compile(rule) #编译为Pattern对象
print(type(compile_rule))
#Pattern才有macth\search\findall方法
#re.findall(pattern,str)
print(compile_rule.findall(str))