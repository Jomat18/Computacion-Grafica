import sys
import cv2 as cv
import numpy as np

def thresholding_adaptativo(image, windows_size, constant):
	heigth, width = image.shape

	boundary = int(windows_size/2)

	output = np.zeros((heigth, width, 1),np.uint8)

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
	  
	cv.imwrite('output_'+str(windows_size)+'_'+str(constant)+'.png', output) 	


if __name__ == "__main__":

	filename = sys.argv[1]
	windows_size = int(sys.argv[2])
	constant = int(sys.argv[3])

	image = cv.imread(filename, 0)

	thresholding_adaptativo(image, windows_size, constant)

	cv.destroyAllWindows()
	cv.waitKey(1) 
	exit()