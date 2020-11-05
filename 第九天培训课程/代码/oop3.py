#coding:utf-8
from newClass import *
#Python的内置类属性
#类的文档字符串
print('Student.__doc__:%s' %Student.__doc__)
#类名
print('Student.__name__:%s' %Student.__name__)
#类定义所在的模块
#JAVA中类名就是文件名，python中类可以只是模块中的一部分
print('Student.__module__:%s' %Student.__module__)
#类的所有父类组成的元组
print('Student.__bases__:%s' %Student.__bases__)
#类的属性组成的字典
print('Student.__dict__:%s' %Student.__dict__)