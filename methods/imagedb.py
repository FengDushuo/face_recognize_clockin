#!/usr/bin/env python
# coding=utf-8
import pymysql
from methods.setdb import imagconnect         #已整合进setdb.py中
 
def setimagedb():
    loginconnect = imagconnect   #连接数据库服务器
        
    loginconn = loginconnect.cursor()        #创建操作游标
    #你需要一个游标 来实现对数据库的操作,相当于一条线索

    loginconn.execute("create table students(id int(11),stuname varchar(20),stuid varchar(20)PRIMARY KEY,imagedata MEDIUMBLOB)")