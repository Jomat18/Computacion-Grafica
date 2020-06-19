import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading image
img = cv.imread('resul_sustraccion_3T.jpg', cv.IMREAD_GRAYSCALE)

# Generating histogram
hist = cv.calcHist([img], [0], None, [256], [0, 256])

# Valores minimos y maximos 
(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(img)

# Dimensions
heigth = img.shape[0]
width = img.shape[1]

# Creating matrix
Contrast = np.zeros((heigth, width, 1),np.uint8)

# Contrast Stretching
a=0
b=255
c=minVal 
d=maxVal 
temp = (b - a)/(d - c)

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	Contrast[x][y] = (img[x][y] - c) * temp + a 

cv.imshow('Contrast',Contrast)

filename = 'resul_sustraccion_3T_contrast.png'

# Saving the image 
cv.imwrite(filename, Contrast) 

#print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()