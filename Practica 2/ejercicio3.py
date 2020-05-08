
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading image
print sys.argv[1]
print int(sys.argv[1])
cantidad = int(sys.argv[1])

img = cv.imread('resultado2.png', cv.IMREAD_GRAYSCALE)
cv.imshow('Original Imagen', img)

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

print (cantidad,'%',' y ', 100-cantidad, '%')

a = 0
b = 255
c = int(colores[lower])
d = int(colores[higher-1])

print ('c :', c, 'd:', d)

temp = (b - a)/(d - c)

for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	Contrast[x][y] = (img[x][y] - c) * temp + a 

cv.imshow('Contrast',Contrast)

hist = cv.calcHist([Contrast], [0], None, [256], [0, 256])
plt.title("Histograma  of Outlier 1") 
plt.plot(hist, color='gray' )
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogram3_2.png')
plt.show()

filename = 'resultado3_2.png'

# Saving the image 
cv.imwrite(filename, Contrast) 

print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()
