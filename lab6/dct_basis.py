import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

n=8
ar = np.zeros((n,n), dtype = np.float)

M,N = ar.shape
bR = np.zeros((M*M,N*N), dtype = np.float)


for i in range(M):
    for j in range(N):
        if j == 0 :
            ar[i,j] = math.sqrt(float(1/M))*np.cos((np.pi * (2*i + 1) * j) / (2*M))
        else:
            ar[i,j] = math.sqrt(float(2/M))*np.cos((np.pi * (2*i + 1) * j) / (2*M))

for u in range(M):
    for v in range(N):
        for i in range(M):
            for j in range(N):
                bR[u*M+i,v*N+j] = ar[i,u] * ar[j,v]
bR[0][0] = 0
Real = np.asarray(bR * 255,dtype=np.uint8)
plt.subplot(111)
plt.imshow(Real,cmap='gray')
plt.show()
