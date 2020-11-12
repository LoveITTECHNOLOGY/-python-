#coding:utf-8
import cx_Oracle
from orac_con import *
pr = {'name':'tyy4141'}
sql  = 'delete from X_USER where username=:name'
cr.execute(sql,pr)
#增删改，要提交事务
cr.close()
db.commit()#提交
db.close()