import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading image
img = cv.imread('contr2.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Original Imagen', img)

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")

# Dimensions
heigth = img.shape[0]
width = img.shape[1]

# Creating matrix
Contrast = np.zeros((heigth, width, 1),np.uint8)

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	Contrast[x][y] = img[x][y]

# Adding outliers
for x in range(0, 10, 1):
    for y in range(0, 10, 1):
    	Contrast[x][y] = 0

cv.imshow('Contrast',Contrast)

# Generating histogram
hist = cv.calcHist([Contrast], [0], None, [256], [0, 256])
plt.title("Histograma  of Contrast") 
plt.plot(hist, color='gray' )
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogram2_2.png')
plt.show()

filename = 'resultado2.png'

# Saving the image 
cv.imwrite(filename, Contrast) 

print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()