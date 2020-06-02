import cv2
import numpy as np 
import matplotlib as plt


def SustraccionN(img1, img2, c):
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
	        aux = abs(img1[x][y] - img2[x][y])
	        img_out[x][y] = abs(aux - c)
	return img_out


img1 = cv2.imread("sub_10.jpg")
img2 = cv2.imread("sub_11.jpg")
c =  int(input())
img_out = SustraccionN(img1,img2,c)
cv2.imwrite("resultado 4.jpg",img_out)




