import cv2 
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('C:/Users/arman/OneDrive/Documents/Practice/colores.jpg')
gris = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
bordes = cv2.Canny(imagen, 100, 200)

cv2.imshow ('Imagen original', imagen)
cv2.imshow ('Imagen bordes', bordes)
cv2.imshow ('Imagen color gris', gris)

cv2.waitKey(0)

cv2.destroyAllWindows()