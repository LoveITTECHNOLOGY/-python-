#coding:utf-8
def mul(a,b):
    if a<b:
        #raise可以主动抛出一个异常
        raise BaseException('被减数不能小于减数！')
    else:
        return a-b
try:
    print(mul(1,2))
    print('try中最后的语句！')
except BaseException as e:
    print(e)
finally:
    print('finally中的语句')
print('-----------------')
sa = 'Hello'
try:
    int(sa)
except IndexError as e:#下标异常
    print('1',e)
except KeyError as e:#字典不存在key值异常
    print('2',e)
except ValueError as e:#值异常
    print('3',e)
else:
    print('没毛病')
finally:
    print('finally')