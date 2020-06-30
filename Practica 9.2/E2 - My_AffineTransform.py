import cv2
import numpy as np 
import matplotlib.pyplot as plt
#import matplotlib as plt

img = cv2.imread('drawing.png')
rows,cols,ch = img.shape

def My_warpAffine(img, M, widthI, heightI):
	h, w, c = img.shape
	img_out = np.zeros((heightI, widthI, c), np.uint8)
	A = np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
	B = np.array([[M[1][2]],[M[0][2]]])
	P = 0
	for i in range(h):
		for j in range(w):
			X = np.array([[i],[j]])
			M1 = (np.dot(A, X) + B)
			M1 = M1.astype(int)
			if (M1[0,0] > 0 and M1[0,0] < heightI and M1[1,0] > 0 and M1[1,0] < widthI):
				for k in range(c):
					img_out[M1[0, 0], M1[1, 0]] =  img[i][j]
	return img_out

def My_affineTransformV0(pts1,pts2):
	A = [[pts1[0][0],pts1[0][1],1],[pts1[1][0],pts1[1][1],1],[pts1[2][0],pts1[2][1],1]]
	B=[pts2[0][0],pts2[1][0],pts2[2][0]]
	X = np.linalg.inv(A).dot(B)
	A1 = [[pts1[0][0],pts1[0][1],1],[pts1[1][0],pts1[1][1],1],[pts1[2][0],pts1[2][1],1]]
	B1=[pts2[0][1],pts2[1][1],pts2[2][1]]
	X1 = np.linalg.inv(A1).dot(B1)
	R = [[X[0],X[1],X[2]],[X1[0],X1[1],X1[2]]]
	return R

def My_affineTransform(pts1,pts2):
	R = []
	for i in range(2):
		A = []
		for j in range(len(pts1)):
			A_ = [pts1[j][0],pts1[j][1],1]
			A.append(A_)
		B = [pts2[0][i],pts2[1][i],pts2[2][i]]
		X = np.linalg.inv(A).dot(B)
		#X = np.linalg.solve(A,B)
		R.append([X[0],X[1],X[2]])
	return R

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = My_affineTransform(pts1,pts2)
dst = cv2.warpAffine(img,np.float32(M),(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.savefig('R2_.png')
plt.show()
