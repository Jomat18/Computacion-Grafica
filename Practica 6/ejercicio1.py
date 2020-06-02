import sys
import cv2
import numpy as np 
import matplotlib as plt

def sumaN(img1, img2):
	# Dimensions
	heigth = img2.shape[0]
	width = img2.shape[1]
	if img1.shape[0]>img2.shape[0]:
		heigth = img2.shape[0]
	if img1.shape[1]>img2.shape[1]:
		width = img2.shape[1] 
	# Creating matrix
	img_out = np.zeros((heigth, width, 3), np.int)
	for x in range(0, heigth, 1):
	    for y in range(0, width, 1):
	        img_out[x][y] = img1[x][y] + img2[x][y]
	return img_out

def sumaS(img1, img2):
	# Dimensions
	heigth = img2.shape[0]
	width = img2.shape[1]
	if img1.shape[0]>img2.shape[0]:
		heigth = img2.shape[0]
	if img1.shape[1]>img2.shape[1]:
		width = img2.shape[1] 
	# Creating matrix
	img_out = np.zeros((heigth, width, 3), np.int)
	s1 = lambda x: x/2
	img1 = s1(img1)
	img2 = s1(img2)
	for x in range(0, heigth, 1):
	    for y in range(0, width, 1):
	        img_out[x][y] = img1[x][y] + img2[x][y]
	return img_out

def sumaC(img1, c):
	# Dimensions
	heigth = img1.shape[0]
	width = img1.shape[1]
	# Creating matrix
	img_out = np.zeros((heigth, width, 3), np.int)
	for x in range(0, heigth, 1):
	    for y in range(0, width, 1):
	        img_out[x][y] = img1[x][y] + c
	return img_out


if __name__ == "__main__":
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	img1 = cv2.imread(filename1)
	img2 = cv2.imread(filename2)
	img_out = sumaN(img1,img2)
	cv2.imwrite("resultado1N.jpg",img_out)
	img_out = sumaS(img1,img2)
	cv2.imwrite("resultado1S.jpg",img_out)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	exit()


