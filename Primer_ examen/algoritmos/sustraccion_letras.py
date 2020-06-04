import sys
import cv2 as cv
import numpy as np 
import matplotlib as plt

def subtraccion(img1, img2,c,threshold):
    #c=parac
    #threshold=parathresh
    # Dimensions
    # Obteniendo dimensiones de la imagen
    heigth = img1.shape[0]
    width = img1.shape[1]

    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]

    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1]   

    # Creating matrix
    img_out = np.zeros((heigth, width, 1),np.uint8)
    img_out=img_out.astype(int)

    #c=100
    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            img_out[x][y] = ((img1[x][y]/2) - (img2[x][y]/2))+c

    #threshold
    #threshold=90
    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            if img_out[x][y]<threshold:
                img_out[x][y]=0
            else:
                img_out[x][y]=255

    return img_out


if __name__ == "__main__":
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    c = int(sys.argv[3])
    threshold = int(sys.argv[4])

    img1 = cv.imread(filename1,0)
    img2 = cv.imread(filename2,0)

    #img1 = cv.imread("sub_1.jpg",0)
    #img2 = cv.imread("sub_2.jpg",0)
    img_out = subtraccion(img1,img2,c,threshold)
    

     # Guardando la imagen del resultado
    cv.imwrite(filename1, img_out) 
    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()
