import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse
import math

def mostrar_guardar(operador, imagen, filename):
    # Mostrando y guardando la imagen del resultado
    cv.imshow('Resultado - ' + operador, imagen)
    cv.imwrite('resultado_' + operador + '_' + filename + '.png', imagen) 

def operador_exponencial(c, b, img, heigth, width, nueva_imagen):
  
    for i in range(heigth):
        for j in range(width):
            temp = c*(pow(b, img[i][j]) - 1)
            
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
    b = float(sys.argv[3])

    
    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)

    # Obteniendo dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]   

    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    filename = filename.split(".")[0]    

    # Operaciones
    operador_1 = 'exp'

    nueva_imagen = operador_exponencial(c, b, img, heigth, width, nueva_imagen)
    mostrar_guardar(operador_1, nueva_imagen, filename)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()