import pymysql

mysqluser="root"
mysqlpassword=""
logindatabase="login_db"
imagedatabase="faceimage"
hostsrc="localhost"

conn = pymysql.connect(host=hostsrc,port=3306,user=mysqluser,password=mysqlpassword,charset='utf8')
cursor = conn.cursor()
createloginsql="CREATE DATABASE IF NOT EXISTS "+logindatabase
createfaceimgsql="CREATE DATABASE IF NOT EXISTS "+imagedatabase
cursor.execute(createfaceimgsql)
cursor.execute(createloginsql)


logconnect = pymysql.connect(    #连接数据库服务器
    user=mysqluser,              #本地mysql用户名
    password="19971130",          #本地MySQL密码
    host=hostsrc,
    port=3306,
    db=logindatabase,
    charset="utf8"
)

imagconnect = pymysql.connect(    #连接数据库服务器
    user=mysqluser,
    password="19971130",
    host=hostsrc,
    port=3306,
    db=imagedatabase,
    charset="utf8"
)

loginconnect = imagconnect               #连接数据库服务器        
loginconn = loginconnect.cursor()        #创建操作游标
                                         #你需要一个游标 来实现对数据库的操作,相当于一条线索
loginconn.execute("create table IF NOT EXISTS students(id int(11),stuname varchar(20),stuid varchar(20)PRIMARY KEY,imagedata MEDIUMBLOB)")

loginconnect = logconnect                #连接数据库服务器
    
loginconn = loginconnect.cursor()        #创建操作游标
                                         #你需要一个游标 来实现对数据库的操作相当于一条线索

loginconn.execute("CREATE TABLE IF NOT EXISTS users (id int(11) PRIMARY KEY ,username VARCHAR(20),password VARCHAR(40),email VARCHAR(40))")