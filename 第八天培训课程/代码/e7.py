#coding:utf-8
class FError(Exception):
    pass #没有特殊属性和方法，但是继承自Exception
try:
    raise FError('自定义异常！')
except FError as e:
    print(e)