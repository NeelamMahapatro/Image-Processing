import cv2
#import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('grain.png')
height = image.shape[0]
width = image.shape[1]

freq = [0 for i in range(256)]
for i in range(0, height):
	for j in range(0, width):
	    x = image[i][j][0]
	    freq[x] = freq[x]+1

#print freq	    

plt.bar(range(256), freq, color='blue')
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram of Grain")

#plt.show()
