# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:19:36 2020

@author: amogha
"""

import cv2
import numpy as np

img=cv2.imread("einstein.png",0)

patch=[[ 1, 2, 1],
       [ 0, 0, 0],
       [-1,-2,-1]]
patch=np.array(patch)

patch_size=[3,3]
img_size=img.shape

output_matrix=np.zeros([img_size[0]-2,img_size[1]-2])

for i in range(img_size[0]-2):
    for j in range(img_size[1]-2):
        
        output=np.zeros(patch_size)
        for k in range(patch_size[0]):
            for l in range(patch_size[1]):
                output[k,l]=img[i+k,j+l]
        temp=np.sum(patch*output)
        temp=temp/8
        output_matrix[i,j]=temp
    
output_matrix=np.uint8(output_matrix)
cv2.imwrite("sobel_filter_hori.png",output_matrix)

        
        
