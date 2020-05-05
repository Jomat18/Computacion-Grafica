import cv2
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Imagen', img)

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")

heigth = img.shape[0]
width = img.shape[1]

Contrast = np.zeros((heigth, width, 1),np.uint8)

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	Contrast[x][y] = img[x][y]

for x in range(0, 15, 1):
    for y in range(0, 15, 1):
    	Contrast[x][y] = 0

cv.imshow('Contrast',Contrast)

filename = 'resultado2.png'

cv.imwrite(filename, Contrast) 

print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()

cv2.waitKey(0)


cv2.destroyAllWindows()
