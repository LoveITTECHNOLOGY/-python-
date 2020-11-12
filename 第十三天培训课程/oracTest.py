#coding:utf-8
import cx_Oracle
#创建连接
#cx_Oracle.connect(账号/密码@端口号/数据源) 
#db=cx_Oracle.connect('xm','111111','localhost:1521/xe')
db = cx_Oracle.connect('xm/111111@localhost:1521/xe')
print(db)
db.close()
