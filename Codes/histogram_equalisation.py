import cv2
import numpy as np
import matplotlib.pyplot as plt

#histogram
img=cv2.imread("lenna.png",0)
cv2.imwrite("lenna_gray.png",img)
hist=np.zeros(256)
s=img.shape

for i in range(s[0]):
    for j in range(s[1]):
        hist[img[i,j]] += 1

plt.plot(hist)   

#cummulative histogram
ch=np.zeros(256)

for i in range(len(hist)):
    if i==0:
        ch[i]=hist[i]
    else:
        ch[i]=hist[i]+ch[i-1]
        
for i in range(len(ch)):
    if ch[i]!=0:
        m=i
        break
print(m)

#Look Up Table(LUT)
lt=np.zeros(256)

for k in range(m,len(ch)):
    lt[k]=(ch[k]-ch[m])/(ch[255]-ch[m])
lt=lt*255

#create a new image 
img1=np.uint8(np.zeros((s[0],s[1])))

for i in range(s[0]):
    for j in range(s[1]):
        img1[i,j]=(lt[img[i,j]])

cv2.imwrite("histogram_equalised.png",img1)


histnew=np.zeros(256)
for i in range(s[0]):
    for j in range(s[1]):
        histnew[img1[i,j]]+=1
plt.plot(histnew)
