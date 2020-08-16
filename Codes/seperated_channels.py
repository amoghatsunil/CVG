# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:28:25 2020

@author: hp
"""

import cv2
import numpy as np

img = cv2.imread('lenna.png')
print(img.shape)

b= img[0:110,0:110,2]
r= img[110:220,0:110,0]
g=img[0:110,110:220,1]


img1 = np.zeros(img.shape)

img1[0:110,0:110,0] = b
img1[0:110,110:220,1] = g
img1[110:220,0:110,2] = r
img1[110:220,110:220]= img[110:220,110:220]


cv2.imwrite('seperated_channels.png',img1) 