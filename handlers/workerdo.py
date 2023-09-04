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
import time
pymysql.install_as_MySQLdb()
work_path="inputimage/"
# from predict import predict

class workerdoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("workerdo.html")
    def post(self):
        base64str = self.get_argument('img') 
        base64str = base64str.replace("data:image/jpeg;base64,","")
        imgstr = base64.b64decode(base64str)
        imgio = io.BytesIO(imgstr) 
        img = Image.open(imgio)
        dataname=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        img.save(work_path+str(dataname)+'.jpg')

        dbimagelist=mird.select_dics("students","*")
        stuidlist=mird.select_columns("students","stuid")
        for i in range(len(stuidlist)):
            fout = open("dbimage/%s.jpg"%stuidlist[i],'wb')
            fout.write(base64.b64decode(eval(dbimagelist[i]["imagedata"])))
            fout.close()



        

    


        



