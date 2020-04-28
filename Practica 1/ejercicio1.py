
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

original = cv.imread('thresh1.png', 0)

plt.hist(original.ravel(),256,[0,256]); plt.show()

width = original.shape[0]
height = original.shape[1]

resultado = np.zeros((width, height, 1),np.uint8)

for i in range(height):
	for j in range(width-1):
		if original[i-1,j-1]>100 and original[i-1,j-1]<170:
			resultado[i-1,j-1] = 0 

cv.imshow('ImageWindow',resultado)
cv.waitKey(0) 
cv.destroyAllWindows()
cv.waitKey(1) 
exit()

