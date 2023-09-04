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


class deleteinfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("deleteinfo.html")
    def post(self):
        deletename = self.get_argument("deletename",default=None)
        deleteid = self.get_argument("deleteid",default=None)
        existname=mird.select_table("students","stuname","stuid",deleteid)[0][0]
        if deletename !=existname or existname==None:
            self.write("inputerror")
        else:
            miwd.deleteinfo("students",deleteid)




        

    


        



