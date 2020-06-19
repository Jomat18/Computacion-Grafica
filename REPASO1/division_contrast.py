#!/usr/bin/python

import sys
import cv2 as cv
import numpy as np

def division(img1, img2):
    global cantidad
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


    # Contrast Stretching        
    colores = np.zeros((heigth, width, 1),np.uint8)

    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            colores[x][y] = nueva_imagen[x][y]

    colores = np.sort(colores, axis = None)   
    lower = int((cantidad/100)*(heigth*width))
    higher = int(((100-cantidad)/100)*(heigth*width))

    a = 0
    b = 255
    c = int(colores[lower])
    d = int(colores[higher-1])

    temp = (b - a)/(d - c)

    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            nueva_imagen[x][y] = (nueva_imagen[x][y] - c) * temp + a 

    return nueva_imagen

if __name__ == "__main__":

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    cantidad = int(sys.argv[3])

    # Leer imagenes
    img1 = cv.imread(filename1, 0)
    img2 = cv.imread(filename2, 0)

    nueva_imagen = division(img1,img2)

    # Guardando la imagen del resultado
    cv.imwrite('division_contrast_'+str(cantidad)+'.jpg', nueva_imagen) 
    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()