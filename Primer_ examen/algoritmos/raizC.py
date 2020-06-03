#!/usr/bin/python

import sys
import cv2 as cv
import numpy as np
import math

def mostrar_guardar(imagen, filename):
    cv.imwrite(filename, imagen) 

def operador_raizCuadrada(c, r, img, heigth, width, nueva_imagen):

    for i in range(heigth):
        for j in range(width):
            temp = c*pow(img[i][j], r)
            
            if temp > 255:
                temp = 255

            if temp < 0:
                temp = 0    

            nueva_imagen[i][j] = temp

    return nueva_imagen

if __name__ == "__main__":

    # Datos
    filename = sys.argv[1]
    c = float(sys.argv[2])
    r = float(sys.argv[3])
    
    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)

    # Obteniendo dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]   

    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    nueva_imagen = operador_raizCuadrada(c, r, img, heigth, width, nueva_imagen)
    mostrar_guardar(nueva_imagen, filename)

    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()