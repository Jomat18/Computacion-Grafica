import cv2
import numpy as np 
import matplotlib as plt


def sumaN(img1, img2):
	# Dimensions
	heigth = img2.shape[0]
	width = img2.shape[1]

	# Creating matrix
	img_out = np.zeros((heigth, width, 1),np.uint8)

	s1 = lambda x: x/2
	img1 = s1(img1)
	img2 = s1(img2)
	
	for x in range(0, heigth, 1):
	    for y in range(0, width, 1):
	        img_out[x][y] = img1[x][y] + img2[x][y] 
	#img_out = img1 + img2


	return img_out

def sumaC(img1, img2):
	# Dimensions
	heigth = img2.shape[0]
	width = img2.shape[1]

	# Creating matrix
	img_out = np.zeros((heigth, width, 1),np.uint8)

	s1 = lambda x: x/2
	img1 = s1(img1)
	img2 = s1(img2)
	
	#for x in range(0, heigth, 1):
	#    for y in range(0, width, 1):
	#        img_out[x][y] = img1[x][y] + img2[x][y] 
	#img_out = img1 + img2


	return img_out


if __name__ == "__main__":
	img1 = cv2.imread("add_1.jpg")
    img2 = cv2.imread("add_2.jpg")
    img_out = sumaC(img1,img2)
    cv2.imwrite("resul.jpg",img_out)

    #img1 = cv2.imread("add_1.jpg",0)
    #img2 = cv2.imread("add_2.jpg",0)
    #img_out = suma(img1,img2)
    #cv2.imwrite("resul.jpg",img_out)

