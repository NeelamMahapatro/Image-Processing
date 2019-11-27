import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

height = 205
width = 232
image = cv2.imread('tire.tif')
height = image.shape[0]
width = image.shape[1]

freq =  np.zeros((256,), dtype=float)

for i in range(0, height):
	for j in range(0, width):
	    x = image[i][j][0]
	    freq[x] = freq[x]+1

pmf = np.zeros((256,), dtype=float)
for i in range(0, 256):
    pmf[i] = freq[i]/(205*232)	    
    
cdf = [0 for i in range(256)]
cdf[0] = pmf[0]

for i in range(1, 256):
    cdf[i] = cdf[i-1]+pmf[i]

new_val = [0 for i in range(256)]
for i in range(0, 256):
    new_val[i] = cdf[i]*255
    
for i in range(0, height):
	for j in range(0, width):
	    image[i][j] = new_val[image[i][j][0]]
    
plt.subplot(121)
plt.imshow(image, cmap='gray') #after histogram equalization
plt.title("Histogram Equalization")

image_using_inbuilt = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
image_using_inbuilt[:,:,0] = cv2.equalizeHist(image_using_inbuilt[:,:,0]) #Histogram Equalization using inuilt function
image_using_inbuilt = cv2.cvtColor(image_using_inbuilt, cv2.COLOR_YUV2BGR)

plt.subplot(122)
plt.imshow(image_using_inbuilt, cmap='gray')
plt.title("Using Inbuilt-Function")
plt.show()

plt.bar(np.arange(256), freq)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram After Equlization")

plt.show()






 
#print new_val
