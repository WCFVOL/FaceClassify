#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import cv2
# 读取图片
import os
from PIL import Image
from FaceClassify import settings
def get_face(img):
    # 转化为灰度图

    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 特征级联表
    # 文件地址是你的opencv目录下的haarcascades\haarcascade_frontalface_alt.xml文件！！注意你要使用需要安装opencv并对下面地址进行修改
    #print(settings.BASE_DIR+'\haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(os.path.join(settings.BASE_DIR, 'haarcascade_frontalface_default.xml'))
    # 多尺寸检测，返回列表  #
    img = cv2.imdecode(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('img.jpg',img)
    face = face_cascade.detectMultiScale(img, 1.3, 3)
    i = 0
    face_list = []
    for (x, y, w, h) in face:
        # (图像对象，圆心，半径，颜色，封闭？)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 0)
        # 将人脸扣出
        i += 1
        # cv2.circle(img,((x+x+w)//2,(y+y+h)//2),w//2,(255,0,0),7)
        # 保存图像+
        im = img[y:y+h, x:x+w]
        img_1 = cv2.resize(im, (47, 55), interpolation=cv2.INTER_CUBIC)
        face_list.append(img_1)
        #cv2.imwrite(str(i) +str(random.randint(0,9))+ '11.jpg', img_1)
    return face_list
