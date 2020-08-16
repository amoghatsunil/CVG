# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:16:10 2020

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

patch_size=[3,3]
xlimit=int(img_size[0]//patch_size[0])
ylimit=int(img_size[0]//patch_size[0])

output_m=np.zeros([xlimit,ylimit])


for i in range(xlimit-1):
    for j in range(ylimit-1):
        output=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                output[k,l]=img[3*i+k,3*j+l]
        temp=np.median(output)
        output_m[i+1,j+1]=temp
        
cv2.imwrite("median_filter_jumping_window.png",output_m)






      