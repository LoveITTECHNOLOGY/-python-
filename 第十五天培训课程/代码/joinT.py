#coding:utf-8
import urllib.parse
url = 'http://www.baidu.com'
new_path = urllib.parse.urljoin(url,'index.html')
print(new_path)