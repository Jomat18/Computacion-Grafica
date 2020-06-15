import sys
import os  # Agregar esto
import cv2 as cv
import numpy as np

# loading image
filename = sys.argv[1]
cantidad = int(sys.argv[2])

img = cv.imread(filename, cv.IMREAD_GRAYSCALE)

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")

# Dimensions
heigth = img.shape[0]
width = img.shape[1]

# Creating matrix
Contrast = np.zeros((heigth, width, 1),np.uint8)

colores = np.zeros((heigth, width, 1),np.uint8)

# Contrast Stretching

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	colores[x][y] = img[x][y]


colores = np.sort(colores, axis = None)   
lower = int((cantidad/100)*(heigth*width))
higher = int(((100-cantidad)/100)*(heigth*width))

a = 0
b = 255
c = int(colores[lower])
d = int(colores[higher-1])

print ('c :', c, 'd:', d)

temp = (b - a)/(d - c)

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
        valor = (img[x][y] - c) * temp + a

        if valor>255:
            valor = 255
        if valor<0:
            valor = 0    

        Contrast[x][y] = valor

#Agregar esto
filename, file_extension = os.path.splitext(filename)

cv.imwrite(filename+'_r'+file_extension, Contrast) 

###############

cv.destroyAllWindows()
cv.waitKey(1) 
exit()