#coding:utf-8
for i in range(1,10):
    # print默认换行   end='' 不换行
    print(i,end='')
print()
for i in range(1,101,3):  #(start,end,step)
    print(i,' ',end='')
print()
for i in ['java','html','python']:
    # 列表、元组、字符串都可以这样遍历
    print(i)
#字典的for循环是循环key值
dic = {'name':'tyy','age':'30'}
for i in dic:
    print(i)