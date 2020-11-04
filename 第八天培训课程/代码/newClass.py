#coding:utf-8
class Student:
    '学生的基础类'  #类文档字符串，类的一个简单的说明
    stuCount = 0   #类变量，归类所有，在实例间共享
    '''
    __new__至少要有一个参数cls，代表要实例化的类
    此参数在实例化时由Python解析器自动提供
    __new__方法必须有返回值，返回实例化出来的对象
    可以返回父类的实例，或者直接返回Object实例
    '''
    def __new__(cls,name,age):
        print('__new__')
        obj = object.__new__(cls) #obj就是Student实例
        print(obj)
        return obj
    '''
       构造函数：在实例化的时候一定会调用的方法
    要放一个默认参数self，代指对象本身
    self不是Python关键字，可以换
    self不用主动放参数，自动放
    '''
    def __init__(self,name,age):
        print('__init__')
        #this.name = name
        #self.attr  是实例变量(属性)
        self.name = name
        self.age = age
        #让类变量stuCount自增
        Student.stuCount +=1
    #普通方法
    def showCount(self):
        print('学生总人数为%d人.' %Student.stuCount)
    def showSelf(self):
        print('我叫%s,我今年%d岁.' %(self.name,self.age))
    def showClass(self):
        print(self)
        print(self.__class__)