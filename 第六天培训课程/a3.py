#coding:utf-8
f = open('aaa.txt','a+')
f.seek(0)
print(f.read())
#删除文件内容 ,如果放参数则表示从第X个位置处开始删除内容，不放参数
#则删除全部
f.truncate(6)
f.close()