#coding:utf-8
import pickle
#序列化,其实是写操作
f = open('fa.txt','wb') #二进制写
dic = {'1':'a','2':'b',3:'c'}
#dump(对象,文件)
pickle.dump(dic,f)
f.close()
 