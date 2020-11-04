#coding:utf-8
import pickle
# list = [{'name':'tyy','psw':'123','exp':'100','hp':100},{},{}]
dic = {'tyy':'123','qwe':'123'} #初始化一个保存用户信息的字典
try:
    f = open('user.txt','rb')
    dic = pickle.load(f)
    f.close()
except Exception as e:
    print(e)
while True:
    cho = input('请输入你的操作:1.登录 2.注册')
    if cho =='1':
        if len(dic)==0:
            print('暂无用户,请先注册！')
            continue
        else:
            userName = input('请输入账号:')
            if userName not in dic:
                print('账号不存在！')
                continue
            else:
                userPsw = input('请输入密码:')
                if dic[userName] == userPsw:
                    print('登录成功！')
                else:
                    print('密码错误！')
    elif cho == '2':
        userName = input('请输入账号:')
        if userName in dic:
            print('账号已存在！')
            continue
        else:
            userPsw = input('请输入密码:')
            dic[userName] = userPsw
            f = open('user.txt','wb')
            pickle.dump(dic,f)
            f.close()
