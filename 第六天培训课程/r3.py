#coding:utf-8
#r+可读可写
f = open('fa.txt','r+')
#执行写操作，如果不改变指针位置，会覆盖原文件内容
f.read()
#write()写入内容
f.write('-----')
f.close()