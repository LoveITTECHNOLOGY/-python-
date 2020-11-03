#coding:utf-8
import pickle
#反序列化,其实就是读取文件
f = open('fa.txt','rb') #二进制读
#load(文件)
#如果一个文件中序列化了多个对象,可以按顺序反序列化出来
for i in range(2):
    a = pickle.load(f)
    print(a)
'''
a = pickle.load(f) #如果文件为空，会报错
#print(type(a))
print(a)
'''
f.close()