
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading image
img = cv.imread('contr2.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Original Imagen', img)

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")

# Generating histogram
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )
plt.title("Histograma  of image") 
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.savefig('histogram1_1.png')
plt.show()

# Dimensions
heigth = img.shape[0]
width = img.shape[1]

# Creating matrix
Contrast = np.zeros((heigth, width, 1),np.uint8)

# Contrast Stretching
a = 0
b = 255
c = 50
d =	144

temp = (b - a)/(d - c)

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	Contrast[x][y] = (img[x][y] - c) * temp + a 

cv.imshow('Contrast',Contrast)

hist = cv.calcHist([Contrast], [0], None, [256], [0, 256])
plt.title("Histograma  of Contrast") 
plt.plot(hist, color='gray' )
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogram1_2.png')
plt.show()

filename = 'resultado1.png'

# Saving the image 
cv.imwrite(filename, Contrast) 

print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()