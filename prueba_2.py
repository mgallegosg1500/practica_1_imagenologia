import cv2 
import numpy as np
import matplotlib.pyplot as plt

import cv2


ip = 'torax.jpg'
cap = cv2.VideoCapture(ip)

leido, frame = cap.read()

if leido == True:
	cv2.imwrite("foto.png", frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

"""
	Finalmente liberamos o soltamos la cámara
"""
cap.release()

#gris = cv2.COLOR_BGR2GRAY(frame)
gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

[fil, col] = gris.shape
histo = np.zeros([1,256])
for i in range (fil):
    for j in range(col):
        pix = np.uint8(gris[i,j]*255)
        
        histo[0,pix] = histo[0,pix] +1
rango = np.linspace(0,255,256)
rango = np.transpose(rango)
pframe = np.zeros([fil,col,3])
pframe[:,:,0] = frame[:,:,2]
pframe[:,:,1] = frame[:,:,1]
pframe[:,:,2] = frame[:,:,0]
pframe = np.uint8(pframe)

pro = histo/(fil*col)
k = 0
suma = np.zeros([1,256])
for i in range(256):
    k = pro[0,i] + k
    suma[0,i] = k
plt.plot(suma[0])
#[fil, col, capa] = frame.shape
newimg = np.zeros(gris.shape)
for i in range (fil):
    for j in range(col):
        newimg[i,j] = suma[0,np.uint8(gris[i,j])]

plt.figure(1)
plt.subplot(121)
plt.imshow(pframe)
plt.title('original')
plt.subplot(122)
plt.imshow(newimg, cmap = 'gray')
plt.title('gris')
plt.show()

plt.figure(2)
plt.subplot(121)
plt.plot(rango, histo[0])
plt.title('Histograma')
plt.subplot(122)
plt.imshow(newimg,cmap = 'gray')
plt.title('final')
plt.show()
