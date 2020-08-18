import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Cargar diferentes pares de imagenes
img_pairs = [("imagen1.jpg", "imagen2.jpg"),
             ("imagen2.jpg", "imagen3.jpg"),
             ("imagen1.jpg", "imagen3.jpg")]


for img_pair_1, img_pair_2 in img_pairs:    

    img1 = cv2.imread(img_pair_1)        
    img2 = cv2.imread(img_pair_2)        

    sift = cv2.xfeatures2d.SIFT_create()

    # Número de puntos a igualar
    top_matches = 800

    # Encuentrar los puntos clave y descriptores con SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)


    # Dibujar puntos clave
    img_1=cv2.drawKeypoints(img1,kp1,img1,color=(0,255,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img_2=cv2.drawKeypoints(img2,kp2,img2,color=(0,255,0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Mostrar los descriptores de puntos clave
    img_1=cv2.resize(img_1, (1200, 800))
    plt.imshow(img_1)
    plt.show()

    img_2=cv2.resize(img_2, (1200, 800))
    plt.imshow(img_2)
    plt.show()

    # Número de descriptores de puntos clave en las imagenes
    keypoint,w1=des1.shape
    keypoint,w2=des2.shape
    print ("Numero de keypoint")
    print (keypoint)

    # BFMatcher con parametros por defecto Brute-Force Matcher
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)
    #print (matches)

    good = []
    for m,n in matches:
        if m.distance < 0.8 * n.distance:  #H/F
            good.append(m)

    # Ordenando según el concepto de distancia mínima en orden ascendente
    topMatches=sorted(good,key=lambda x:x.distance)

    # Crear un mapa para las mejores coincidencias 
    img_match = cv2.drawMatches(img1,kp1,img2,kp2,topMatches[:top_matches],None,flags=2)

    # Mostrando
    image_match_display = cv2.resize(img_match, (1200,800))
    plt.imshow(image_match_display)
    plt.show()

    # Elegir solo las mejores opciones
    pts1 = np.float32([ kp1[m.queryIdx].pt for m in topMatches[:top_matches] ]).reshape(-1,1,2)
    pts2 = np.float32([ kp2[m.trainIdx].pt for m in topMatches[:top_matches] ]).reshape(-1,1,2)

    #print pts2

    #print pts1.shape

    # Creación de la matriz intrínseca K
    K=[[1229.0,0.0,360.0,0.0,640.0,1153.0,0,0,1]]
    K=np.array(K).reshape(3,3)
    #print K

    # puntos clave que no distorsionan para considerar las distorsiones de la cámara
    upts1 = cv2.undistortPoints(pts1, K, distCoeffs=None)
    upts2 = cv2.undistortPoints(pts2, K, distCoeffs=None)

    # Calculando la matrix esencial
    E, mask = cv2.findEssentialMat(pts1,pts2,1229.0,(360.0, 640.0),cv2.RANSAC,0.999,1.0)
    print ("Matriz Esencial")
    print (E)

    K_normal=[[1.0,0.0,0.0,0.0,1.0,0.0,0,0,1]]
    K_normal=np.array(K).reshape(3,3)

    # Descomponiendo E para obtener R y T
    # descomposición en valores singulares o SVD
    Points, R,T,mask = cv2.recoverPose(E, upts1, upts2, K_normal)
    print ("Matriz de Rotacion")
    print (R)
    print ("Matriz de Traslacion")
    print (T)

    # Haciendo las matrices de proyección: R-> izquierda; T-> derecha
    proj_mat2 = np.hstack((R,T))

    # Matriz de proyección de la primera camara en el origen
    # Después de este proceso se obtiene una de las dos matrices de cámara, para conseguir
    # la segunda matriz hay que asumir que una de las cámaras es fija y canónica (no tiene
    # rotación ni traslación), la siguiente matriz representa a esta cámara:
    proj_mat1 = np.array([ [1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0]])

	# Cambiando las dimensiones de upts para la triangulación.
    upts1_array = np.array(upts1).reshape(2,len(pts1))
    upts2_array = np.array(upts2).reshape(2,len(pts2))


    # Triangulacion
    # Conversión de coordenadas homogéneas 4D en coordenadas de imagen
    P_l = np.dot(K,  proj_mat1)
    P_r = np.dot(K,  proj_mat2)

    pts4d = cv2.triangulatePoints(P_l, P_r, upts1, upts2)

    point_4d_nonHom = pts4d / np.tile(pts4d[-1, :], (4, 1))
    point_3d = point_4d_nonHom[:3, :].T
    #print point_3d

    #Exportando a txt
    #np.savetxt("points_3d.csv", point_3d, delimiter="," , usecols=np.arange(0,2))

    #5 - Puntos de Salida en 3D
    #Mostrar puntos 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for x, y, z in point_3d:
        ax.scatter(x, y, z, c="g", marker="o")

    plt.show()
    print()