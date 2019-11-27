import cv2
import numpy as np
import matplotlib.pyplot as plt

height = 461
width = 469
image = cv2.imread('fractal.png')

mat1 = np.zeros((height, width))
mat2 = np.zeros((height, width))
mat3 = np.zeros((height, width))
mat4 = np.zeros((height, width))
mat5 = np.zeros((height, width))
mat6 = np.zeros((height, width))
mat7 = np.zeros((height, width))
mat8 = np.zeros((height, width))


for i in range(0, height):
	for j in range(0, width):
	    x = image[i][j][0]
	    for k in range(1, 8):
	        #print type(x)
	    	if (k==1):
	    		mat1[i][j] = (x >> (k-1))&1
	    	if (k==2):
	    		mat2[i][j] = (x >> (k-1))&1
	    	if (k==3):
	    		mat3[i][j] = (x >> (k-1))&1
	    	if (k==4):
	    		mat4[i][j] = (x >> (k-1))&1
	    	if (k==5):
	    		mat5[i][j] = (x >> (k-1))&1
	    	if (k==6):
	    		mat6[i][j] = (x >> (k-1))&1
	    	if (k==7):
	    		mat7[i][j] = (x >> (k-1))&1
	    	if (k==8):
	    		mat8[i][j] = (x >> (k-1))&1
            #x = x>>1
		#print (image[i][j][0] & 1)
		
		#print x
plt.imshow(mat1, cmap='gray')
plt.show()
plt.imshow(mat2, cmap='gray')
plt.show()
plt.imshow(mat3, cmap='gray')
plt.show()
plt.imshow(mat4, cmap='gray')
plt.show()
plt.imshow(mat5, cmap='gray')
plt.show()
plt.imshow(mat6, cmap='gray')
plt.show()
plt.imshow(mat7, cmap='gray')
plt.show()
plt.imshow(mat8, cmap='gray')
plt.show()
