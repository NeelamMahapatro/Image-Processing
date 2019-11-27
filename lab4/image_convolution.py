import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
height1 = 136
width1 = 172

'''
for i in range(0, 242):
	for j in range(0, 201):
		for row in range(-1, 2):
			for col in range(-1, 2):
				new[i][j] = conv[row+1][col+1]*grey[i-row][j-col]
'''
row=5
col=5
x = [[1,2,3,4,5],
	[3,4,6,8,9],
	[5,8,9,12,5],
	[6,7,8,9,10],
	[11,12,13,14,15]]
h = [[1,0,1],
	[0,1,5],
	[2,0,3]]

H = np.zeros((row,7,3), dtype=int)
for i in range(0, 5):
	for j in range(0, 3):
		for k in range(j, j+5):
			H[i][k][j] = x[i][k-j]
print(H)

A = np.zeros((row*7, col*3))

'''
for i in range(0, 3):
	for j in range(i*5, 5+i*5):
		for k in range()
'''
#cv2.imshow('average Image', x)

cv2.waitKey(50000) 
cv2.destroyAllWindows()







