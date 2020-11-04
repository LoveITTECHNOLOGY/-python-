#coding:utf-8
import traceback
try:
    print(5/0)
except (TypeError,ZeroDivisionError) as e:
    traceback.print_exc() #打印堆栈信息
    print(e)
else:
    print('没错误！')