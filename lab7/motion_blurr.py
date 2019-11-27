import numpy
import cv2
import random
import math
import matplotlib.pyplot as plt

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#generate A and H(u,v)
complexMatrix = numpy.zeros((m,n),dtype= complex)
H = numpy.zeros((m,n),dtype=complex)
a = 0.001
b = 0.1
for i in range(0,m):
    for j in range(0,n):
        power = i*j
        real = math.cos((2*math.pi*power)/m)
        img = -1*math.sin((2*math.pi*power)/n)
        complexMatrix[i][j] = complex(real,img)

        param = math.pi*((i+1)*a + (j+1)*b)
        real = ((math.sin(math.pi*param)*math.cos(math.pi*param))/float(math.pi*param))
        img = -1*((math.sin(math.pi*param)*math.sin(math.pi*param))/float(math.pi*param))
        H[i][j] = complex(real,img)

matConj = numpy.conj(complexMatrix)
dftImage = numpy.matmul(numpy.matmul((complexMatrix),greyImage) , (numpy.transpose(complexMatrix)))
blurredImage = H*dftImage
idftImage = numpy.matmul(numpy.matmul((numpy.transpose(matConj)), blurredImage) , matConj)
plt.subplot(121)
plt.imshow(numpy.real(idftImage),cmap='gray')
plt.title("Motion blurred Image")


restoredImage = blurredImage/H
idftImage = numpy.matmul(numpy.matmul((numpy.transpose(matConj)), restoredImage) , matConj)
plt.subplot(122)
plt.imshow(numpy.real(idftImage),cmap='gray')
plt.title("Restored Image")
plt.show()