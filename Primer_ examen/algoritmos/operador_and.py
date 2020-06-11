#!/usr/bin/python

import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def thresholding(img):

	heigth = img.shape[0]
	width = img.shape[1]

	for x in range(heigth):
	    for y in range(width):
	        color = img[x][y]
	        if 104 < color:
	        	img[x][y] = 255
	        else:
	        	img[x][y] = 0        		  	              	

	return img
	        	

def operator_and(img1, img2):
    
    img1 = cv.bitwise_not(img1)
    img2 = cv.bitwise_not(img2)

    img1 = thresholding(img1)
    cv.imwrite('static/images/img3.png',img1)      
    img2 = thresholding(img2)
    cv.imwrite('static/images/img4.png',img2)      

    new_image = cv.bitwise_and(img1, img2)
    
    return new_image

if __name__ == "__main__":

    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    # Leer imagenes
    img1 = cv.imread(filename1, 0)
    img2 = cv.imread(filename2, 0)

    new_image = operator_and(img1,img2)

    # Saving result
    cv.imwrite(filename1, new_image) 
    
    cv.waitKey(0) 
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()