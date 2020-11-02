#coding:utf-8
#字符串常用方法
#python中字符串时用'' 或者"" 包含的变量
# 输出 I don\'t know.    \转义符
print('I don\\\'t konw')
#\n 换行符
#字符串可以通过下标进行查询
strA = 'tuyy@seecen.com'
print('字符串的长度为%d。' %len(strA))
print('字符串strA[2]=%s。' %strA[2] )
print('字符串strA[-2]=%s。' %strA[-2] )
print('字符串strA[2:5]=%s。' %strA[2:5] )
print('字符串strA[2:]=%s。' %strA[2:] )