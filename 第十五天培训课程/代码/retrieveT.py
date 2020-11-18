#coding:utf-8
from urllib.request import urlretrieve
import os
def cbk(a,b,c):
    #回调函数  每当有数据被下载就会调用
    '''
    a是已经下载的数据块的数量
    b是每个数据块的大小
    c是文件总大小    c=a*b
    '''
    per = a*b/c*100.0
    if per > 100:
        per = 100
    print('%.2f%%' %per)
#设置路径为当前文件夹下
dir = os.path.abspath('.')
#url = 'http://www.baidu.com'
url = 'https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe'
#下载到本地的文件名
work_path = os.path.join(dir,'python-3.9.0-amd64.exe')
urlretrieve(url,work_path,cbk)