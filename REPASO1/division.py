import cv2 as cv
import numpy as np 
import matplotlib as plt

def division(img1, img2):
    # Dimensions
    heigth = img2.shape[0]
    width = img2.shape[1]

    # Creating matrix
    img_out = np.zeros((heigth, width, 1),np.uint8)
    #img_out=img_out.astype(int)
    #(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(img1)
    c=100
    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            img_out[x][y] =(img1[x][y] / img2[x][y])*c

    return img_out


if __name__ == "__main__":
    img1 = cv.imread("paper6.jpg",0)
    img2 = cv.imread("paper7.jpg",0)
    img_out = division(img1,img2)
    cv.imwrite("resul_division.jpg",img_out)
    cv.imshow('Healthy',img_out)
