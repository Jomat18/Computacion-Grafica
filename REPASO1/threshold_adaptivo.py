import cv2 as cv
import numpy as np
# el ,0 lo tranforma a escala de grises la imagen yee
img=cv.imread('paper6.jpg',0)
ancho=img.shape[0]
alto=img.shape[1]
rows,cols=img.shape
threshold=90
windows=11
c=2
img_out=np.zeros((ancho, alto, 1),np.uint8)
#int threshold2=150
for i in range(rows):
   for j in range(cols):
   		y0=i-int(windows/2)
   		y1=i+int(windows/2)+1
   		x0=j-int(windows/2)
   		x1=j+int(windows/2)+1

   		if y0<0:
   			y0=0
   		if y1>rows:
   			y1=rows
   		if x0<0:
   			x0=0
   		if x1>cols:
   			x1=cols

   		block=img[y0:y1, x0:x1]
   		thresh=np.mean(block) - c
   		if img[i,j]<thresh:
   			img_out[i,j]=0
   		else:
   			img_out[i,j]=255


cv.imshow('image',img_out)
cv.imwrite("resul_threshold_apdativo.jpg",img_out)
cv.waitKey(0)
