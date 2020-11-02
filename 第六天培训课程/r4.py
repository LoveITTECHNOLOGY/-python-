#coding:utf-8
f = open('fa.txt','rb')
print(f.readline())
print(f.tell())
#seek(偏移量-负数代表向前偏移,偏移的位置 0开头1当前位置2文件结尾)
#seek()函数只有b模式才可以使用12，否则只能用0
f.seek(-2,2)
print(f.tell())
f.close()