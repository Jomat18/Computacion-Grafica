import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math

def escribiendo_resultado(nueva_imagen, img, heigth, width, h, w, s_n):
    # Nueva imagen
    for i in range(heigth):
        for j in range(width):
            nueva_imagen[i][j] = int(s_n[img[i][j]])
            #nueva_imagen[h+i][w+j] = int(s_n[img[i][j]])


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


def segmento(f, c, x, y, img, intensidad, s_n, nueva_imagen): #f -> fila c -> columna  
    crop_img = img[f:f+y, c:c+x]
    #print (crop_img.shape[0], crop_img.shape[1])  
    cv.imshow('Crop',crop_img) 
    heigth = crop_img.shape[0]
    width = crop_img.shape[1]

    histograma = calculando_histograma(crop_img, heigth, width, intensidad)
    ecualizacion(heigth, width, s_n, intensidad, histograma)
    #escribiendo_resultado(nueva_imagen, crop_img, heigth, width, f, c, s_n)

    heigth = img.shape[0]
    width = img.shape[1]
    escribiendo_resultado(nueva_imagen, img, heigth, width, f, c, s_n)


if __name__ == "__main__":

    # Leer imagen
    img = cv.imread('hist10_1.jpg', cv.IMREAD_GRAYSCALE)

    # Dimensiones de la imagen
    heigth = img.shape[0]
    width = img.shape[1]

    print (heigth, width)

    intensidad = 256
    # Imagen resultado
    nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

    s_n = np.zeros(intensidad ,np.float32)

    #tiled_x = 412
    #tiled_y = 663
    
    # for i in range(int(heigth/tiled_y)):
    #     for j in range(int(width/tiled_x)):    
            #segmento(i*tiled_y, j*tiled_x, tiled_x, tiled_y, img, intensidad, s_n, nueva_imagen)
    segmento(320, 200, 100, 120, img, intensidad, s_n, nueva_imagen)

    hist = cv.calcHist([nueva_imagen], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.title("Histograma  del resultado") 
    plt.xlabel('intensidad de iluminacion')
    plt.ylabel('cantidad de pixeles')
    plt.savefig('hist_segmento.png')
    plt.show()

    cv.imshow('Resultado',nueva_imagen)

    # Guardando la imagen
    cv.imwrite('resultado_segmento.png', nueva_imagen) 
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()