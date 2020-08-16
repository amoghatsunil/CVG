# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:00:51 2020

@author: hp
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("lenna.png",0)

hist=np.zeros(256)
s=img.shape

for i in range(s[0]):
    for j in range(s[1]):
        hist[img[i,j]]+=1
plt.stem((hist))

