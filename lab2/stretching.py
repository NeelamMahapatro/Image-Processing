import cv2
import matplotlib.pyplot as plt

image = cv2.imread('grain.png', 0)
height = image.shape[0]
width = image.shape[1]
for i in range(0, height):
	for j in range(0, width):
		x = image[i][j]
		if(x < 80):
			image[i][j] = x/2
		elif(x >80 and x<160):
			image[i][j] = 2*x-120
		else:
			image[i][j] = 0.578*x+107.52
			
plt.imshow(image, cmap='gray')
plt.title("Bit-stretching")
plt.show()

freq = [0 for i in range(256)]
for i in range(0, height):
	for j in range(0, width):
	    x = image[i][j]
	    freq[x] = freq[x]+1

plt.bar(range(256), freq, color='blue')
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Histogram After Stretching")
