# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:24:24 2020

@author: hp
"""

import numpy as np
import cv2

a=np.zeros((240,240,3))
'''a[0:120,0:120,0]=255
a[0:120,120:240,1]=255
a[120:240,0:120,2]=255
a[120:240,120:240]=255
a=np.uint8(a)
cv2.imwrite("color_image.png",a)
print(a.shape)'''

a[0:80,:,0]=255
a[80:160,:,1]=255
a[160:240,:]=255
a=np.uint8(a)
cv2.imwrite("BGW_image.png",a)
print(a.shape)