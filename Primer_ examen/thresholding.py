import sys
import cv2 as cv
import numpy as np

# loading image
filename = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

image = cv.imread(filename)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Dimensions
heigth = image.shape[0]
width = image.shape[1]

# Creating matrix
harvests = np.zeros((heigth, width, 3),np.uint8)

# Thresholding
for x in range(0, heigth, 1):
    for y in range(0, width, 1):
        color = gray[x][y]
        if a < color < b:
        	harvests[x][y] = 255
        else:
        	harvests[x][y] = 0        		

  
# Saving the image 
cv.imwrite(filename, harvests) 

cv.destroyAllWindows()
cv.waitKey(1) 
exit()