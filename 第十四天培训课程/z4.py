#coding:utf-8
import re
'''
常用正则表达式的匹配符号
\D 非数字
\d 数字
'''
#\W 非字母数字下滑线 ,\w字母数字下滑线
print(re.findall(r'\W','abcd123!@#_'))
print(re.findall(r'\w','abcd123!@#_'))
#\S 非空字符  \s空白
print(re.findall(r'\S','a b c d'))
print(re.findall(r'\s','a b c d'))
#\b必须与其他字符组成单词   \B不能与其他字符组成单词
#\B只能单独存在       \b不能单独存在
print(re.findall(r'\Bab','ab abc dabc'))
print(re.findall(r'\bab','ab abc dabc'))
