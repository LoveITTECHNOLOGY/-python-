#coding:utf-8
#a+可读可写的追加写，a+模式的指针在结尾，如果要读文件，要改变指针位置
f = open('aaa.txt','a+')
f.seek(0) #把指针放在文件开头
print(f.read())
f.close()