#coding:utf-8
#列表 可以存放不同数据类型的变量
list = ['java',3.14,'python',999,666]
alist = ['c#','html',333]
list[1] = 3.1415  #列表中的元素可以被修改
print(list)
print(list[1])
print(list[1:4])
print(list[2:])
print(list*2)
#python中列表可以拼接
nlist = list + alist
print(nlist)
#截取列表的元素还可以设置步长
print(nlist[1:6])
print(nlist[1:6:2])  #[start:end:step]
print(nlist[-1::-2])  #反着取，步长也要为负数