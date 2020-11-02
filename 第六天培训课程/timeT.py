#coding:utf-8
import time
'''
表现time的两种形式
1.时间戳方式：表示的是1970年1月1日00:00:00至今的秒数
的偏移量
2.元组（struct_time）方式:struct_time有九个元素，分别
表示时间相关的参数，格式化得时间字符串
'''
#time.time()至今的秒数
print('当前的时间数值为%f' %time.time())
'''
localtime()得到本地时间，转换为计算机能够识别的时间格式
以元组形式存放
tm_year 年
tm_mon  月
tm_mday 日
tm_hour 时
tm_min  分
tm_sec  秒
tm_wday 0-6 周一-周日
tm_yday 一年中的第几天
tm_isdst 是否为夏令时节 但是中国没有   1是 0否 -1不详
'''
print(time.localtime())
#time.gmtime() 将一个时间戳转换为伦敦的时间UTC时区的一个struct_time
print(time.gmtime())
#time.mktime() 参数是struct_time,得到时间戳格式
t=(2020,11,1,8,0,0,6,306,0)
print(time.mktime(t))
print(time.mktime(time.localtime()))
#time.asctime() 可以把struct_time转换为固定的时间格式输出
print(time.asctime(t))
print(time.asctime(time.localtime()))
#ctime() 把一个秒数计算的浮点数(时间戳)作为参数，得到一个asctime
#如果不给参数则以当前时间
print(time.ctime())
print(time.ctime(1604188800))
print('-----------')
#time.sleep() 让程序睡眠，单位为秒
def sleep_time():
    print(time.ctime())
    time.sleep(5)
    print(time.ctime())
sleep_time()




