#   Estos codigos abren ventanas con imagenes y esperan a que se presione una tecla para cerrarlas
#   por lo tanto no se pueden ejecutar en el codspace de github, almenos para mi se ah presentado ese problema

#Filtro Kernel
import numpy as np
import cv2
np.zeros((3, 3))
kernel = np.array([[1,1,1],[-1,-1,-1],[0,0,0]])
imagen = cv2.imread('Tralalero.png',0)
bordes= np.zeros_like(imagen)

resolucion = 45
m,n = imagen.shape
for i in range(m-2):
    for j in range(n-2):
        res = np.sum(imagen[i:i+3,j:j+3]*kernel)
        if res>resolucion:
            bordes[i,j] = 255

ikernel = np.transpose(kernel)

bordes1 = np.zeros_like(imagen)

for i in range(m-2):
     for j in range(n-2):
         res = np.sum(imagen[i:i+3,j:j+3]*ikernel)
         if res>resolucion:
            bordes1[i,j] = 255

bordest = bordes + bordes1

cv2.imshow('Original', imagen)
cv2.imshow('Bordes', bordes)
cv2.imshow('Bordes1', bordes1)
cv2.imshow('Bordest', bordest)
cv2.waitKey(0)
cv2.destroyAllWindows()
