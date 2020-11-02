#coding:utf-8
'''
ASCII码
'''
#可以将字符串改为元组或者列表输出
la = 'python'
print(tuple(la))
print(list(la))
#ord() 得到字符对应的ASCII码
print(ord('中'))
print(ord('a'))
#chr() 根据ASCII码得到相应字符
print(chr(20013))
print(chr(65))
#判断字符串中是否包含某个字符
print(la.index('t'))
print('y' in la)
strB = '  aaBcDd  '
print(strB.strip()) #去字符串首尾的空格
strC = '12hdify934!!'
print(strC.isalpha()) #判断字符是否是纯字母
print(strB.upper())  #转大写
print(strB.lower())  #转小写
strD = 'm|n|a|b|c'
print(strD.split('|')) #以某字符分割字符串转换为列表
print(strD.split('|')[3]) #取出某个元素
#判断是否为纯大写/纯小写
print(la.isupper()) 
print(la.islower()) 