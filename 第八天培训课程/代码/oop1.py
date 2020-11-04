#coding:utf-8
from newClass import * #复制代码
stu = Student('张三',18) #实例化Student
'''
stu = Student('张三',18)
首先调用Student的__new__方法，创建了一个实例
再去调用Student的__init__方法，完成初始化操作
'''
stu.showCount()
stu.showSelf()
stu.showClass()
stu2 = Student('李四',20)
stu.showCount()