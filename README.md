# face_recognize_clockin
Face recognition attendance system.  
Please refer to the PDF for specific operating instructions.

# requirements
chardet==4.0.0  
face_recognition==1.3.0  
glob2==0.7  
matplotlib==3.2.2  
numpy==1.19.3  
opencv_python_headless==4.1.2.30  
Pillow==10.0.0  
PyMySQL==0.9.3  
scikit_image==0.17.2  
skimage==0.0  
tensorflow==2.0.0  
tornado==6.1  

# brief description of the database
1. You need to use MySQL and configure MySQL locally.  
If MySQL is not available locally, to perform installation configuration you can refer to https://www.runoob.com/w3cnote/windows10-mysql-installer.html  
2. Remember the root name and password in step 1, and modify "mysqluser" and "mysqlpassword" in methods/setdb.py.
3. Execute setdb.py.

# other declarations
1. sendemail.py : This file involves password recovery when the account password is lost, which requires the administrator's email account and password. It involves personal privacy and needs to be modified according to each individual's situation.
2. The modifications of sendemail.py include:
   my_sendername = "***"       # Sender account name, such as "yangfan"
   my_sender="***"    	       # Example of sender's email account "1224556@163.com"
   my_pass = "***"             # Sender's email password, such as "123456"
   mail_host = "***"           # SMTP server, such as "stmp.163. com"
   And in line 24 of code: server.sendmail (my_sender, [to_address[1], "***"], msg. as_string()), change "* * *" to the corresponding account of my_sender.
