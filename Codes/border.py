

import cv2
import numpy as np 

img=cv2.imread("lenna.png")

s=img.shape
print(img.shape)
img1=np.uint8(np.zeros((240,240)))


img1[20:220+20,20:220+20]


cv2.imwrite("border.png",img1)