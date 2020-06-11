import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def thresholding(img):
    heigth = img.shape[0]
    width = img.shape[1]
    img_out = np.zeros((heigth, width, 1), np.int)
    for x in range(heigth):
        for y in range(width):
            if (70 < img[x][y] < 150):
                img_out[x][y] = 0
            else:
                img_out[x][y] = 255
    return img_out
                

def operator_xor(img1, img2, img_out):   
    img1 = thresholding(img1)
    cv.imwrite('E3img1_bin.png',img1)      
    img2 = thresholding(img2)
    cv.imwrite('E3img2_bin.png',img2)      
    img_out = cv.bitwise_xor(img1, img2)  
    return img_out

if __name__ == "__main__":
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    # Leer imagenes
    img1 = cv.imread(filename1, 0)
    img2 = cv.imread(filename2, 0)

    # Obteniendo dimensiones de la imagen
    heigth = img1.shape[0]
    width = img1.shape[1]
    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]
    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1] 

    img_out = np.zeros((heigth, width, 1), np.int)
    img_out = operator_xor(img1,img2,img_out)
    cv.imwrite('resultado3.png', img_out) 
    
    cv.waitKey(0) 
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()