#coding:utf-8
'''
python中没有switch
自己写一个swicth  使用函数和字典
swicth()   放入1-7得到周一-周日
'''
def swDate(a):
    dic = {1:'周一',
           2:'周二',
           3:'周三',
           4:'周四',
           5:'周五',
           6:'周六',
           7:'周日',
    }
    return dic.get(a,'参数不正确')
print(swDate(7))