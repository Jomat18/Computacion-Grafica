import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse
import math


def mostrar_guardar(operador, imagen, filename, c):
    # Mostrando y guardando la imagen del resultado
    cv.imshow('Resultado - ' + operador, imagen)
    cv.imwrite('resultado_' + operador + '_' + filename + ' Con ' + str(c) + '.png', imagen) 


def RaizOperator(c, img, heigth, width, nueva_imagen):
    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            aux = c * math.sqrt( (1 + img[x][y]) )
            if (aux > 255):
                aux = 255
            if (aux < 0):
                aux = 0
            nueva_imagen[x][y] = aux 
    return nueva_imagen
                
if __name__ == "__main__":

    # Datos
    filename = sys.argv[1]
    c = float(sys.argv[2])
    
    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)
    # Obteniendo dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]   

    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    filename = filename.split(".")[0]    

    # Operaciones
    operador = 'RaizOperator'

    nueva_imagen = RaizOperator(c, img, heigth, width, nueva_imagen)
    mostrar_guardar(operador, nueva_imagen, filename, c)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()