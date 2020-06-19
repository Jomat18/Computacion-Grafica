#!/usr/bin/python

import sys
import cv2 as cv
import os  # Agregar esto
import numpy as np

def division(img1, img2):
    # Obteniendo dimensiones de la imagen
    heigth = img1.shape[0]
    width = img1.shape[1]

    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]

    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1]       

    # Imagen resultado
    nueva_imagen = np.zeros((heigth, width, 1), np.int)

    for i in range(heigth):
        for j in range(width):
            nueva_imagen[i][j] = (img1[i][j]/img2[i][j])*30

    return nueva_imagen

if __name__ == "__main__":

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    # Leer imagenes
    img1 = cv.imread(filename1, 0)
    img2 = cv.imread(filename2, 0)

    nueva_imagen = division(img1, img2)

    # Guardando la imagen del resultado

    filename, file_extension = os.path.splitext(filename1)

    cv.imwrite(filename+'_r'+file_extension, nueva_imagen) 
    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()