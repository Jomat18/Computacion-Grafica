import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math

#datos
img = cv.imread('hist5.jpg', 0)
alto = img.shape[0]
ancho = img.shape[1]
intensidad = 256
Sn = np.zeros(intensidad ,np.float32)

#histograma
histograma = np.zeros((intensidad, 1) ,np.float32)

for i in range(alto):
    for j in range(ancho):
        histograma[img[i][j]][0] = histograma[img[i][j]][0] + 1

#hallando Pn
Pn = np.zeros(intensidad ,np.float32)
alto_x_ancho = alto*ancho
Pn[0] = histograma[0][0]/alto_x_ancho
Sn[0] = math.floor((intensidad-1)*Pn[0])

#Agsignando los Sn
for i in range(1,intensidad):
    Pn[i] = histograma[i][0]/alto_x_ancho + Pn[i-1]
    Sn[i] = math.floor((intensidad-1)*Pn[i])

#Cambiando los valores a la imagen 
for i in range(alto):
        for j in range(ancho):
            img[i][j] = int(Sn[img[i][j]])


cv.imshow('Nueva Imgen',img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()














