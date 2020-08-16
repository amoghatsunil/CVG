# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:36:04 2020

@author: hp
"""

import cv2
import numpy as np

img=cv2.imread("einstein.png",0)
img_size=img.shape

patch=[[1,2,1],[2,4,2],[1,2,1]]

patch=np.array(patch)
patch_size=[3,3]

xlimit=int(img_size[0]//patch_size[0])
ylimit=int(img_size[0]//patch_size[0])

output_m=np.zeros([xlimit,ylimit])

for i in range(xlimit):
    for j in range(ylimit):
        output=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                output[k,l]=img[3*i+k,3*j+l]
        temp=np.sum(patch*output)
        temp=temp/16
        output_m[i,j]=temp
        
cv2.imwrite("gaussian_filter_jumping_window.png",output_m)