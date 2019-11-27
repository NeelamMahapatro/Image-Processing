import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

n = input("Enter value of n ")
final_imageR = np.zeros((n*n,n*n), dtype=float)
final_imageI = np.zeros((n*n,n*n), dtype=float)

imageR = np.zeros((n*n,n*n), dtype=np.uint8)
imageI = np.zeros((n*n,n*n), dtype=np.uint8)

Areal = np.zeros((n, n), dtype = float)
Aimg = np.zeros((n, n), dtype = float)
ArealT = np.zeros((n, n), dtype = float)
AimgT = np.zeros((n, n), dtype = float)

for i in range(0, n):
	for j in range(0, n):
		Areal[j][i] = math.cos(2*3.1416*i*j/n)
		Aimg[j][i] = math.sin(-2*3.1416*i*j/n)
		ArealT[i][j] = Areal[j][i]
		AimgT[i][j] = Aimg[j][i] 
	'''
print(Areal)
print(ArealT)
'''
for j in range(0, n):
	for k in range(0, n):
		for l in range(0, n):
			for w in range(0, n):
				final_imageR[j*n+l][k*n+w] = Areal[l][j] * ArealT[k][w]
				final_imageI[j*n+l][k*n+w] = Aimg[l][j] * AimgT[k][w]
				imageR[j*n+l][k*n+w] = abs(final_imageR[j*n+l][k*n+w])*255
				imageI[j*n+l][k*n+w] = abs(final_imageI[j*n+l][k*n+w])*255
'''
var = 0
for i in range(0,n):
	for j in range(0, n):
		var = var+1
		plt.subplot(n,n, var)
		plt.imshow(imageR)
		plt.show() 
		
print(final_imageR)

print(Areal[2][4])
print(Areal[5][3])
print(final_imageR[34][43])
'''



print(imageR)
plt.imshow('Real DFT', imageR)
plt.imshow('Imaginary DFT', imageI)









    
      
            



        







