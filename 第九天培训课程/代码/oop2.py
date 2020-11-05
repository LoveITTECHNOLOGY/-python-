#coding:utf-8
from newClass import *
'''
如何实现无参构造函数??
stu1 = Student() #不放参数的实例化
print(stu1.name)
print(stu1.age)
'''
stu1 = Student('Tom',18)
stu2 = Student('Jerry',20)
#python中__XXX__一般是用特殊用法的属性或方法
print(Student.__doc__)#得到类的文档字符串
#访问对象的属性和方法，通过 . 来访问
stu1.showSelf()
stu2.showSelf()
#类变量，通过类名访问
print('总学生数为:%d' %Student.stuCount)
#添加，删除，修改类的属性
stu1.stuNo = 10000 #添加一个学号stuNo属性
print('学生的学号为:%d' %stu1.stuNo)
stu1.stuNo = 10001 #修改对象的属性
#del stu1.stuNo #删除对象的属性
#print('学生的学号为:%d' %stu1.stuNo)
'''
通过函数的方式访问属性：
getattr:得到属性
hasattr:判断是否有某个属性
srtattr:设置属性值
delattr:删除属性
'''
#hasattr(obj,attr) 返回True False
print(hasattr(stu1,'stuNo'))
#getattr(obj,attr) 返回属性值
print(getattr(stu1,'stuNo'))
#setattr(obj,attr,value)
setattr(stu1,'stuNo',10002)
print(getattr(stu1,'stuNo'))
#delattr(obj,attr)
delattr(stu1,'stuNo')