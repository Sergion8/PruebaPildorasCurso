
# Programa que pasa a escala de grises una foto

import cv2

#Modificado prueba Git
a = 2
#Fin pruebas Git

cv2.namedWindow("Imagen_1") #le damos nombre a la ventana
image = cv2.imread("monster.png") #leemos una imagen desde el disco (tiene que existir)
ancho,alto,canales = image.shape #propiedades de la imagen
print (ancho,alto,canales)
cv2.imshow("Imagen_1", image) #mostramos la imagen en la ventana creada
imagegrey = cv2.imread("monster.png",0)#0 = cargamos pero ahora en escala grises
cv2.namedWindow("Imagen_gris")#creamos una segunda ventana para la imagen en grises
cv2.imshow("Imagen_gris", imagegrey) #mostramos la imagen en la ventana creada
cv2.imwrite("monster_gris.jpg",imagegrey) #guardamos la imagen en grises
cv2.waitKey(0)#esperamos pulsación de una tecla
cv2.destroyAllWindows()#salimos


    
