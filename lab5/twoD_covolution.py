# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:46:04 2019

@author: STUDENT
"""


import numpy as np
import cv2
import matplotlib.pyplot as plt


input_array=np.zeros((5,5),dtype=np.int32)

for i in range(0,5):
    for j in range(0,5):
        input_array[i][j]=i*5+j+1

k=np.ones((3,3),dtype=np.int32)

row_traspose=np.ones((3,3),dtype=np.int32)
for i in range(3):
    for j in range(3):
        row_traspose[i][j]=k[i][2-j]
        
for j in range(3):
    for i in range(3):
        k[i][j]=row_traspose[2-i][j]

H=np.zeros((5,7,3),dtype=np.int32)

for i in range(5):
    for j in range(7):
        if j<=4:
            H[i][j][0]=input_array[i][j]
        else:
            H[i][j][0]=0

for i in range(5):
    for j in range(7):
        H[i][j][1]=H[i][(j-1+7)%7][0]
        H[i][j][2]=H[i][(j-2+7)%7][0]
print(H)

A=np.zeros((49,9),dtype=np.int32)

for i in range(35):
    h=int(i/7)
    for j in range(7):
        A[h*7+j][0]=H[h][j][0]
        A[h*7+j][1]=H[h][j][1]
        A[h*7+j][2]=H[h][j][2]

for i in range(35,49):
    A[i][0]=0
    A[i][1]=0
    A[i][2]=0

for i in range(49):
    h=int(i/7)
    for j in range(7):
        A[h*7+j][3]=A[((h-1+7)%7)*7+j][0]
        A[h*7+j][4]=A[((h-1+7)%7)*7+j][1]
        A[h*7+j][5]=A[((h-1+7)%7)*7+j][2]
        
        A[h*7+j][6]=A[((h-2+7)%7)*7+j][0]
        A[h*7+j][7]=A[((h-2+7)%7)*7+j][1]
        A[h*7+j][8]=A[((h-2+7)%7)*7+j][2]

print("A matrix is:" )
print(A)
oneDkernel=np.zeros(9,dtype=np.int32)

for i in range(3):
    for j in range(3):
        oneDkernel[i*3+j]=k[i][j]
print("\nKernel: ")
print(oneDkernel)



ans=np.dot(A,oneDkernel)

ans=ans.reshape(7,7)

print("\nConvoluted Matrix")
print(ans)



    
      
            



        







