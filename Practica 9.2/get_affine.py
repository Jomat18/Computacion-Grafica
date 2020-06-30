import cv2 as cv
import numpy as np
import matplotlib as plt
import math
from matplotlib import pyplot as plts



def my_getAffine(src,dst):
    A = np.zeros((3,2))
    Ones = np.ones((3,1))
    Zeros = np.zeros((3,3))
    src1= np.concatenate((src,Ones,Zeros),axis=1)
    src2= np.concatenate((Zeros,src,Ones),axis=1)
    A = np.concatenate((src1,src2),axis=0)
    B = np.float64([[dst[0,0]],[dst[1,0]],[dst[2,0]],[dst[0,1]],[dst[1,1]],[dst[2,1]]])
    X = np.zeros((6))
    cv.solve(A,B,X)
    M = np.zeros((2,3))
    a = 0
    for i in range (2):
        for j in range(3):
            M[i,j] = X[a]
            a+=1
    return M


img = cv.imread("draw.png")
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

MM =  my_getAffine(pts1,pts2)
M = cv.getAffineTransform(pts1,pts2)
print(MM)
print(M)

dst = cv.warpAffine(img,M,(cols,rows))
plts.subplot(121),plts.imshow(img),plts.title("Input")
plts.subplot(122),plts.imshow(dst),plts.title("Output")
plts.show()