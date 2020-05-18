import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
# el ,0 lo tranforma a escala de grises la imagen yee
img=cv.imread('exp_5.jpg',cv.IMREAD_GRAYSCALE)
alto=img.shape[0]
ancho=img.shape[1]
c=20
b=1.02
nueva_imagen = np.zeros((alto, ancho, 1),np.uint8)

for i in range(0, alto, 1):
    for j in range(0, ancho, 1):
   		nueva_imagen[i][j]= c * ( math.pow(b, img[i][j])-1 )
cv.imshow('image',nueva_imagen)
cv.imwrite('b_1_0_2.png', nueva_imagen) 
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()
