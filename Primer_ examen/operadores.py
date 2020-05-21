import sys
import cv2 as cv
from logaritmo import operador_logaritmo

if __name__ == "__main__":

    filename = sys.argv[1]
    c = int(sys.argv[2])

    # Leer imagen
    img = cv.imread(filename , cv.IMREAD_GRAYSCALE)

    # Funciones
    nueva_imagen = operador_logaritmo(c, img)

    # Guardando la imagen del resultado
    cv.imwrite(filename, nueva_imagen) 
    
    cv.destroyAllWindows()
    cv.waitKey(1) 
    exit()