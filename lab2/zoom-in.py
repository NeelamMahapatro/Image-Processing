# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:36:27 2019

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

def zoom_fun():
    img = cv2.imread('cameraman.tif',0)
    arr = np.asarray(img, dtype=np.uint8)
    row, col = arr.shape

    k = input('Enter zooming factor : ')
    k = int(k)
    img1 = np.zeros((int(row/k), int(col/k)), dtype=np.uint8)
    img2 = np.zeros((row * k, col * k), dtype=np.uint8)

    for i in range(len(img1)):
        for j in range(len(img1[0])):
            img1[i,j] = img[i*k][j*k];

    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2[i,j] = img[int(i/k)][int(j/k)];
    plt.subplot(121)
    plt.imshow(img1, cmap="gray")
    plt.title("Zoomout Image")
    plt.subplot(122)
    plt.imshow(img2, cmap="gray")
    plt.title("Zoomin Image")
    plt.show()
    
if __name__ == "__main__":
    zoom_fun()