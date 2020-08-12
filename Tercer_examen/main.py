import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

MIN_MATCH_COUNT = 10

#Cargar diferentes pares de imagenes
img_pairs = [("imagen1.jpg", "imagen2.jpg"),
             ("imagen2.jpg", "imagen3.jpg"),
             ("imagen1.jpg", "imagen3.jpg")]
counter = 0

#Reemplazar K con la matriz intrinsica
K = np.array([[518.86, 0., 285.58],
              [0., 519.47, 213.74],
              [0.,   0.,   1.]])

for img_pair_1, img_pair_2 in img_pairs:
    counter += 1
    img1=cv2.imread(img_pair_1)
    img2=cv2.imread(img_pair_2)

    ###1 - SIFT
    #Detectar las caracteristicas para ambas imagenes
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    #usar flann para realizar la coincidencia de caracteriticas
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    #Almacenar todas coincidencias con el ratio propuesto por Lowe 0.7
    good = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        p1 = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        p2 = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                       singlePointColor = None,
                       flags = 2)

    img_siftmatch = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
    cv2.imwrite('sift_match_' + str(counter) + '.png',img_siftmatch)

    #2 - Matriz esencial
    E, mask = cv2.findEssentialMat(p1, p2, K, cv2.RANSAC, 0.999, 1.0);

    matchesMask = mask.ravel().tolist()

    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor = None,
                       matchesMask = matchesMask,
                       flags = 2)

    img_inliermatch = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
    cv2.imwrite('inlier_match_' + str(counter) + '.png',img_inliermatch)
    print("Essential matrix:")
    print(E)

    #3 - Recuperar puntos

    points, R, t, mask = cv2.recoverPose(E, p1, p2)
    print("Rotation:")
    print(R)
    print("Translation:")
    print(t)
    # p1_tmp = np.expand_dims(np.squeeze(p1), 0)
    p1_tmp = np.ones([3, p1.shape[0]])
    p1_tmp[:2,:] = np.squeeze(p1).T
    p2_tmp = np.ones([3, p2.shape[0]])
    p2_tmp[:2,:] = np.squeeze(p2).T
    print((np.dot(R, p2_tmp) + t) - p1_tmp)

    #4 - Triangulacion
    #Calcular la matriz de proyeccion para ambas camaras
    M_r = np.hstack((R, t))
    M_l = np.hstack((np.eye(3, 3), np.zeros((3, 1))))

    P_l = np.dot(K,  M_l)
    P_r = np.dot(K,  M_r)

    #Puntos no distorsionados
    p1 = p1[np.asarray(matchesMask)==1,:,:]
    p2 = p2[np.asarray(matchesMask)==1,:,:]
    p1_un = cv2.undistortPoints(p1,K,None)
    p2_un = cv2.undistortPoints(p2,K,None)
    p1_un = np.squeeze(p1_un)
    p2_un = np.squeeze(p2_un)

    #Triangular puntos esto requiere puntos en coordenadas normalizadas
    point_4d_hom = cv2.triangulatePoints(P_l, P_r, p1_un.T, p2_un.T)
    point_3d = point_4d_hom / np.tile(point_4d_hom[-1, :], (4, 1))
    point_3d = point_3d[:3, :].T

    #5 - Puntos de Salida en 3D
    #Mostrar puntos 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for x, y, z in point_3d:
        ax.scatter(x, y, z, c="r", marker="o")

    plt.show()
    fig.savefig('3-D' + str(counter) + '.jpg')
