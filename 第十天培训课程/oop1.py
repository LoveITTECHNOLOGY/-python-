#coding:utf-8
'''
Python除了可以自己定义方法去访问属性
还支持@property去操作属性
'''
class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    #访问器 --getter方法
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    #修改器 --setter方法
    @age.setter   #前面要先设置了@property
    def age(self,age):
        self.__age = age
    
p1 = Person('张三',18)
print('名字是:%s' %p1.name)
print('年龄是:%s' %p1.age)
p1.age = 'aa'
print('年龄是:%s' %p1.age)
        