#!/usr/bin/python
import sys
import os 
import cv2
import numpy as np
 
def transform(pos):
# Esta función se utiliza para encontrar las esquinas del objeto y las dimensiones del objeto.
# para la trasformacion perpectiva
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


#define kernal convolution function
# with image X and filter F
def convolve(X, F):

    # height and width of the image
    X_height = X.shape[0]
    X_width = X.shape[1]
    
    # height and width of the filter
    F_height = F.shape[0]
    F_width = F.shape[1]
    
    H = (F_height - 1) // 2
    W = (F_width - 1) // 2
    
    #output numpy matrix with height and width
    out = np.zeros((X_height, X_width))
    #iterate over all the pixel of image X
    for i in np.arange(H, X_height-H):
        for j in np.arange(W, X_width-W):
            sum = 0
            #iterate over the filter
            for k in np.arange(-H, H+1):
                for l in np.arange(-W, W+1):
                    #get the corresponding value from image and filter
                    a = X[i+k, j+l]
                    w = F[H+k, W+l]
                    sum += (w * a)
            out[i,j] = sum
    #return convolution  
    return out
    

filename = sys.argv[1]
img=cv2.imread(filename)

r = 500.0 / img.shape[1]
dim = (500, int(img.shape[0] * r))
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
# Su funcion
#normalizing the vectors
Gx = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
Gy = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
sob_x = convolve(img, Gx) 
sob_y = convolve(img, Gy) 

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(11,11),0)
edge=cv2.Canny(gray, 75, 200)  

contours,_=cv2.findContours(edge.copy(),1,1)
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
 
# Tranformacion perspectiva 
size=img.shape
w,h,arr=transform(approx)
 
pts2=np.float32([[0,0],[w,0],[0,h],[w,h]])
pts1=np.float32(arr)
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(w,h))

image=cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(w,h),interpolation = cv2.INTER_AREA)

# Guardando resultados
filename, file_extension = os.path.splitext(filename)
cv2.imwrite(filename+'_r'+file_extension, image) 

cv2.destroyAllWindows()
cv2.waitKey(1) 
exit()