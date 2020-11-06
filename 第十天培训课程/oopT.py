#coding:utf-8
import random
'''
对应对象.属性的操作，会使得设置属性时无法去判断属性的
类型或者是范围，会造成未知的错误
'''
'''
#情况1   会有各种错误发生
class Student:
    pass
s1 = Student()
#可以直接附属性值
s1.score = 'aaa'
print('学生成绩为:',s1.score)
'''
'''
#情况2 自己设置setter和getter方法
class Student:
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('分数必须为整数！')
        if score<0 or score>100:
            raise ValueError('分数必须在0-100之间！')
        self.__score = score
    def get_score(self):
        return self.__score
s1 = Student()
#设置和得到属性都要自己定义方法名
s1.set_score(90)
print('学生分数为:%d' %s1.get_score())
'''
#情况3 使用自带的@property
class Student:
    def __init__(self):
        self.__score = 0
    @property
    def score(self):
        return self.__score
    #如果不设置setter方法，则属性为只读
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('分数必须为整数！')
        if score<0 or score>100:
            raise ValueError('分数必须在0-100之间！')
        self.__score = score
    @score.deleter
    def score(self):  #在调用 del obj.attrs时会调用
        print('属性被删除！')
    def exam(self):
        self.__score = random.randint(0,100)
s1 = Student()
# s1.exam()
# print('学生成绩为:%d' %s1.score)
s1.score = 99
print('学生成绩为:%d' %s1.score)
del s1.score