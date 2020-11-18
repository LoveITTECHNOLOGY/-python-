#coding:utf-8
import urllib.request
import urllib.parse
#get请求与普通访问方式一样，直接拼接参数
dic = {'page':'3'}
data = urllib.parse.urlencode(dic)
#url = 'http://localhost:8087/xxx.do'
resp = urllib.request.urlopen('http://localhost:8087/showGoods.do?%s' %data)
content = resp.read().decode()
print(content)