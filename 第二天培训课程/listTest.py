#coding:utf-8
#对列表的增删改查
names1 = ['zhangsan','lisi','wanger','tyy','lisi']
#遍历列表  类似foreach  查
for i in names1:
    print(i)
#增
names2 = ['timao','yasuo']
#extend() 将另一个列表添加至列表的结尾处
names1.extend(names2)
#print(names1)
#append(obj)  追加  
names1.append('youmi')
#print(names1)
#insert(index,obj) 插入数据
names1.insert(2, 'yongen')
#删
#remove(value)  以元素的值去删除第一个匹配的元素，如果不存在则报错
names1.remove('lisi')
#pop(index)  以下标去删除元素，默认删最后一个，有返回值
#print(names1)
print(names1.pop(4))  #方法(参数列表){方法的内容，是否有返回值}
print(names1)
#查
#index() 查询是否有指定的元素，如果有返回下标，如果没有报错
print(names1.index('yasuo'))
#print(names1.index('yysuo')) 如果不存在此元素会报错
#count() 查询元素出现的次数
print(names1.count('youmi'))
#排序
#按照首字母的顺序排序
names1.sort() #升序
print(names1)
names1.reverse() #降序
print(names1)