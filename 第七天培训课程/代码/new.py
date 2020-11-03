#coding:utf-8
import pickle
f = open('user.txt','wb')
dic = {'admin':'admin'}
pickle.dump(dic,f)
f.close()