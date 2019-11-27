import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

height = 205
width = 232
image1 = cv2.imread('tire.tif')
image2 = cv2.imread('cameraman.tif')

freq1 =  np.zeros((256,), dtype=float)
freq2 =  np.zeros((256,), dtype=float)

for i in range(0, height):
	for j in range(0, width):
	    x = image1[i][j][0]
	    freq1[x] = freq1[x]+1
	    
for i in range(0, 256):
	for j in range(0, 256):
	    x = image2[i][j][0]
	    freq2[x] = freq2[x]+1

pmf1 = np.zeros((256,), dtype=float)
for i in range(0, 256):
    pmf1[i] = freq1[i]/(205*232)
 

pmf2 = np.zeros((256,), dtype=float)
for i in range(0, 256):
    pmf2[i] = freq2[i]/(256*256)	    
    
cdf1 = [0 for i in range(256)]
cdf1[0] = pmf1[0]
cdf2 = [0 for i in range(256)]
cdf2[0] = pmf2[0]

for i in range(1, 256):
    cdf1[i] = cdf1[i-1]+pmf1[i]
    cdf2[i] = cdf2[i-1]+pmf2[i]

set1 = [0 for i in range(256)]
set2 = [0 for i in range(256)]

for i in range(0, 256):
    set1[i] = int(cdf1[i]*255)
    set2[i] = int(cdf2[i]*255)
    
new_val = [0 for i in range(256)]
for i in range(0, 256):
    target = set1[i]
    index = 0
    for j in range(0, 256):
        if(set2[j] >=target):
            index = j
            break
    new_val[i] = index
    
freq_new = np.zeros((256,), dtype=float)
new_image = np.zeros((height,width), dtype=np.uint8)
for i in range(0, height):
    for j in range(0, width):
        new_image[i][j] = new_val[image1[i][j][0]]
        freq_new[new_image[i][j]] = freq_new[new_image[i][j]]+1 
        
plt.subplot(121)
plt.imshow(image1, cmap='gray')
plt.title("Original Tire Image")

plt.subplot(122)
plt.imshow(new_image, cmap='gray')
plt.title("After Hist Specification")
plt.show()

plt.bar(np.arange(256), freq1)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram of tire image")

plt.show()

plt.bar(np.arange(256), freq2)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram of cameraman image")

plt.show()
plt.bar(np.arange(256), freq_new)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram of tire image after histogram specification with cameraman")

plt.show()








 
#print new_val
