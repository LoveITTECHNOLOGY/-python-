#coding:utf-8
import urllib.request
import urllib.parse
dic = {'page':'2'}
data = urllib.parse.urlencode(dic)
req = urllib.request.Request('http://localhost:8087/showGoods.do',data.encode())
resp = urllib.request.urlopen(req)
content = resp.read().decode()
print(content)


