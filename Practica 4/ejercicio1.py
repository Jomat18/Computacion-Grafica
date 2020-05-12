import cv2
import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt

# cargamos la imagen
image = cv.imread('log_1.jpg', 0)
cv.imshow('Original Imagen',image)

# Generar su histograma
plt.title("Histograma  of log_1.jpg") 
plt.hist(image.ravel(),256,[0,256]) 
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogram1.png')
plt.show()

# Dimensiones de la imagen original
heigth = image.shape[0]
width = image.shape[1]

# Creamos una matriz
Logarithm = np.zeros((heigth, width, 1),np.uint8)


#aplicamos Logarithm Operator
c = 120
for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	aux = c * math.log10( (1 + image[x][y]) )
    	if (aux > 255):
    		aux = 255
    	if (aux < 0):
    		aux = 0
    	Logarithm[x][y] = aux



#calculamos el histograma de nuestro resultado
plt.title("Histograma  of resul log_1.jpg") 
plt.hist(Logarithm.ravel(),256,[0,256]) 
plt.xlabel('lighting intensity')
plt.ylabel('number of pixels')
plt.savefig('histogramOfResult1-120.png')
plt.show()

# Guardamos la imagen
cv.imshow('Logarithm',Logarithm)
filename = 'resultado1-120.png'
cv.imwrite(filename, Logarithm) 

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()
