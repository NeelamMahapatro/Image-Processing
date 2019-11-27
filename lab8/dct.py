import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def DCT(k,n,N):
    dct = -1
    if n==0:
        dct = math.sqrt(1/float(N))*math.cos((math.pi*(2*k+1)*n)/(2*float(N)))
    else:
        dct = math.sqrt(2/float(N))*math.cos((math.pi*(2*k+1)*n)/(2*float(N)))
    return dct

def getBasisDCT(a,b):
    b_image=[]
    for i in range(len(a)):
        temp=[]
        for j in range(len(b)):
            temp.append(a[i]*b[j])
        b_image.append(temp)
    return b_image

def basisImage(N):
    A_list=[]
    for i in range(N):
        Ak=[]
        for j in range(N):
            Ak.append(DCT(j,i,N))
        A_list.append(Ak)
    basis=[]
    for i in range(len(A_list)):
        temp=[]
        for j in range(len(A_list)):
            temp.append(getBasisDCT(A_list[i],A_list[j]))
        basis.append(temp)
    basis=np.asarray(basis)
    return basis

result=basisImage(8)
fig=plt.figure(figsize=(8,8))
k=1
for i in range(8):
    for j in range(8):
        fig.add_subplot(8,8,k)
        plt.imshow(result[i][j],cmap='gray')
        k+=1
plt.show()