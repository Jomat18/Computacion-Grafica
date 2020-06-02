import cv2 as cv
import numpy as np 
import matplotlib as plt

def suma(img1, img2):
    # Dimensions
    heigth = img2.shape[0]
    width = img2.shape[1]

    # Creating matrix
    img_out = np.zeros((heigth, width, 1),np.uint8)
    img_out=img_out.astype(int)

    c=0
    for x in range(0, heigth, 1):
        for y in range(0, width, 1):

            img_out[x][y] = ((img1[x][y]/2) + (img2[x][y]/2))+c
    return img_out


if __name__ == "__main__":
    img1 = cv.imread("add_1.jpg",0)
    img2 = cv.imread("add_2.jpg",0)
    img_out = suma(img1,img2)
    cv.imwrite("resul.jpg",img_out)
    cv.imshow('Healthy',img_out)
