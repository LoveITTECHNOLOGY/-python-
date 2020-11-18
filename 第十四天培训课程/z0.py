#coding:utf-8
import re
'''
正则表达式：用来做格式的判断
爬取数据：首先获取页面全部内容
爬图片：  <img title="" alt="" src="只要这里" class="">
        <img.*src="()".*title="()".*>
通过正则表达式获取页面中的所有img标签
再获取src中的内容
爬链接： <a href="">百度一下，你就知道</a>
获取href的属性，获取a标签的文本值
文本值-----href的链接
        123456@qq.com
'''

'''
1.re.match(匹配的规则,用于匹配的内容,[匹配的标志符])
从开头开始匹配，有则返回匹配的位置，没有则返回None
2.re.search(参数一致) 在整个内容中寻找，匹配则返回第一次满足要求的位置
3.re.findall(参数一致) 查找所有满足要求的，返回一个list
'''
print(re.match(r'ab','abcd'))
print(re.match(r'ab','babcd'))
print(re.search(r'ab','babcabd'))
print(re.findall(r'ab','babcabd'))


