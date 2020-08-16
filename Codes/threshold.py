# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:14:36 2020

@author: hp
"""

import cv2


img=cv2.imread('doraemon.png',0)
s=img.shape

for i in range(s[0]):
    for j in range(s[1]):
        if img[i,j]< 127:
            img[i,j]=0
        else:
            img[i,j]=255
            
cv2.imwrite('threshold.png',img)