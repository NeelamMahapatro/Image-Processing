import numpy as np
import cv2
import random
import math
import matplotlib.pyplot as plt

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cov_mat = np.cov(greyImage)
eigan_values, eigan_vectors = np.linalg.eig(cov_mat)

k=50
k1 =200 

kl_mul = np.asarray(eigan_vectors[:,0:k])
compressed = np.matmul(np.transpose(kl_mul),greyImage)

print("     Restoration using KL-Transform")
restored = np.matmul(kl_mul,compressed)
plt.subplot(121)
plt.imshow(restored,cmap='gray')
plt.title("(K=50)")
kl1_mul = np.asarray(eigan_vectors[:,0:k1])
compressed1 = np.matmul(np.transpose(kl1_mul),greyImage)

restored1 = np.matmul(kl1_mul,compressed1)

plt.subplot(122)
plt.imshow(restored1,cmap='gray')
plt.title("(K=200)")
plt.show()