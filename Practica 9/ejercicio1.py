import sys
#import cv2 as cv
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def TranslateW(img, x, y):
	h, w = img.shape[:2]
	A = np.identity(2)  
	B = [[x],[y]]
	M = np.concatenate((A, B), axis=1)
	img_out = cv2.warpAffine(img, M, (w, h))
	return img_out

def ScaleW(img, x, y):
	h, w = img.shape[:2]
	A = np.float32([[x,0],[0,y]])
	B = [[0],[0]]
	M = np.concatenate((A, B), axis=1)
	img_out = cv2.warpAffine(img, M, (w, h))
	return img_out

def RotationW(img, angle):
    h, w = img.shape[:2]
    img_c = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(img_c, angle, 1)
    rad = math.radians(angle)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))
    M[0, 2] += ((b_w / 2) - img_c[0])
    M[1, 2] += ((b_h / 2) - img_c[1])
    img_out = cv2.warpAffine(img, M, (b_w, b_h))
    return img_out

def shearW(img, x, y):
	h, w = img.shape[:2]
	ix = math.tan(x * math.pi / 180)
	iy = math.tan(y * math.pi / 180)
	M = np.float32([[1,ix,0],[iy,1,0]])
	img_out = cv2.warpAffine(img, M, (w+256, h+256))
	return img_out

if __name__ == "__main__":
	filename = sys.argv[1]
	#c = int(sys.argv[2])
	# Leer imagen
	img = cv2.imread(filename)
	heigth = img.shape[0]
	width = img.shape[1]

	img_out = np.zeros((heigth, width, 3),np.uint8)

	img_outT = TranslateW(img, 70, 70)
	cv2.imwrite('resultado_1T.png', img_outT)
	cv2.imshow('resultado_1T.png', img_outT)
	cv2.waitKey(0)

	img_outSc = ScaleW(img, 0.7, 0.8)
	cv2.imwrite('resultado_1Sc.png', img_outSc)
	cv2.imshow('resultado_1Sc.png', img_outSc)
	cv2.waitKey(0)

	img_outR = RotationW(img, 45)
	cv2.imwrite('resultado_1R.png', img_outR)
	cv2.imshow('resultado_1R.png', img_outR)
	cv2.waitKey(0)

	img_outSh = shearW(img, 20, 15)
	cv2.imwrite('resultado_1Sh.png', img_outSh)
	cv2.imshow('resultado_1Sh.png', img_outSh)
	cv2.waitKey(0)

	#cv2.imshow('1',nueva_imagen)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	exit()