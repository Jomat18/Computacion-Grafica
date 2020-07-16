import sys
import cv2 
import numpy as np

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

    print (gaussian)        

    G = img.copy()          

    for i in range(m, height-m):
        for j in range(n, width-n):
            img_block = img[i-m:i+m+1, j-n:j+n+1]
            k_block = gaussian[0:m*2+1, 0:n*2+1]            

            suma = np.sum(np.multiply(k_block, img_block))
            G[i,j] = suma

    return G        


if __name__ == "__main__":

    filename = sys.argv[1]

    image = cv2.imread(filename, 0)

    output = gaussian_blur(image, (5, 5), 1)
    output2 = cv2.GaussianBlur(image, (5, 5), 0) 

    cv2.imshow('Gaussian', output)
    cv2.imshow('Gaussian2', output2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1) 
    exit()