import cv2
import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt

# loading image
image = cv.imread('hist10_1.jpg', 0)
cv.imshow('Original Imagen',image)

# Generating histogram
plt.title("Histograma  of hist10_1.jpg") 
plt.hist(image.ravel(),256,[0,256]) 
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogram3.png')
plt.show()


# Dimensions
heigth = image.shape[0]
width = image.shape[1]

# Creating matrix
EqualizacionH = np.zeros((heigth, width, 1),np.uint8)

#date
NumberOfPixel = heigth * width
L = 255  

#version con ayuda de 
'''
#for x in range(0, heigth, 1):
#    for y in range(0, width, 1):
P=[]
for x in range(0,L):
	aux = np.count_nonzero((image == x)) 
	P.append(aux / NumberOfPixel)
	res1 = L * sum(P)
	res = math.floor(res1)
	print (res)

'''

#version 1
'''
P=[]
for c in range(0,L):
	aux = 0
	for x in range(0, heigth, 1):
		for y in range(0, width, 1): 
			if (image[x][y]==c):
				aux+=1

	P.append(aux / NumberOfPixel)
	res1 = L * sum(P)
	res = math.floor(res1)
	print (res)
	for x in range(0, heigth, 1):
		for y in range(0, width, 1): 
			if (image[x][y]==c):
				EqualizacionH[x][y] = res 
'''

#version mejorada

P=[]
for c in range(0,L):
	Li=[]
	aux = 0
	for x in range(0, heigth, 1):
		for y in range(0, width, 1): 
			if (image[x][y]==c):
				Li.append([x,y])
				aux+=1

	P.append(aux / NumberOfPixel)
	res1 = L * sum(P)
	res = math.floor(res1)
	#print (res)
	for i in range(0,aux):
		h=Li[i][0]
		b=Li[i][1]
		EqualizacionH[h][b] = res 

plt.title("Histograma  of result 3") 
plt.hist(EqualizacionH.ravel(),256,[0,256]) 
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogramOfResult3.png')
plt.show()

cv.imshow('EqualizacionH',EqualizacionH)

filename = 'resultado3.png'
  
# Saving the image 
cv.imwrite(filename, EqualizacionH) 


print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()
