import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

M=256
N=256

image = cv2.imread('cameraman.tif')
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
A = np.zeros((M,N),dtype= float)
dct = np.zeros((M,N),dtype=complex)

for i in range(0,M):
    for j in range(0,N):
        if j == 0 :
            A[i,j] = np.sqrt(np.float(1/M))*np.cos((np.pi * (2*i + 1) * j) / (2*M))
        else:
            A[i,j] = np.sqrt(np.float(2/M))*np.cos((np.pi * (2*i + 1) * j) / (2*M))

dct = (A) * greyImage * (np.transpose(A))
idct = np.zeros((M,N),dtype=float)

idct = (np.transpose(A))* dct * (A)

print(idct)



plt.show()