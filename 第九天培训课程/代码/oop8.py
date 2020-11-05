#coding:utf-8
'''
运算符重载:+-*/
'''
class Vetor:
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    def __str__(self):
        #打印对象时会调用的方法
        # v1 = Vetor()   print(v1)
        return 'Vetor(%d,%d)' %(self.a,self.b)
    def __add__(self,other):
        #用对象做加法会调用此方法
        return Vetor(self.a+other.a,self.b+other.b)
v1 = Vetor(2,5)
#print(v1)    
v2 = Vetor(3,1)
v3 = v1 + v2  # Vetor(2+3,5+1)
print(v1+v2)