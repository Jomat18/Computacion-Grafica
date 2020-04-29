
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading image
image = cv.imread('thresh3.png', 0)
cv.imshow('Original Imagen',image)

# Generating histogram
plt.hist(image.ravel(),256,[0,256]); plt.show()

# Dimensions
heigth = image.shape[0]
width = image.shape[1]

# Creating matrix
healthy_cell = np.zeros((heigth, width, 1),np.uint8)

# Thresholding
for x in range(0, heigth, 1):
    for y in range(0, width, 1):
        color = image[x][y]
        if 162	 < color < 177:
        	healthy_cell[x][y] = 255
        else:
        	healthy_cell[x][y] = 0        		


cv.imshow('Healthy',healthy_cell)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()
