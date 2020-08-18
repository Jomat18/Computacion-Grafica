import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

MIN_MATCH_COUNT = 25 #10

# Cargar diferentes pares de imagenes

img_pairs = [("imagen1.jpg", "imagen2.jpg"),
             ("imagen2.jpg", "imagen3.jpg"),
             ("imagen1.jpg", "imagen3.jpg")]

counter = 0

# Creando la matriz intrinseca K
# E = K'*F*K
# K es la matriz de la camara equilibrada, F la matriz fundamental y E la matriz esencial
K = np.array([[518.86, 0., 285.58],   #[ fm_x   0     C_x] 
              [0., 519.47, 213.74],   #[ 0      fm_y  C_y]
              [0.,   0.,   1.]])      #[ 0      0      1 ]


for img_pair_1, img_pair_2 in img_pairs:
    counter += 1
    img1=cv2.imread(img_pair_1)
    img2=cv2.imread(img_pair_2)

    ###1 - SIFT
    #Detectar las caracteristicas o keypoints  y descriptores para ambas imagenes
    sift = cv2.xfeatures2d.SIFT_create() 

    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # Dibujar los keypoints de las imagenes
    img_1=img1.copy()
    img_2=img2.copy() 
    img_1=cv2.drawKeypoints(img_1,kp1,img_1,color=(0,255,0)) 
    img_2=cv2.drawKeypoints(img_2,kp2,img_2,color=(0,255,0))

    img_1=cv2.resize(img_1, (1200, 800))
    plt.imshow(img_1)
    plt.show()

    img_2=cv2.resize(img_2, (1200, 800))
    plt.imshow(img_2)
    plt.show()

    #keypoint,w1=des1.shape
    #keypoint,w2=des2.shape

    # Usar flann para realizar la coincidencia de caracteriticas
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # Las parejas con menor distancia son las que queremos.
    #matches = sorted(matches, key = lambda x : x.distance)  #matches[:50]

    # Almacenar todas coincidencias con el ratio propuesto por Lowe 0.7
    good = []
    for m,n in matches:
        if m.distance < 0.8 * n.distance:  #H/F
            good.append(m)


    # recuperación de las coordenadas de la imagen de puntos clave coincidentes
    if len(good)>MIN_MATCH_COUNT:
        p1 = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        p2 = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)


    print ("Numero de Matches")
    print (len(good))    

    draw_params = dict(matchColor = (0,255,0), # color verde
                       singlePointColor = (0,255,0),
                       flags = 2)

    
    img_siftmatch = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
    cv2.imwrite('sift_match_' + str(counter) + '.png',img_siftmatch)

    img_siftmatch_display = cv2.resize(img_siftmatch, (1200,800))
    plt.imshow(img_siftmatch_display)
    plt.show()

    #2 - Matriz esencial    
    # Ransac elimina las correspondencias atípicas
    E, mask = cv2.findEssentialMat(p1, p2, K, cv2.RANSAC, 0.999, 1.0);

    matchesMask = mask.ravel().tolist()
  

    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor = None,
                       matchesMask = matchesMask,
                       flags = 2)

    # emparejamiento interno, correspondencias de características internas
    img_inliermatch = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
    cv2.imwrite('inlier_match_' + str(counter) + '.png',img_inliermatch)
    print("Matriz Esencial:")
    print(E)

    #3 - Recuperar puntos

    # K_normal=[[1.0,0.0,0.0,0.0,1.0,0.0,0,0,1]]
    # K_normal=np.array(K).reshape(3,3)

    # Descomponiendo E para obtener R y T, Reconstruccion inicial
    points, R, t, mask = cv2.recoverPose(E, p1, p2)
    print("Matriz de Rotacion:")
    print(R)
    print("Matriz de Translacion:")
    print(t)

    p1_tmp = np.ones([3, p1.shape[0]])
    p1_tmp[:2,:] = np.squeeze(p1).T
    p2_tmp = np.ones([3, p2.shape[0]])
    p2_tmp[:2,:] = np.squeeze(p2).T
    #print((np.dot(R, p2_tmp) + t) - p1_tmp)

    #4 - Triangulacion lineal
    # Calculamos la matriz de Proyecciones para ambas camaras
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

    # Triangular puntos esto requiere puntos en coordenadas normalizadas
    # triangulatePoints es un método puro basado en SVD.
    point_4d_hom = cv2.triangulatePoints(P_l, P_r, p1_un.T, p2_un.T)
    point_3d = point_4d_hom / np.tile(point_4d_hom[-1, :], (4, 1))
    point_3d = point_3d[:3, :].T

    #5 - Puntos de Salida en 3D
    #Mostrar puntos 3D
    fig = plt.figure()
    fig.suptitle('3D reconstruido', fontsize=16)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for x, y, z in point_3d:
        ax.scatter(x, y, z, c="b", marker="o")

    plt.show()        
    print ()    