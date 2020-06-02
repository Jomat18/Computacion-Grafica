import sys
import cv2
import numpy as np 
import matplotlib as plt
import math
def subtraccion(img1, img2, c, img_out):
	for x in range(0, heigth, 1):
		for y in range(0, width, 1):
			img_out[x][y] = ((img1[x][y]/2) - (img2[x][y]/2)) + c
	return img_out
def subtraccionC(img1, c, img_out):
	for x in range(0, heigth, 1):
		for y in range(0, width, 1):
			img_out[x][y] = img1[x][y] + c
	return img_out
def subtraccionR(img1, img2, img_out):
	c=100
	for x in range(0, heigth, 1):
		for y in range(0, width, 1):
			img_out[x][y] = ((img1[x][y]/2) - (img2[x][y]/2))+c
	#threshold
	threshold=90
	for x in range(0, heigth, 1):
		for y in range(0, width, 1):
			if (img_out[x][y]<threshold).all():
				img_out[x][y]=0
			else:
				img_out[x][y]=255
	return img_out
if __name__ == "__main__":
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	img1 = cv2.imread(filename1)
	img2 = cv2.imread(filename2)
	# Dimensions
	heigth = img2.shape[0]
	width = img2.shape[1]
	if img1.shape[0]>img2.shape[0]:
		heigth = img2.shape[0]
	if img1.shape[1]>img2.shape[1]:
		width = img2.shape[1] 
	# Creating matrix
	img_out = np.zeros((heigth, width, 3), np.int)
	c=100
	img_out = subtraccion(img1, img2, c, img_out)
	cv2.imwrite("resultado3.jpg",img_out)
	#thresholding
	img_outT = np.zeros((heigth, width, 3), np.int)
	img_outT = subtraccionR(img1, img2, img_outT)
	cv2.imwrite("resultado3T.jpg",img_outT)
