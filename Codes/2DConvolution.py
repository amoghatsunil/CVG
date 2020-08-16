

import numpy as np

#extract patch
a=np.ones([10,10])
counter=1
for i in range(10):
    for j  in  range(10):
        a[i,j]=counter
        counter=counter+1

patch_size=[3,3]
size_a=a.shape

row=int(input("enter number of rows (1-8)\n"))
col=int(input("enter number of columns (1-8)\n"))


i=row
j=col
output=np.zeros(patch_size)


for k in range(patch_size[0]):
    for l in range(patch_size[1]):
        output[k,l]=a[i+k,j+l]
        
        
print(output)
       