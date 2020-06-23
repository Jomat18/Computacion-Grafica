#!/usr/bin/python

import sys
import cv2 
import numpy as np 
from matplotlib import pyplot as plt

def pixel_replication(img):

    heigth, width, rgb = img.shape

    scaling = np.zeros((heigth*2, width*2, rgb), np.uint8)

    for row in range(heigth):
        for column in range(width):
            scaling[row*2][column*2] = img[row][column]
            scaling[row*2][column*2+1] = img[row][column]
            scaling[row*2+1][column*2] = img[row][column]
            scaling[row*2+1][column*2+1] = img[row][column]
            

    cv2.imwrite('pixel_replication.jpg', scaling)        
    plt.subplot(2, 2, 1) 
    plt.title('Original') 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img)
    plt.imshow(img)
    plt.subplot(2, 2, 2) 
    plt.title('Scaling') 
    scaling = cv2.cvtColor(scaling, cv2.COLOR_BGR2RGB)
    scaling = np.array(scaling)
    plt.imshow(scaling)
    plt.show()        


if __name__ == "__main__":

    filename = sys.argv[1]

    img = cv2.imread(filename)

    pixel_replication(img)
    
    cv2.destroyAllWindows()
    cv2.waitKey(1) 
    exit()