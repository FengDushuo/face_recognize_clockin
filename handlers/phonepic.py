# -*- coding: utf-8 -*-
import base64
import numpy as np
import tornado.escape
from tornado.websocket import WebSocketHandler
import tornado.web
import json
import cv2  
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import tensorflow as tf
from PIL import Image, ImageFilter
import skimage
import PIL.ImageOps 
import io
import methods.imgwritedb as miwd
import methods.imgreaddb as mird
import pymysql
from methods.multifyfacerecognition import Mfacerecognition
pymysql.install_as_MySQLdb()
import csv
import time
csvs_path="attendance_csvs/"
# from predict import predict

def create_csv(path):
    with open(path,'w+',encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_head = ["studentid","studentname","ifattend","time"]
        csv_write.writerow(csv_head)
def write_csv(path,a,b,c,d):
    with open(path,'a+',encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = [a,b,c,d]
        csv_write.writerow(data_row)

# class stuattendinfo:
#     def __init__(self,stuid,stuname,ifattend):
#         self.stuid=stuid
#         self.stuname=stuname
#         self.ifattend=ifattend

class phonepicHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("phonepic.html")
    def post(self):
        # base64str = self.get_argument('img') 
        # base64str = base64str.replace("data:image/jpeg;base64,","")
        # imgstr = base64.b64decode(base64str)
        # imgio = io.BytesIO(imgstr) 
        # img = Image.open(imgio) 
        # stuname=self.get_argument("stuname")
        # stuid=self.get_argument("stuid")
        # img.save('faceimage/'+str(stuid)+'.png')
        # fin = open('faceimage/'+str(stuid)+'.png','rb+')
        # img=base64.b64encode(fin.read())
        # fin.close()
        # imgdata=pymysql.escape_string(str(img))
        # miwd.insertinfo("students",stuname,stuid,imgdata)
        filedata=self.get_argument("formFile")
        #解码并生成图片存于predict_images/test.png
        img_data=base64.b64decode(filedata) 
        image = 'predict_images/test.jpg'
        file = open(image,'wb')
        file.write(img_data)
        file.close()

        dbimagelist=mird.select_dics("students","*")
        stuidlist=mird.select_columns("students","stuid")
        for i in range(len(stuidlist)):
            fout = open("dbimage/%s.jpg"%stuidlist[i],'wb')
            fout.write(base64.b64decode(eval(dbimagelist[i]["imagedata"])))
            fout.close()

        attendid_list=Mfacerecognition("faceimage","predict_images")
        print(attendid_list)        #返回在勤人员学号

        # stunum=len(attendid_list)
        # studatalist=[[] for i in range(stunum)]
        dataname=time.strftime('StudentsAttendanceInfo_%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        csv_name=csvs_path+str(dataname)+'.csv'
        create_csv(csv_name)
        returnidlist=[]
        returnnamelist=[]
        returnifattend=[]
        for stuid in attendid_list:
            stuname=mird.select_table("students","stuname","stuid",stuid)[0][0]
            write_csv(csv_name,stuid,stuname,"在勤",datetime)
            returnidlist.append(stuid)
            returnnamelist.append(stuname)
            returnifattend.append("在勤")
        absent_list=[]
        for stuid in stuidlist:
            if stuid[0] not in attendid_list:
                absent_list.append(stuid[0])
        for stuid in absent_list:
            stuname=mird.select_table("students","stuname","stuid",stuid)[0][0]
            write_csv(csv_name,stuid,stuname,"缺勤",datetime)
            returnidlist.append(stuid)
            returnnamelist.append(stuname)
            returnifattend.append("缺勤")
            

        returndata={"stuid":returnidlist,"stuname":returnnamelist,"ifattend":returnifattend}
        returndata_json=json.dumps(returndata)
        self.write(returndata_json)

        

        





        


    


        



