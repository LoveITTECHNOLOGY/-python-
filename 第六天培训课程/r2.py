#coding:utf-8
f = open('fa.txt','r')
#readline() 读文件的一行  read() 读文件以字节数为参数，不给则为全部文件
#在读取文件时指针一直在移动
print(f.readline())
#f.tell() 得到指针位置
print(f.tell())
print(f.readline())
print(f.read())
#执行完read后，指针在最后，无法再读文件
#f.seek(index) 改变指针位置
f.seek(10)
print('======')
print(f.read())
#file.write() 写入文件
#f.write('aa') 无法写入
f.close()