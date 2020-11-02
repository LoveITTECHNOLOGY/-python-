#coding:utf-8
#以a模式打开文件，如果不存在会新建文件，如果存在则追加
f = open('aaa.txt','a')
#会在文件结尾追加内容
f.write('apythona')
#print(f.read())
f.close()