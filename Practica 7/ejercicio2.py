import sys
import cv2 as cv
import numpy as np

def divisionI(img1, img2, heigth, width, constante, intensidad):
    # Imagen resultado
    img_out = np.zeros((heigth, width, 1), np.int)
    #colores = np.zeros((heigth, width, 1), np.uint8)
    colores = np.zeros((heigth, width, 1), np.int)
    for i in range(heigth):
        for j in range(width):
            img_out[i][j] = (img1[i][j]/img2[i][j]) * constante 

    colores = np.sort(img_out, axis = None)   
    lower = int((intensidad/100)*(heigth*width))
    higher = int(((100-intensidad)/100)*(heigth*width))
    newMin = 0
    newMax = 255
    Min = int(colores[lower])
    Max = int(colores[higher-1])
    div = Max-Min
    if (div<=0):
    	div=1
    temp = (newMax-newMin)/div

    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            img_out[x][y] = (img_out[x][y] - Min) * temp + newMin

    return img_out

def thresholding(t, img, heigth, width):
	img_out = np.zeros((heigth, width, 1), np.int)
	for x in range(heigth):
		for y in range(width):
			if (img[x][y] < t):
				img_out[x][y] = 0
			else:
				img_out[x][y] = 255
	return img_out

if __name__ == "__main__":
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    constante = int(sys.argv[3])
    intensidad = int(sys.argv[4])
    threshold = int(sys.argv[5])
    # Leer imagenes
    img1 = cv.imread(filename1,0)
    img2 = cv.imread(filename2,0)
        # Obteniendo dimensiones de la imagen
    heigth = img1.shape[0]
    width = img1.shape[1]
    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]
    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1] 

    img_out2 = divisionI(img1,img2,heigth, width,constante,intensidad)
    cv.imwrite('resultado2T_'+str(constante)+'_'+str(intensidad)+'.jpg', img_out2)
    img_outT = thresholding(threshold, img_out2, heigth, width)
    cv.imwrite('resultado2T_'+str(threshold)+'.jpg', img_outT)

    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()
	
