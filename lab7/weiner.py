import numpy
import cv2
import math
import matplotlib.pyplot as plt

image = cv2.imread('cameraman.tif')
m=image.shape[0]
n=image.shape[1]
greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#generate A and H(u,v)
cMatrix = numpy.zeros((m,n),dtype= complex)
deg_fun=numpy.zeros((m,n),dtype=complex)
a=0.001
b=0.1
T=1.0000
for i in range(0,m):
    for j in range(0,n):
        power = i*j
        real = math.cos((2*math.pi*power)/m)
        img = -math.sin((2*math.pi*power)/n)
        cMatrix[i][j] = complex(real,img)
        
        realv=(float(T)/(math.pi*((i+1)*a+(j+1)*b)))*math.sin(math.pi*((i+1)*a+(j+1)*b))*math.cos(-math.pi*((i+1)*a+(j+1)*b))
        imgv=(float(T)/(math.pi*((i+1)*a+(j+1)*b)))*math.sin(math.pi*((i+1)*a+(j+1)*b))*-math.sin(math.pi*((i+1)*a+(j+1)*b))
        deg_fun[i][j]=complex(realv,imgv)

matConj = numpy.conj(cMatrix)
dftImage = numpy.dot(numpy.dot((cMatrix), greyImage ) , (numpy.transpose(matConj)))
degraded_image = deg_fun*dftImage
idftImage = numpy.dot(numpy.dot((numpy.transpose(matConj)), degraded_image) , (cMatrix))
plt.subplot(121)
plt.imshow(numpy.real(idftImage),cmap='gray')
plt.title("Median Blur")

plt.subplot(122)
restored = (numpy.conj(deg_fun)/((deg_fun*numpy.conj(deg_fun))+0.00000001))*degraded_image
restored_idftImage = numpy.dot(numpy.dot((numpy.transpose(matConj)), restored) , (cMatrix))
plt.imshow(numpy.real(restored_idftImage),cmap='gray')
plt.title("Restored by Weiner Filter")
plt.show()