#!/usr/bin/python
import sys
import os 
import cv2
import numpy as np

def thresholding_adaptativo(image, windows_size, constant):
	heigth, width = image.shape

	boundary = int(windows_size/2)

	output = image.copy()

	for x in range(heigth):
	    for y in range(width):

	    	x_i = x-boundary
	    	y_i = y-boundary
	    	x_f = x+boundary
	    	y_f = y+boundary

	    	if x_i<0:
	    		x_i = 0

	    	if x_f>heigth:
	    		x_f = heigth

	    	if y_i<0:
	    		y_i = 0

	    	if y_f>width:
	    		y_f = width

	    	box = image[x_i:x_f, y_i:y_f]					    			

	    	if image[x][y] < box.mean() - constant:
	    		output[x][y] = 0
	    	else:
	    		output[x][y] = 255        		
	  
	return output

def contrast(img):
	heigth, width = img.shape

	Contrast = img.copy()

	colores = np.zeros((heigth, width, 1),np.uint8)

	for x in range(heigth):
	    for y in range(width):
	    	colores[x][y] = img[x][y]

	cantidad = 0
	colores = np.sort(colores, axis = None)   
	lower = int((cantidad/100)*(heigth*width))
	higher = int(((100-cantidad)/100)*(heigth*width))

	a = 0
	b = 255
	c = int(colores[lower])
	d = int(colores[higher-1])

	temp = (b - a)/(d - c)

	for x in range(0, heigth, 1):
	    for y in range(0, width, 1):
	        valor = (img[x][y] - c) * temp + a

	        if valor>255:
	            valor = 255
	        if valor<0:
	            valor = 0    

	        Contrast[x][y] = valor

	return Contrast

 
def transform(pos):
# This function is used to find the corners of the object and the dimensions of the object
    pts=[]
    n=len(pos)
    for i in range(n):
        pts.append(list(pos[i][0]))
       
    sums={}
    diffs={}
    tl=tr=bl=br=0
    for i in pts:
        x=i[0]
        y=i[1]
        sum=x+y
        diff=y-x
        sums[sum]=i
        diffs[diff]=i
    sums=sorted(sums.items())
    diffs=sorted(diffs.items())
    n=len(sums)
    rect=[sums[0][1],diffs[0][1],diffs[n-1][1],sums[n-1][1]]
    #      top-left   top-right   bottom-left   bottom-right
   
    h1=np.sqrt((rect[0][0]-rect[2][0])**2 + (rect[0][1]-rect[2][1])**2)     #height of left side
    h2=np.sqrt((rect[1][0]-rect[3][0])**2 + (rect[1][1]-rect[3][1])**2)     #height of right side
    h=max(h1,h2)
   
    w1=np.sqrt((rect[0][0]-rect[1][0])**2 + (rect[0][1]-rect[1][1])**2)     #width of upper side
    w2=np.sqrt((rect[2][0]-rect[3][0])**2 + (rect[2][1]-rect[3][1])**2)     #width of lower side
    w=max(w1,w2)
   
    return int(w),int(h),rect

 
# loading image
filename = sys.argv[1]

img=cv2.imread(filename)
r=500.0 / img.shape[1]
dim=(500, int(img.shape[0] * r))
img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
cv2.imshow('imagen',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray=cv2.GaussianBlur(gray,(5,5),0)  #(5,5) is the kernel size and 0 is sigma that determines the amount of blur
gray=cv2.GaussianBlur(gray,(11,11),0) #tamaño del nucleo, sigma para x e y
#edge=cv2.Canny(gray,100,200)
edge=cv2.Canny(gray, 75, 200)  #MinThreshold and MaxThreshold

contours,_=cv2.findContours(edge.copy(),1,1)
img_ = img.copy()
cv2.drawContours(img_,contours,-1,[0,255,0],2)
cv2.imshow('contornos',img_)


n=len(contours)
max_area=0
pos=0
for i in contours:
    area=cv2.contourArea(i)
    if area>max_area:
        max_area=area
        pos=i
peri=cv2.arcLength(pos,True)
approx=cv2.approxPolyDP(pos,0.02*peri,True)
 
size=img.shape
w,h,arr=transform(approx)
 
pts2=np.float32([[0,0],[w,0],[0,h],[w,h]])
pts1=np.float32(arr)
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(w,h))
image=cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
#image=cv2.adaptiveThreshold(image,255,1,0,11,2)
image = cv2.resize(image,(w,h),interpolation = cv2.INTER_AREA)
#image = contrast(image)
#image = thresholding_adaptativo(image, 10, 2)


filename, file_extension = os.path.splitext(filename)
cv.imwrite(filename+'_r'+file_extension, image) 

cv.destroyAllWindows()
cv.waitKey(1) 
exit()