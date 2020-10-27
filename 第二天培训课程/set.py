#coding:utf-8
'''
集合可以存放不同数据类型的对象
可以用来去重、做成员变量的关系检测
集合写在{}中，定义一个空的集合要用set()
{}是定义字典的
'''
stu = {'zhangsan','xiaoming','lisi','tyy','lisi'}
print(stu)
if 'tyy' in stu:
    print('tyy在集合中')
else:
    print('tyy不在集合中')
seta = {} #定义空字典
setb = set() #定义空集合
print(type(seta),type(setb))
a = set('abcdfgnk')
b = set('abcghjk')  
#a-b 差集 只在a中出现的元素
print(a-b)
#a|b 并集
print(a|b)
#a&b 交集
print(a&b)
#a^b 在a、b中不同时出现
print(a^b)