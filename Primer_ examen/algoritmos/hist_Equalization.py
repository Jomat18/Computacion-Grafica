import sys
import os 
import cv2 as cv
import numpy as np
import math

def escribiendo_resultado(nueva_imagen, img, heigth, width, s_n):
    # Nueva imagen
    for i in range(heigth):
        for j in range(width):
            nueva_imagen[i][j] = int(s_n[img[i][j]])


def calculando_histograma(img, heigth, width, intensidad):
    histograma = np.zeros((intensidad, 1) ,np.float32)

    for i in range(heigth):
        for j in range(width):
            histograma[img[i][j]][0] = histograma[img[i][j]][0] + 1

    return histograma

# Ecualizacion del Histograma 
def ecualizacion(heigth, width, s_n, L, histograma):
    p_n = np.zeros(L ,np.float32)
    h_w = heigth*width
    p_n[0] = histograma[0][0]/h_w
    s_n[0] = math.floor((L-1)*p_n[0])

    for i in range(1,L):
        p_n[i] = histograma[i][0]/h_w + p_n[i-1]
        s_n[i] = math.floor((L-1)*p_n[i])
   

if __name__ == "__main__":

    filename = sys.argv[1]

    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)

    # Dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]

    print (heigth, width)

    intensidad = 256
    # Imagen resultado
    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    s_n = np.zeros(intensidad ,np.float32)

    histograma = calculando_histograma(img, heigth, width, intensidad)
    ecualizacion(heigth, width, s_n, intensidad, histograma)
    escribiendo_resultado(nueva_imagen, img, heigth, width, s_n)

    # Guardando la imagen
   # cv.imwrite(filename, nueva_imagen) 
   #Agregar esto
    filename, file_extension = os.path.splitext(filename)

    cv.imwrite(filename+'_r'+file_extension, nueva_imagen) 

    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()