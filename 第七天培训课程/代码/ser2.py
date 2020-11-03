#coding:utf-8
import pickle
f = open('fa.txt','ab')#追加写模式
#序列化也是写操作，只是写的是二进制形式
dic = {'111':'aaa','222':'bbb',333:'ccc'}
pickle.dump(dic,f)
f.close()