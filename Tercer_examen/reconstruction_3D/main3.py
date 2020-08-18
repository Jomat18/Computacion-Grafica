import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2

import structure
import processor
import features

fig2 = plt.figure()
fig2.suptitle('3D reconstruido', fontsize=16)
ax = fig2.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
      

img1=cv2.imread("viff.000.ppm")
img2=cv2.imread("viff.001.ppm")             

pts1, pts2 = features.find_correspondence_points(img1, img2)
points1 = processor.cart2hom(pts1)
points2 = processor.cart2hom(pts2)

fig, ax2 = plt.subplots(1, 2)
ax2[0].autoscale_view('tight')
ax2[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
ax2[0].plot(points1[0], points1[1], 'g.')
ax2[1].autoscale_view('tight')
ax2[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
ax2[1].plot(points2[0], points2[1], 'g.')
fig.show()

height, width, ch = img1.shape
intrinsic = np.array([  
[2360, 0, width / 2],
[0, 2360, height / 2],
[0, 0, 1]])


points1n = np.dot(np.linalg.inv(intrinsic), points1)
points2n = np.dot(np.linalg.inv(intrinsic), points2)
E = structure.compute_essential_normalized(points1n, points2n)
print('Matriz Esencial:', (-E / E[0][1]))

P1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
P2s = structure.compute_P_from_essential(E)

ind = -1
for i, P2 in enumerate(P2s):

    d1 = structure.reconstruct_one_point(
        points1n[:, 0], points2n[:, 0], P1, P2)

    P2_homogenous = np.linalg.inv(np.vstack([P2, [0, 0, 0, 1]]))
    d2 = np.dot(P2_homogenous[:3, :4], d1)

    if d1[2] > 0 and d2[2] > 0:
        ind = i

P2 = np.linalg.inv(np.vstack([P2s[ind], [0, 0, 0, 1]]))[:3, :4]

tripoints3d = structure.linear_triangulation(points1n, points2n, P1, P2)

ax.scatter(tripoints3d[0], tripoints3d[1], tripoints3d[2], c="b", marker="o")

plt.show()
