#coding:utf-8
import urllib
import urllib.request
import re
#写一个获取html内容的方法
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('gbk')
    return html
def getImg(html):
    #写一个获取img中src值的规则
    #   <img xxx xxx  src="(xxx.jpg xxx.png)" xx xxx>
    #print(html)
    patt = r'<img.*?src="(.*?)"'
    imgPatt = re.compile(patt)
    imgList = re.findall(patt,html)
    x = 0 #用来当做文件名
    for imgUrl in imgList:
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
getImg(getHtml('http://www.jj20.com/bz/ktmh/list_16_5.html'))