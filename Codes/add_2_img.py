# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:28:48 2020

@author: hp
"""

import cv2


img1=cv2.imread("lenna.png")
img2=cv2.imread("doraemon.png")
img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

img=img1/2+img2/2

cv2.imwrite('add_2_img.png',img)

