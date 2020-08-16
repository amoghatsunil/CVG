# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:11:04 2020

@author: hp
"""


import numpy
import cv2 
 
img1=cv2.imread("lenna.png")
img2=cv2.imread("doraemon.png")
img1=cv2.resize(img1,(256,256))
img2=cv2.resize(img2,(256,256))

verticalAppendedImg = numpy.hstack((img1,img2))

cv2.imwrite("concatenate_2_img.png",verticalAppendedImg)