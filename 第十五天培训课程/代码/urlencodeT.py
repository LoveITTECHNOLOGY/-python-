#coding:utf-8
import urllib.parse
dic = {'name':'tyy','psw':'123'}
data = urllib.parse.urlencode(dic)
print(data)