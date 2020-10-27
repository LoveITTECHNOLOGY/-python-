#coding:utf-8
'''
学生成绩录入系统
'''
print('---欢迎来到XXX学生成绩管理系统---')
stuList = ['zhangsan','lisi']
stuScore = [60,70]
#input()
print('请输入你的操作：')
choose = int(input('1.查看所有学生成绩  '\
               '2.修改学生成绩 3.添加学生成绩 '\
               '4.删除学生成绩'))
#print(type(choose))
#     for i in stuList:
#         indexS = stuList.index(i)
#         print(i,'的成绩为',stuScore[indexS])
      #for i in range(n): 循环，从0到(n-1) 
if choose == 1:
    for i in range(len(stuList)):
        print(stuList[i],'的成绩为',stuScore[i])
elif choose == 2:
    for i in range(len(stuList)):
        print(stuList[i],'的成绩为',stuScore[i])
    cho = input('请选择要修改的学生姓名:')
    scor = int(input('请输入修改后的成绩'))
    ind = stuList.index(cho)
    stuScore[ind] = scor
    for i in range(len(stuList)):
          print(stuList[i],'的成绩为',stuScore[i])    
