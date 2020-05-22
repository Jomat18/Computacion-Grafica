import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse
import math


def mostrar_guardar(operador, imagen, filename,mi,ma):
    # Mostrando y guardando la imagen del resultado
    #cv.imshow('Resultado - ' + operador, imagen)
    #cv.imwrite('resultado_' + operador + '_' + filename + ' Con ' + str(mi) + '_' + str(ma) + '.png', imagen) 
    filename='resultado.png'
    ruta_output="static/output/"
    # Saving the image 

    cv.imwrite(ruta_output+filename, imagen) 



# Contrast Stretching
def Contrast(mi, ma, img, heigth, width, nueva_imagen):
	a=0
	b=255
	c=mi
	d=ma 
	temp = (b - a)/(d - c)
	for x in range(0, heigth, 1):
	    for y in range(0, width, 1):
	    	nueva_imagen[x][y] = (img[x][y] - c) * temp + a 
	return nueva_imagen
                
if __name__ == "__main__":

    # Datos
    filename = sys.argv[1]
    mi = float(sys.argv[2])
    ma = float(sys.argv[3])
    
    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)

    # Obteniendo dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]   

    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    filename = filename.split(".")[0]    

    # Operaciones
    operador = 'Contrast'

    nueva_imagen = Contrast(mi, ma, img, heigth, width, nueva_imagen)
    mostrar_guardar(operador, nueva_imagen, filename, mi, ma)

    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()