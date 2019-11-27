import cv2
import numpy as np
import matplotlib.pyplot as plt


height = 486
width = 349
image = cv2.imread('detectshape.png')

freq =  np.zeros((256,), dtype=float)

for i in range(0, height):
	for j in range(0, width):
	    x = image[i][j][0]
	    freq[x] = freq[x]+1



print(freq)
'''
cv2.imshow('Histogram specification', image1)
cv2.waitKey(30000) 
cv2.destroyAllWindows()
'''








 
#print new_val
