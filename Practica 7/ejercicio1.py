#!/usr/bin/python

import sys
import cv2 as cv
import numpy as np


#multiplicación por una constante

def MultiplicacionC(img1, c):

    heigth = img1.shape[0]
    width = img1.shape[1]

    # Imagen resultado
    nueva_imagen = np.zeros((heigth, width, 3), np.int)

    for i in range(heigth):
        for j in range(width):
            for k in range(3):
                nueva_imagen[i][j][k] = img1[i][j][k] * c

    return nueva_imagen

if __name__ == "__main__":

    filename1 = sys.argv[1]
    c = int(sys.argv[2])

    # Leer imagenes
    img1 = cv.imread(filename1)

    nueva_imagen = MultiplicacionC(img1,c)

    # Guardando la imagen del resultado
    cv.imwrite('resultado_1_'+str(c)+'.jpg', nueva_imagen) 
    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()
