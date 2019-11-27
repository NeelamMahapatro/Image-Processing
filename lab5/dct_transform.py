import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
n = input("Enter value of n ")
final_imageR = np.zeros((n*n,n*n), dtype=float)

imageR = np.zeros((n*n,n*n), dtype=np.uint8)

Areal = np.zeros((n, n), dtype = float)
ArealT = np.zeros((n, n), dtype = float)


for i in range(0, n):
	for j in range(0, n):
		if(j==0):
			Areal[j][i] = math.sqrt(1/n)*math.cos(3.1416*(2*i+1)*j/2*n)
		else:
		    Areal[j][i] = math.sqrt(2/n)*math.cos(3.1416*(2*i+1)*j/2*n)
		ArealT[i][j] = Areal[j][i]
		 
'''
print(Areal)
print(ArealT)
'''
for j in range(0, n):
	for k in range(0, n):
		for l in range(0, n):
			for w in range(0, n):
				final_imageR[j*n+l][k*n+w] = Areal[l][j] * ArealT[k][w]
				#final_imageI[j*n+l][k*n+w] = Aimg[l][j] * AimgT[k][w]
				imageR[j*n+l][k*n+w] = abs(final_imageR[j*n+l][k*n+w])*255
				#imageI[j*n+l][k*n+w] = abs(final_imageI[j*n+l][k*n+w])*255
print(Areal)
print(final_imageR[34][43])
'''
print(final_imageR)

print(Areal[2][4])
print(Areal[5][3])
print(final_imageR[34][43])
'''

plt.imshow('DCT', imageR)
plt.show()









    
      
            



        







