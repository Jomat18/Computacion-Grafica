import cv2 as cv
import numpy as np
import math

def operador_logaritmo(c, img):
    # Obteniendo dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]   

    # Imagen resultado
    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    for i in range(heigth):
        for j in range(width):
            temp = c*math.log10(1 + img[i][j])
            
            if temp > 255:
                temp = 255

            if temp < 0:
                temp = 0    

            nueva_imagen[i][j] = temp

    return nueva_imagen