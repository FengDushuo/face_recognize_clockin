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

class downloadHandler(tornado.web.RequestHandler):
    def get(self):
        filename=self.get_argument("filename",default=None)
        #url 下载文件的位置
        url = "D:\\a_work\\test\\self_test\\face_recognize\\face_recognize\\attendance_csvs\\" + filename
        self.set_header('Content-Type', 'application/octet-stream;charset=UTF-8')
        # filename 指定下载名字
        self.set_header("Content-Disposition", "attachment; filename=" + filename )
        buf_size = 4096
        with open(url, "r+",encoding="utf-8") as f:
            while True:
                data=f.read(buf_size)
                print(data)
                if not data:
                    break
                self.write(data.encode('mbcs'))
        self.finish()