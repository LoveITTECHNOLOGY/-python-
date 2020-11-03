#coding:utf-8
import pickle
f = open('user.txt','ab+')#二进制可读可写
f.seek(0)
dic = pickle.load(f) #存储的是用户的信息
print(dic)
f.close()
cho = input('请输入你的操作:1.登录 2.注册')
if cho == '1':
    userName = input('请输入用户名:')
    if userName in dic:
        userPsw = input('请输入密码:')
        if dic[userName]==userPsw:
            print('登录成功')
        else:
            print('密码错误')
    else:
        print('账号不存在')
elif cho == '2':
    userName = input('请输入账号:')
    #用户名如果存在，注册失败
    userPsw = input('请输入密码:')
    dic[userName] = userPsw
    print('注册成功')
    f = open('user.txt','wb') #文件中只存用户账户密码的字典
    pickle.dump(dic,f)
    f.close()