import cv2
import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('ggplot')

height = 464
width = 464
image = cv2.imread('grain.png')
#cv2.imshow('grain', image)

freq = [0 for i in range(256)]

for i in range(0, height):
	for j in range(0, width):
	    x = image[i][j][0]
	    freq[x] = freq[x]+1
	    
print freq

	    
#plt.bar(np.arange(256), freq)
#plt.xlabel("Intensity")
#plt.ylabel("Frequency")
#plt.title("Histogram")

#plt.show()
'''
plt.hist(freq, bins = [i for i in range(0, 256, 10)])
plt.title('Histogram')
plt.show()
'''
