#!/usr/bin/python
import sys
import os 
import cv2
import numpy as np

def thresholding_adaptativo(image, windows_size, constant):
	heigth, width = image.shape

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

	    	box = image[x_i:x_f, y_i:y_f]					    			

	    	if image[x][y] < box.mean() - constant:
	    		output[x][y] = 0
	    	else:
	    		output[x][y] = 255        

	return output  

	
filename = sys.argv[1]
img=cv2.imread(filename)

img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

image = thresholding_adaptativo(img, 10, 2)

# Guardando resultados
filename, file_extension = os.path.splitext(filename)
cv2.imwrite(filename+'_r'+file_extension, image) 

cv2.destroyAllWindows()
cv2.waitKey(1) 
exit()