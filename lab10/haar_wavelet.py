# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:14:19 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy import linalg
import operator
import math

img = Image.open('cameraman.tif').convert('L')
img = np.array(img, dtype = float)

w = np.zeros((4, int(img.shape[0]/2), int(img.shape[1]/2)), dtype=int)

x=1
for i in range(2):
    img_arr = np.zeros((img.shape[0], img.shape[1]), dtype=float)
    downsampled = np.zeros((img.shape[0], int(img.shape[1]/2)), dtype = float)
    second_conv = np.zeros((img.shape[0], int(img.shape[1]/2)), dtype = float)
    if(i==1):
        first = [-0.7071068, 0.7071068]
    else:
        first = [0.7071068, 0.7071068]
    for k in range(img.shape[1]):
        for l in range(img.shape[0]):
            if(l==img.shape[0]-1):
                img_arr[l][k] = first[0]*img[l][k]
            else:
                img_arr[l][k] = first[0]*img[l][k] + first[1]*img[l+1][k]            
    for k in range(img.shape[0]):
        for l in range(int(img.shape[1]/2)):
            downsampled[k][l] = img_arr[k][l*2]
    for j in range(2):
        if(j==1):
            second = [-0.7071068, 0.7071068]
        else:
            second = [0.7071068, 0.7071068]
        for k in range(downsampled.shape[0]):
            for l in range(downsampled.shape[1]):
                if(l == downsampled.shape[1]-1):
                    second_conv[k][l] = second[0]*downsampled[k][l]
                else:
                    second_conv[k][l] = second[0]*downsampled[k][l] + second[1]*downsampled[k][l+1]
        for k in range(128):
            for l in range(128):
                w[x-1][k][l] = second_conv[2*k][l]
        print(w[x-1])
        plt.subplot(2,2,x)
        plt.imshow(w[x-1], cmap = 'gray')
        x = x+1
plt.show()

upsampled = np.zeros((4, img.shape[0], int(img.shape[1]/2)), dtype = float)
after_conv = np.zeros((4, img.shape[0], int(img.shape[1]/2)), dtype = float)
for i in range(4):
    for k in range(128):
        for l in range(128):
            upsampled[i][2*k][l] = w[i][k][l]
            upsampled[i][2*k+1][l] = w[i][k][l]
for i in range(4):
    if(i%2==0):
        first = [0.7071068, 0.7071068]
    else:
        first = [-0.7071068, 0.7071068]
    for k in range(256):
        for l in range(127):
            if(l==127):
                after_conv[i][k][l] = upsampled[i][k][l]*first[0]
            else:
                after_conv[i][k][l] = upsampled[i][k][l]*first[0] + upsampled[i][k][l+1]*first[1]

after_conv[0] = (after_conv[0]+after_conv[1])/2
after_conv[1] = (after_conv[2]+after_conv[3])/2

upsampled_col = np.zeros((2, img.shape[0], img.shape[1]), dtype = float)
for i in range(256):
    for j in range(128):
        upsampled_col[0][i][2*j] = after_conv[0][i][j]
        upsampled_col[0][i][2*j+1] = after_conv[0][i][j]
        upsampled_col[1][i][2*j] = after_conv[1][i][j]
        upsampled_col[1][i][2*j+1] = after_conv[1][i][j]

after_conv2 = np.zeros((2, img.shape[0], img.shape[1]), dtype = int)
for i in range(2):
    if(i==0):
        second = [0.7071068, 0.7071068]
    else:
        second = [0.7071068, -0.7071068]
        for k in range(img.shape[1]):
            for l in range(img.shape[0]):
                if(l==img.shape[0]-1):
                    after_conv2[i][l][k] = second[0]*upsampled_col[i][l][k]
                else:
                    after_conv2[i][l][k] = second[0]*upsampled_col[i][l][k] + second[1] * upsampled_col[i][l+1][k]

after_conv2[0] = (after_conv2[0]+after_conv2[1])/2
final_image = np.zeros((img.shape[0], img.shape[1]), dtype = int)
final_image = after_conv2[0]
plt.imshow(final_image, cmap='gray')
plt.show()
                









