#!/usr/bin/python

import sys
import cv2 as cv
import numpy as np


def thresholding(img):

    heigth = img.shape[0]
    width = img.shape[1]

    for x in range(heigth):
        for y in range(width):
            color = img[x][y]
            if img[x][y]>70 and img[x][y]<150:
                img[x][y] = 255
            else:
                img[x][y] = 0                                   

    return img

def operador_or(img1, img2):

    img1 = thresholding(img1)
    img2 = thresholding(img2)
    # Obteniendo dimensiones de la imagen nueva
    heigth = img2.shape[0]
    width = img2.shape[1]

    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]

    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1]       

    # Imagen resultado operador or
    nueva_imagen = np.zeros((heigth, width, 1), np.int)
    nueva_imagen=nueva_imagen.astype(int)
    nueva_imagen=cv.bitwise_or(img1,img2)

    return nueva_imagen

if __name__ == "__main__":

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    # Leer imagenes
    img1 = cv.imread(filename1,0)
    img2 = cv.imread(filename2,0)

    nueva_imagen = operador_or(img1,img2)
     
    # Guardando la imagen del resultado
    cv.imwrite(filename1, nueva_imagen)  

    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()