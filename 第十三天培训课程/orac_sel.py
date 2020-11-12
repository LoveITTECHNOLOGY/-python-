#coding:utf-8
import cx_Oracle
#建立连接
db = cx_Oracle.connect('xm/111111@localhost:1521/xe')
#创建游标
cr = db.cursor()
#写sql语句
sql = 'select * from X_USER'
#执行语句
cr.execute(sql)
#得到结果集
rs = cr.fetchall()
print('结果集为(%s)' %rs)
#分条查询
#执行语句
cr.execute(sql)
while True:
    rs = cr.fetchone()
    if rs==None:
        break
    print(rs)
cr.close()
db.close()