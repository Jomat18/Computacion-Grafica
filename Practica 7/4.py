#!/usr/bin/python

import sys
import cv2 as cv
import numpy as np

def blending(img1, img2):
    # Obteniendo dimensiones de la imagen
    heigth = img1.shape[0]
    width = img1.shape[1]

    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]

    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1]       

    # Imagen resultado
    nueva_imagen = np.zeros((heigth, width, 3), np.int)

    #img1 = img1*(0.9)
    #img2 = img2*(0.9)
    x=0.75
    for i in range(heigth):
        for j in range(width):
            for k in range(3):
                nueva_imagen[i][j][k] = x*img1[i][j][k] +(1-x)*img2[i][j][k]

    return nueva_imagen

if __name__ == "__main__":

  #  filename1 = sys.argv[1]
  #  filename2 = sys.argv[2]

    # Leer imagenes
   # img1 = cv.imread(filename1)
    #img2 = cv.imread(filename2)
    img1 = cv.imread("blen1.png")
    img2 = cv.imread("blen2.png")

    nueva_imagen = blending(img1,img2)

    # Guardando la imagen del resultado
    cv.imwrite('resultado4_075.jpg', nueva_imagen) 
    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()