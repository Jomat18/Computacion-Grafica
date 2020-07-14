#!/usr/bin/python
import sys
import os 
import cv2
import numpy as np

filename = sys.argv[1]
img=cv2.imread(filename)

img_copy = img.copy()
r = 500.0 / img.shape[1]
dim = (500, int(img.shape[0] * r))
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Detectando bordes
#gray=cv2.GaussianBlur(gray,(5,5),0)  
gray=cv2.GaussianBlur(gray,(11,11),0) # kernelde 11x11 y sigma igual a 0, sigma determina la cantidad de blur
#edge=cv2.Canny(gray,100,200)
edge=cv2.Canny(gray, 75, 200)  #75 Threshold min y 200 Threshold max

# Coloreando bordes
contours,_=cv2.findContours(edge.copy(),1,1)
img_ = img.copy()
cv2.drawContours(img_,contours,-1,[0,255,0],2)

img_=cv2.resize(img_, (img_copy.shape[1], img_copy.shape[0]), interpolation = cv2.INTER_AREA)

# Guardando resultados
filename, file_extension = os.path.splitext(filename)
cv2.imwrite(filename+'_r'+file_extension, img_) 

cv2.destroyAllWindows()
cv2.waitKey(1) 
exit()