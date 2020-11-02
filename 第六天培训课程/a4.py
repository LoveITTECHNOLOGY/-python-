#coding:utf-8
'''
相对路径：相对当前文件所在路径。   ../往上回退一级菜单
绝对路径：相对盘符而言                    D://dic1//dic2//
'''
'''
f = open('../a.txt','a+')
f.write('abcdefg')
f.close()
'''
for i in range(5):
    f = open('D://app//'+str(i)+'.txt','a+')
    f.write('abcdefg')
    f.close()