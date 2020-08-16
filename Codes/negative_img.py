# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:17:37 2020

@author: hp
"""

import cv2
img=cv2.imread("doraemon.png")
a=img.shape
for i in range(a[0]):
    for j in range(a[1]):
        img[i,j]=255-img[i,j]
cv2.imwrite("negative_img.png",img)

