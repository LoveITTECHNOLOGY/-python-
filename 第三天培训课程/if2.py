#coding:utf-8
#创建一个存放账号密码的字典
userDic = {'admin':'admin','aaa':'bbb'}
#userDic[newKey]=newValue
userName = input('请输入账号:')
#标识符
isExist=False  #默认账号不存在  布尔类型的值命名 isXXX
for i in userDic:  #循环的是key值
    if i==userName:
        isExist=True
    else:
        pass  #过
if isExist:
    passWord = input('请输入密码:')
    if userDic[userName]==passWord:
        print('登录成功')
    else:
        print('密码错误')
else:
    print('账号不存在')
    