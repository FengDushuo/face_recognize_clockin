# -*- coding: utf-8 -*-
import base64
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
pymysql.install_as_MySQLdb()
# from predict import predict

class workattendanceHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("workattendance.html")
    def post(self):
        base64str = self.get_argument('formFile') 
        base64str = base64str.replace("data:image/jpeg;base64,","")
        imgstr = base64.b64decode(base64str)
        imgio = io.BytesIO(imgstr) 
        img = Image.open(imgio) 
        stuname=self.get_argument("studentname")
        stuid=self.get_argument("studentid")
        img.save('faceimage/'+str(stuid)+'.jpg')
        fin = open('faceimage/'+str(stuid)+'.jpg','rb+')
        img=base64.b64encode(fin.read())
        fin.close()
        imgdata=pymysql.escape_string(str(img))
        miwd.insertinfo("students",stuname,stuid,imgdata)
        returndata={"result":"success"}
        returndata_json=json.dumps(returndata)
        self.write(returndata_json)

    


        



