import sys
import cv2 as cv
import cv2
import numpy as np
import math

if __name__ == "__main__":

	filename = sys.argv[1]
	c = int(sys.argv[2])

	# Leer imagen
	img = cv.imread(filename , cv.IMREAD_GRAYSCALE)
	heigth = img.shape[0]
	width = img.shape[1]
	
	A = np.identity(c)  
	B = [[100],[30]]
	M = np.concatenate((A, B), axis=1)
	
	nueva_imagen = np.zeros((heigth, width, 1),np.uint8)
	nueva_imagen = cv2.warpAffine(img, M, (heigth, width))

	# Guardando la imagen del resultado
	cv.imwrite(filename, nueva_imagen) 

	cv.destroyAllWindows()
	cv.waitKey(1) 
	exit()