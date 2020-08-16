# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 07:29:01 2020

@author: hp
"""

import cv2
import random
import numpy as np

img=cv2.imread("einstein.png",0)
img_size=img.shape
for i in range(500):
    x=random.randint(0,img_size[0]-1)
    y=random.randint(0,img_size[1]-1)
    img[x,y]=random.randint(0,1)*255

cv2.imwrite("saltpepper_noise.png",img)
   
patch_size=[3,3]
output_m=np.zeros([img_size[0]-2,img_size[1]-2]) 
for i in range(img_size[0]-3): 
    for j in range(img_size[1]-3):
        output=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                output[k,l]=img[i+k,j+l]
        temp=np.median(output)
        output_m[i+1,j+1]=temp
        
output_m=np.uint8(output_m)
cv2.imwrite("median_filter.png",output_m)
