#coding:utf-8
#以只读形式打开文件，文件必须已存在
f = open('fa.txt','r',encoding='gbk')
#file.name文件名属性
print('文件名为%s' %f.name)
#file.mode 文件的打开方式
print('文件的打开方式为%s' %f.mode)
#file.closed 如果文件已关闭返回true，未关闭返回false
print(f.closed)
#close()刷新缓冲区的任何还未写入的信息，并关闭该文件
f.close()
print(f.closed)