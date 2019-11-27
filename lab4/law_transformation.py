import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

image1 = cv2.imread('tire.tif')
imagex = cv2.imread('tire.tif')
imagey = cv2.imread('tire.tif')

image2 = cv2.imread('pout.tif')
imagez = cv2.imread('pout.tif')
imagew = cv2.imread('pout.tif')

height1 = image1.shape[0]
width1 = image1.shape[1]

height2 = image2.shape[0]
width2 = image2.shape[1]
neg_transform1 = image1
log_transform1 = imagex
pow_transform1 = imagey

neg_transform2 = image2
log_transform2 = imagez
pow_transform2 = imagew

#freq =  np.zeros((256,), dtype=float)
c = 100
c1 = 10
y = 1/2.5

for i in range(0, height1):
	for j in range(0, width1):
	    x = image1[i][j][0]
	    neg_transform1[i][j] = 255-x
	    log_transform1[i][j] = c*(math.log(1+x,10))
	    pow_transform1[i][j] = c1*(math.pow(x,y))


for i in range(0, height2):
	for j in range(0, width2):
	    x = image2[i][j][0]
	    neg_transform2[i][j] = 255-x
	    log_transform2[i][j] = c*(math.log(1+x, 10))
	    pow_transform2[i][j] = c1*(math.pow(x,y))

plt.subplot(121)
plt.imshow(neg_transform1)
plt.title("Negative transform of tire")
plt.subplot(122)
plt.imshow(neg_transform2)
plt.title("Negative transform of pout")
plt.show()

plt.subplot(121)
plt.imshow(log_transform1)
plt.title("Logarithmic transform of tire")
plt.subplot(122)
plt.imshow(log_transform2)
plt.title("Logarithmic transform of pout")
plt.show()


plt.subplot(121)
plt.imshow(pow_transform1)
plt.title("Power transform of tire")
plt.subplot(122)
plt.imshow(pow_transform2)
plt.title("Power transform of pout")
plt.show()







