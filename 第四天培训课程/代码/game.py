#coding:utf-8
import random
'''
猜拳游戏：
每次询问玩家出拳(选择1石头2剪刀3布)，
电脑随机出拳，将玩家和电脑的出拳结果打印出来，
并告知胜负，再询问玩家是否继续游戏。
'''
choDic = {1:"石头",2:"剪刀",3:"布"}
while True:
    #  dic.get(key[,default="默认值"])
    p = int(input('请出拳:1.石头 2.剪刀 3.布'))
    pCho = choDic.get(p,'error')    
    if pCho == 'error':
        print('输入有误，重新来过')
        continue
    #str(a) 转字符串
    c = random.randint(1,3)
    comCho = choDic[c] 
    print('你出的是',pCho)
    print('电脑出的是',comCho)
    re = p-c
    if re==-1 or re==2:
        print('你赢了')
    elif re==0:
        print('平局')
    else:
        print('你输了')
    choose = input('是否继续游戏？Y/N')
    if choose == 'N':
        break
'''
概率问题
生成随机数，判断随机数的范围
1-100  if 1-10  elif 11-50 elif 51-100
'''