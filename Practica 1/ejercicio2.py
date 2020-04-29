
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# loading image
image = cv.imread('thresh2.png', 0)
cv.imshow('Original Imagen',image)

# Generating histogram
plt.title("Histogram") 
plt.hist(image.ravel(),256,[0,256]); 
plt.savefig('histogram2.png')
plt.show()

# Dimensions
heigth = image.shape[0]
width = image.shape[1]

# Creating matrix
healthy_cell = np.zeros((heigth, width, 1),np.uint8)

# Thresholding
for x in range(0, heigth, 1):
    for y in range(0, width, 1):
        color = image[x][y]
        if 130 < color < 170:
        	healthy_cell[x][y] = 255
        else:
        	healthy_cell[x][y] = 0        		


cv.imshow('Healthy',healthy_cell)

filename = 'resultado2.png'
  
# Saving the image 
cv.imwrite(filename, healthy_cell) 

print ("Presione una tecla para cerrar")
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1) 
exit()
