#coding:utf-8
'''
while True:
    try:
        x = int(input('请输入一个数字:'))
        print(x)
        break
    except ValueError:
        #可以只捕获异常但不做处理
        print('妈耶，这不是数字！')
最后的except语句可以忽略异常的类型，如果忽略了当做通配符处理
可以通过这种方式打印异常，然后再抛出异常

try:
    f = open('母猪的产后护理.txt','r')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print(err)
# except ValueError:
#     print('无法转换为数字类型！')
except:
    print('未知错误！')
    raise   #可以再抛出这个异常
'''
sa = 'Hello'
try:
    int(sa)
#Exception所有的异常都是继承自此类
except Exception as e:
    print(e)