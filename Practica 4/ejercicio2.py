import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
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

if __name__ == "__main__":

    filename = sys.argv[1]
    c = int(sys.argv[2])

    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)

    nueva_imagen = operador_logaritmo(c, img)

    filename = filename.split(".")[0]

    # Generando histograma del resultado
    hist = cv.calcHist([nueva_imagen], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.title("Histograma  del resultado") 
    plt.xlabel('intensidad de iluminacion')
    plt.ylabel('cantidad de pixeles')
    plt.savefig('hist_' + filename + '.png')
    plt.show()

    # Mostrando y guardando la imagen del resultado
    cv.imshow('Resultado',nueva_imagen)
    cv.imwrite('resultado_' + filename + '.png', nueva_imagen) 
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()