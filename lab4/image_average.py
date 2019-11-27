import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
height1 = 136
width1 = 172

image1 = cv2.imread('eight.tif')
image2 = cv2.imread('eight.tif')

avg_image = image1
wavg_image = image2

weight = np.zeros((3,3), dtype=float)

weight[0][0] = 1
weight[0][1] = 2
weight[0][2] = 2
weight[1][0] = 1.5
weight[1][1] = 3
weight[1][2] = 1
weight[2][0] = 2
weight[2][1] = 1
weight[2][2] = 2

temp = 0
for i in range(3):
	for j in range(3):
		temp = temp+weight[i][j]
for i in range(0, height1):
    for j in range(0, width1):
        s = 0
        ws = 0
        count = 1
        s = s+image1[i][j][0]
        ws = ws+weight[1][1]*image2[i][j][0]
        if(i-1>=0 and j-1>=0):
            s=s+image1[i-1][j-1][0]
            ws=ws+weight[0][0]*image2[i-1][j-1][0]
            count = count+1
        if(i-1>=0):
            s = s+image1[i-1][j][0]
            ws = ws+weight[0][1]*image2[i-1][j][0]
            count = count+1
        if(i-1>=0 and j+1 < width1):
            s= s+image1[i-1][j+1][0]
            ws= ws+weight[0][2]*image2[i-1][j+1][0]
            count = count+1
        if(i+1 < height1 and j-1>=0):
            s= s+image1[i+1][j-1][0]
            ws=ws+weight[2][0]*image2[i+1][j-1][0]
            count = count+1
        if(i+1 < height1):
            s= s+image1[i+1][j][0]
            ws= ws+weight[2][1]*image2[i+1][j][0]
            count = count+1
        if(i+1 < height1 and j+1 < width1):
            s= s+image1[i+1][j+1][0]
            ws= ws+weight[2][2]*image2[i+1][j+1][0]
            count = count+1
        if(j-1 >=0):
            s= s+image1[i][j-1][0]
            ws= ws+weight[1][0]*image2[i][j-1][0]
            count = count+1
        if(j+1 < width1):
            s= s+image1[i][j+1][0]
            ws= ws+weight[1][2]*image2[i][j+1][0]
            count = count+1
		#print(s)
        avg_image[i][j] = s/count
        wavg_image[i][j] = ws/temp


plt.imshow(avg_image, cmap='gray')
plt.title("Averaging of Image")
plt.show()
plt.imshow(wavg_image, cmap='gray')
plt.title("Weighted Averaging of Image")
plt.show()








