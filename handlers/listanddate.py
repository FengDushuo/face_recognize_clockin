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
import pymysql
pymysql.install_as_MySQLdb()
csv_path=".\\attendance_csvs"


class listanddateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("listanddate.html")

    def post(self):
        csvlist = os.listdir(csv_path)
        csvdata=",".join(csvlist)
        self.write(csvdata)
