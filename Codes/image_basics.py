# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:15:50 2020

@author: hp
"""

import cv2
import numpy as np

a=np.zeros((240,240))
b=np.shape(a)
a[:,:b[1]//2]=255
a[:,b[1]//2:b[1]]=0
a=np.uint8(a)
cv2.imwrite("first_image.png",a)

