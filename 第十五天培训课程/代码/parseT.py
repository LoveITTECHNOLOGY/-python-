#coding:utf-8
import urllib.parse
import urllib.request
url = 'http://www.baidu.com'
parsed = urllib.parse.urlparse(url)
print(parsed)
'''
scheme 协议
netloc 域名
path 路径
params 参数
query 查询
fragment 用来判断
'''