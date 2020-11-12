#coding:utf-8
from orac_con import *
import cx_Oracle
#带参数的语句  username=:attrs
#             字段        :自己取的
sql = 'select * from X_USER where username=:name'
pr = {'name':'admin'} #用字典传参
#cr.execute(sql,pr) #execute(sql,参数)
cr.execute(sql,name='tyy0414') #直接写参数
rs = cr.fetchall()
print('查询结果为%s' %rs)
cr.close()
db.close()
