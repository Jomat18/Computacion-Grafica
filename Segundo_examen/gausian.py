import numpy as np

def gaussian_blur(img, m, n, sigma):
	gaussian = np.zeros((m, n))
	m = m//2
	n = n//2

	for x in range(-m, m+1):
		for y in range(-n, n+1):
			x1 = 2*np.pi*(sigma**2)
			x2 = np.exp(-(x**2+y**2)/(2*sigma**2))
			gaussian[x+m, y+n] = (1/x1)*x2

	return gaussian		