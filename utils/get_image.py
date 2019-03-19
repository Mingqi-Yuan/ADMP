"""
Encoding = UTF-8
By Mingqi, Yuan, 2019/3/18
Usage: get image file from the onstage
"""
from flask import request
import cv2
import os

def get_image():
    img = request.files.get('photo')
    path = "static/images/"
    file_path = path + img.filename
    img.save(file_path)
    img = cv2.imread(file_path)
    cv2.imwrite(os.path.join('static/images', 'test.jpg'), img)
