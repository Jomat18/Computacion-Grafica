#import required library
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpig
#matplotlib inline

#read the gray scale image
image = cv2.imread('1.png')#,cv2.IMREAD_GRAYSCALE)
def CSmoothing(image, windows_size):
    heigth, width, k = image.shape
    cv2.imshow('OR',image)
    boundary = int(windows_size/2)
    output = image.copy()
    for x in range(heigth):
        for y in range(width):
            x_i = x-boundary
            y_i = y-boundary
            x_f = x+boundary
            y_f = y+boundary
            if x_i<0:
                x_i = 0
            if x_f>heigth:
                x_f = heigth
            if y_i<0:
                y_i = 0
            if y_f>width:
                y_f = width                          
            for c in range(k):
                box = image[x_i:x_f, y_i:y_f,c]
                minimo=box.min()
                maximo=box.max()
                if (image[x][y][c] > box.max()).all():
                    output[x][y][c] = box.max()
                if (image[x][y][c] < box.min()).all():
                    output[x][y][c] =   box.min()  
                else:
                    output[x][y][c] = output[x][y][c]
    return output

image = CSmoothing(image, 2)
cv2.imwrite('FiltroCS.png',image)
cv2.imshow('Entrada',image)
cv2.waitKey(0)
cv2.destroyAllWindows()