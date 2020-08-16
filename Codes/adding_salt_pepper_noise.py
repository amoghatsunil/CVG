# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 06:52:00 2020

@author: hp
"""

import numpy as np
import random
import cv2


def noise_make(img,prob):
    thres =1-prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output1[i][j] = 0
            elif rdn > thres:
                output1[i][j] = 255
            else:
                output1[i][j] = img[i][j]
    return output1
    



img=image=cv2.imread("einstein.png",0)
output1 = np.zeros(img.shape,np.uint8)
ouput1=noise_make(img,0.05)
cv2.imwrite('salt_pepper_noise.jpg', output1)