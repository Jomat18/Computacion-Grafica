import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math

intensidad = 256

# Leer imagen
img = cv.imread('hist10_1.jpg', cv.IMREAD_GRAYSCALE)

# pixels para calcular el histograma
pixels = np.zeros((intensidad, 1) ,np.float32)

# Dimensiones de la imagen
heigth = img.shape[0]
width = img.shape[1]

# Calculando el histograma
for i in range(heigth):
    for j in range(width):
        pixels[img[i][j]][0] = pixels[img[i][j]][0] + 1

p_n = np.zeros(intensidad ,np.float32)
s_n = np.zeros(intensidad ,np.float32)

# Imagen resultado
nueva_imagen = np.zeros((heigth, width, 1), np.uint8)

# Ecualizacion del Histograma 
h_w = heigth*width
p_n[0] = pixels[0][0]/h_w
s_n[0] = math.floor((intensidad-1)*p_n[0])

for i in range(1,intensidad):
    p_n[i] = pixels[i][0]/h_w + p_n[i-1]
    s_n[i] = math.floor((intensidad-1)*p_n[i])

# Nueva imagen
for i in range(heigth):
    for j in range(width):
        nueva_imagen[i][j] = int(s_n[img[i][j]])


hist = cv.calcHist([nueva_imagen], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )
plt.title("Histograma  del resultado") 
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.savefig('histograma.png')
plt.show()

cv.imshow('Resultado',nueva_imagen)

# Guardando la imagen
cv.imwrite('Resultado.png', nueva_imagen) 

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()