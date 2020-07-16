#!/usr/bin/python
import sys
import os 
import cv2
import numpy as np
import math  

#define horizontal and Vertical sobel kernels
#Gx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
#Gy = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

#Gx = np.array([[1, 0, 1],[0, 0, 0],[-1, 0, 1]])
#Gy = np.array([[1, 0, -1],[0, 0, 0],[-1, 0, 1]]) 


#Sx = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])*(1/3) # Derivacion Gausiana
#Sy = np.array([[1, 1, 1],[0, 0, 0],[-1, -1, -1]])*(1/3) # Derivacion Gausiana

Sx = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]]) # Derivacion Gausiana
Sy = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]]) # Derivacion Gausiana

#Gy = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]]) #Filtro Laplace


def grises(image):
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])      

#cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)

def thresholding(gray, a, b):

    heigth, width = gray.shape
    # Creating matrix
    harvests = np.zeros((heigth, width),np.uint8)

    # Thresholding
    for x in range(0, heigth, 1):
        for y in range(0, width, 1):
            color = gray[x][y]
            if a < color < b:
                harvests[x][y] = 255
            else:
                harvests[x][y] = 0              

    return harvests         


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
            #iterate over the filter
            img_block = X[i-H:i+H+1, j-W:j+W+1]
            k_block = F[0:H*2+1, 0:W*2+1]            
            
            suma = np.sum(np.multiply(k_block, img_block))
            out[i,j] = suma                     
    
    return out

def magnitude(sx, sy):
    height, width = sx.shape
    out = np.zeros((height, width))

    for i in range(height):
        for j in range(width):    
            out[i,j] = math.sqrt(sx[i,j]**2 + sy[i,j]**2)
            

    # supression
    ''' 
    for i in range(1,height-1):
        for j in range(1,width-1):

            if (math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i-1,j-1]/sx[i-1,j-1]) and 
                math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i+1,j+1]/sx[i+1,j+1])):

                if (out[i,j] > out[i-1,j-1] and out[i,j] > out[i+1,j+1]):
                    out[i-1,j-1] = 0
                    out[i+1,j+1] = 0

                else:
                    out[i,j] = 0    

            elif (math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i-1,j]/sx[i-1,j]) and
                math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i+1,j]/sx[i+1,j])):    
                if (out[i,j] > out[i-1,j] and out[i,j] > out[i+1,j]):
                    out[i-1,j] = 0
                    out[i+1,j] = 0

                else:
                    out[i,j] = 0    

            elif (math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i-1,j+1]/sx[i-1,j+1]) and 
                math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i+1,j-1]/sx[i+1,j-1])):    
                if (out[i,j] > out[i-1,j+1] and out[i,j] > out[i+1,j-1]):
                    out[i-1,j+1] = 0
                    out[i+1,j-1] = 0

                else:
                    out[i,j] = 0        
            
            else: 
                if (math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i,j-1]/sx[i,j-1]) and
                 math.atan(sy[i,j]/sx[i,j])==math.atan(sy[i,j+1]/sx[i,j+1])):   
                    if (out[i,j] > out[i,j-1] and out[i,j] > out[i,j+1]):
                        out[i,j-1] = 0
                        out[i,j+1] = 0

                    else:
                        out[i,j] = 0            
    '''     
  
    return out

def gaussian_blur(img, k, sigma):
    height, width = img.shape   
    m = k[0]
    n = k[1]

    gaussian = np.zeros((m, n))

    m = m//2
    n = n//2

    for x in range(-m, m+1):
        for y in range(-n, n+1):
            x1 = 2*np.pi*(sigma**2)
            x2 = np.exp(-(x**2+y**2)/(2*sigma**2))
            gaussian[x+m, y+n] = (1/x1)*x2

    G = img.copy()          

    for i in range(m, height-m):
        for j in range(n, width-n):
            img_block = img[i-m:i+m+1, j-n:j+n+1]
            k_block = gaussian[0:m*2+1, 0:n*2+1]            
            
            suma = np.sum(np.multiply(k_block, img_block))
            G[i,j] = suma

    return G    


filename = sys.argv[1]
img=cv2.imread(filename)

img_copy = img.copy()
r = 500.0 / img.shape[1]
dim = (500, int(img.shape[0] * r))
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
  
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = grises(img)   

# Detectando bordes
# Gaussian Blur Opencv
#gray=cv2.GaussianBlur(gray,(5,5),0)  
#gray=cv2.GaussianBlur(gray,(11,11),0) # kernelde 11x11 y sigma igual a 0, sigma determina la cantidad de blur

# Gaussian Blur
gray=gaussian_blur(gray,(11, 11), 2) #2.6  Smoothing 

# Canny
sob_x = convolve(gray, Sx) 
sob_y = convolve(gray, Sy) 
out = magnitude(sob_x, sob_y)
edge = thresholding(out, 120, 200)  #MinThreshold and MaxThreshold

# Canny Opencv
#edge=cv2.Canny(gray, 75, 200)  #75 Threshold min y 200 Threshold max
#edge=cv2.Canny(gray,100,200) #MinThreshold and MaxThreshold

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