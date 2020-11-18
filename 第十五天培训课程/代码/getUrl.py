#coding:utf-8
from requests_html import HTMLSession
def get_url_sel(url,sel):
    #得到一个会话，打开浏览器
    session = HTMLSession()
    #url = 'https://www.baidu.com'
    r = session.get(url)
    #sel = 'a'/ 'img' /'div'
    results = r.html.find(sel)
    urlDic = {} #用来存放链接的名字和链接的地址
    for i in results:
        #print(i)
        #查找文本不为空的a标签
        if i.text !='': 
            #查找链接不为空的
            if len(list(i.absolute_links))!=0:
                #两个条件都满足，就存进字典中
                urlDic[i.text]=list(i.absolute_links)[0]
    #遍历字典的键值对
    for text in urlDic:
        print('%s---%s' %(text,urlDic[text]))
get_url_sel('https://www.runoob.com/','a')      