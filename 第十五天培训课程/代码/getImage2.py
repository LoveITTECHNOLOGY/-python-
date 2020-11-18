#coding:utf-8
#模拟浏览器创建会话的对象
from requests_html import HTMLSession
import urllib
import urllib.request
import re
def getUrlImg(url):
    #建立一个会话
    session = HTMLSession()
    session.headers.update()
    #得到响应对象
    resp = session.get(url)
    '''
    resp.html 得到html内容
    resp.html.text  得到text值
    resp.html.links
    resp.html.absolute_links
    '''
    sel = 'img' #要选择的标签
    #resp.html.find(标签名) 在页面中查找标签
    results = resp.html.find(sel)
    '''
    res = resp.html.find() 
        得到页面中所有符合条件的元素组成的列表
       得到的元素的所有属性形成一个attr字典
       通过attr[attrName]得到相应的属性值   
    res[index].attrs['src']
    
    '''
    x = 0
    for img in results:
        try:
            imgUrl = img.attrs['src']
        except:
            #print('没有SRC属性！')
            pass
        else:
            if not 'http:' in imgUrl:
                if not 'https:' in imgUrl:
                    imgUrl ='https:' + imgUrl
            # imgUrl = 'https://xxxxx'
            print(imgUrl)
            try:
                resp = urllib.request.urlopen(imgUrl)
            except:
                print('路径打不开！')
            else:
                respImg = resp.read()
                #写一个获取文件名后缀的正则
                fileLast = re.findall(r'.*\.(.*)',imgUrl)[0]
                #打开确定的一个文件
                fileName = r'C:\Users\Administrator\Desktop\PythonImg\%d.%s' %(x,fileLast)
                #打开一个用于存放图片的文件
                picFile = open(fileName,'wb')
                picFile.write(respImg)
                picFile.close()
                x += 1
getUrlImg('http://www.jj20.com/bz/ktmh/list_16_5.html')