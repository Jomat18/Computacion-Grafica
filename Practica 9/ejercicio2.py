import sys
#import cv2 as cv
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def My_warpAffine(img, M, widthI, heightI):
	h, w, c = img.shape
	img_out = np.zeros((heightI, widthI, c), np.uint8)
	A = np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
	B = np.array([[M[1][2]],[M[0][2]]])
	for i in range(h):
		for j in range(w):
			X = np.array([[i],[j]])
			M1 = np.dot(A, X) + B
			M1 = M1.astype(int)
			if (M1[0,0] > 0 and M1[0,0] < heightI and M1[1,0] > 0 and M1[1,0] < widthI):
				for k in range(c):
					img_out[M1[0, 0], M1[1, 0]] =  img[i][j]
	return img_out

def Translate(img, x, y):
	h, w = img.shape[:2]
	A = np.identity(2)  
	B = [[x],[y]]
	M = np.concatenate((A, B), axis=1)
	img_out = My_warpAffine(img, M, w, h)
	return img_out

def Scale(img, x, y):
	h, w = img.shape[:2]
	A = np.float32([[x,0],[0,y]])
	B = [[0],[0]]
	M = np.concatenate((A, B), axis=1)
	img_out = My_warpAffine(img, M, w, h)
	return img_out

def Rotation(img, angle):
    h, w = img.shape[:2]
    img_c = (w / 2, h / 2)
    
    rad = math.radians(angle)
    sin = math.sin(rad)
    cos = math.cos(rad)
    b_w = int((h * abs(sin)) + (w * abs(cos)))
    b_h = int((h * abs(cos)) + (w * abs(sin)))

    mid_h = int((h+1)/2)
    mid_w = int((w+1)/2)

    A = np.float32([[cos,sin],[-sin,cos]])
    #B = [[((1-cos)*img_c[0])-(sin*img_c[1])],[(sin*img_c[1])+((1-sin)*img_c[0])]]
    B = [[((1-cos)*mid_w)-(sin*mid_h)],[(sin*mid_w)+(1-sin)*mid_h]]
    M = np.concatenate((A, B), axis=1)

    M[0, 2] += ((b_w / 2) - img_c[0])
    M[1, 2] += ((b_h / 2) - img_c[1])
    img_out = My_warpAffine(img, M, b_w, b_h)
    return img_out

def Shear(img, x, y):
	h, w = img.shape[:2]
	ix = math.tan(x * math.pi / 180)
	iy = math.tan(y * math.pi / 180)
	A = np.float32([[1,ix,0],[iy,1,0]])
	B = [[0],[0]]
	M = np.concatenate((A, B), axis=1)
	img_out = My_warpAffine(img, M, w+256, h+256)
	return img_out

if __name__ == "__main__":
	filename = sys.argv[1]
	#c = int(sys.argv[2])
	# Leer imagen
	img = cv2.imread(filename)
	heigth = img.shape[0]
	width = img.shape[1]

	img_out = np.zeros((heigth, width, 3),np.uint8)

	img_outT = Translate(img, 70, 70)
	cv2.imwrite('resultado_2T.png', img_outT)
	cv2.imshow('resultado_2T.png', img_outT)
	cv2.waitKey(0)

	img_outSc = Scale(img, 0.7, 0.8)
	cv2.imwrite('resultado_2Sc.png', img_outSc)
	cv2.imshow('resultado_2Sc.png', img_outSc)
	cv2.waitKey(0)

	img_outR = Rotation(img, 45)
	cv2.imwrite('resultado_2R.png', img_outR)
	cv2.imshow('resultado_2R.png', img_outR)
	cv2.waitKey(0)

	img_outSh = Shear(img, 20, 15)
	cv2.imwrite('resultado_2Sh.png', img_outSh)
	cv2.imshow('resultado_2Sh.png', img_outSh)
	cv2.waitKey(0)

	#cv2.imshow('1',nueva_imagen)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	exit()