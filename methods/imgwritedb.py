from methods.imgreaddb import *
import pymysql
from methods.setdb import imagconnect


def insertinfo(table,stuname,stuid,imagedata):
    loginconnect = imagconnect    #连接数据库服务器
		
    loginconn = loginconnect.cursor()        #创建操作游标
    print("start insert data into mysql!")
    id=select_maxid(table)+1
    sql_insert="INSERT INTO "+table+"(id,stuname,stuid,imagedata) VALUES("+str(id)+",'"+stuname+"','"+stuid+"','"+imagedata+"')"
    loginconn.execute(sql_insert)
    loginconnect.commit()
    print("successfully")

def deleteinfo(table,stuid):
    loginconnect = imagconnect    #连接数据库服务器
		
    loginconn = loginconnect.cursor()        #创建操作游标
    print("start delete data into mysql!")
    sql_insert="DELETE FROM "+table+" WHERE stuid='"+stuid+"'"
    loginconn.execute(sql_insert)
    loginconnect.commit()
    print("successfully")


