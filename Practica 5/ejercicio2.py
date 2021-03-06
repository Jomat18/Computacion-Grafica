import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse
import math


def mostrar_guardar(operador, imagen, filename,c,r):
    # Mostrando y guardando la imagen del resultado
    cv.imshow('Resultado - ' + operador, imagen)
    cv.imwrite('resultado_' + operador + '_' + filename + ' Con ' + str(c) + '_' + str(r) + '.png', imagen) 


def mostrar_histograma(operador, imagen, filename,c,r):

    # Generando histograma del resultado
    hist = cv.calcHist([imagen], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.title("Histograma") 
    plt.xlabel('intensidad de iluminacion')
    plt.ylabel('cantidad de pixeles')
    plt.savefig('hist_' + operador + '_' + filename + ' Con ' + str(c)+ '_'+ str(r) + '.png')
    plt.show()


def operador_raizCuadrada(c, r, img, heigth, width, nueva_imagen):

    for i in range(heigth):
        for j in range(width):
            #operador RaizCuadrada
            temp = c*pow(img[i][j], r)
            #El resultado este dentro de los limites
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

    filename = filename.split(".")[0]    

    # Operaciones
    operador = 'raiz'

    nueva_imagen = operador_raizCuadrada(c, r, img, heigth, width, nueva_imagen)
    mostrar_histograma(operador, nueva_imagen, filename, c, r)
    mostrar_guardar(operador, nueva_imagen, filename, c, r)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()