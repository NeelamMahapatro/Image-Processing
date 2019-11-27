import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

m=8
n=8

ar = np.zeros((m,n), dtype = np.float)
ai = np.zeros((m,n), dtype = np.float)
M,N = ar.shape
bR = np.zeros((M*M,N*N), dtype = np.float)
bI = np.zeros((M*M,N*N), dtype = np.float)

for i in range(M):
    for j in range(N):
        ar[i,j] = np.cos((-2 * np.pi * i * j)/M)
        ai[i,j] = np.sin((-2 * np.pi * i * j)/M)

for u in range(M):
    for v in range(N):
        for i in range(M):
            for j in range(N):
                bR[u*M+i,v*N+j] = ar[i,u] * ar[j,v] - ai[i,u] * ai[j,v]
                bI[u*M+i,v*N+j] = ar[i,u] * ai[j,v] + ai[i,u] * ar[j,v]
                
Real = np.asarray(bR * 255,dtype=np.uint8)
Img =  np.asarray(bI * 255,dtype=np.uint8)

plt.subplot(1,2,1)
plt.imshow(Real[8:16, 8:16],cmap='gray')
plt.subplot(1,2,2)
plt.imshow(Img,cmap='gray')
plt.show()

#cv2.imshow('Real',Real)
#cv2.imshow('Imaginary',Img)


#cv2.waitKey(50000) 
#cv2.destroyAllWindows()     
