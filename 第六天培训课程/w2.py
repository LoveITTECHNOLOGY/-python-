#coding:utf-8
#使用w+模式打开文件
f = open('ff.txt','w+')
print(f.read())
f.write('html+css')
print(f.tell())
f.seek(0) #写完后指针在最后，要读要改变指针位置
print(f.read())
f.close()