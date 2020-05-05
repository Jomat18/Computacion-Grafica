import cv2
import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original Imagen', img)

if img.size == 0:
    sys.exit("Error: the image has not been correctly loaded.")


hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )
plt.title("Histograma  of contr2") 
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.savefig('histogram1.png')
plt.show()


heigth = img.shape[0]
width = img.shape[1]

Contrast = np.zeros((heigth, width, 1),np.uint8)
a=0
b=255
c=55
d=135
for x in range(0, heigth, 1):
    for y in range(0, width, 1):
    	aux = (img[x][y] - c)
    	Contrast[x][y] = aux * ((b-a)/(d-c)) + a 
cv.imshow('Contrast',Contrast)

print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()

cv2.waitKey(0)


cv2.destroyAllWindows()
