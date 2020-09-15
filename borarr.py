import cv2
import numpy as np

#Texto añadido desde git hub
img = cv2.imread('objetos.jpg',0)#Imagen en escala de grises
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)#Para poder pintar en colores encima

#Coordenadas x,y,radio de todos los círculos encontrados
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,30,
                            param1=40,param2=40,minRadius=0,maxRadius=0)

#minRadius=Minimo radio detectado
#maxRadius=Maximo radio detectado
#param2= Parametros para deteccion de bordes
#param1=
#30=distancia minima entre centros
#imprimimos coordenadas
print(circles)
circles = np.uint16(np.around(circles)) #Redondea el número de circulos
for i in circles[0,:]:
    # Para dibujar el circulo exterior
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # Para dibujar el centro del círculo
    cv2.circle(cimg,(i[0],i[1]),2,(0,255,0),3)

cv2.imshow('Deteccion de circulos',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
