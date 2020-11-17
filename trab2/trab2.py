#Renato Alberto dos Santos
#Rodrigo Norio Tsuhako


import numpy as np
from matplotlib import pyplot as plt
import cv2
import time



saida = np.zeros([256, 256,3], dtype=np.uint8)

verde = np.zeros([256, 256], dtype=np.uint8)
verde[::1,::1] = np.linspace(0,255,num=256)

azul = np.ones([256, 256], dtype=np.uint8)
azul[::1,::1] = np.linspace(0,255,num=256)
azul = azul.T 
azul = np.flip(azul)

vermelho = np.zeros([256, 256], dtype=np.uint8)
vermelho[::1,::1] = np.linspace(0,255,num=256)
vermelho= vermelho.T


print("direita = 1, esquerda = 2, frente = 3, tras = 4, baixo = 5, cima = 6")

face = input("Escolha a face: ") 
fatia = input("Escolha a fatia de 0 a 255: ") 
op = int(face)
fatia = int(fatia)


#direita
if op == 1:
    verde[::1,::1] = np.linspace(255-fatia,255-fatia,num=256)
    vermelho = np.zeros([256, 256], dtype=np.uint8)
    vermelho[::1,::1] = np.linspace(255,0,num=256)
    saida[::1,::1] = cv2.merge((azul,verde,vermelho))

    nome = "direita"

#esquerda
if op == 2:
    verde[::1,::1] = np.linspace(fatia,fatia,num=256)
    vermelho = np.zeros([256, 256], dtype=np.uint8)
    vermelho[::1,::1] = np.linspace(0,255,num=256)
    saida[::1,::1] = cv2.merge((azul,verde,vermelho))

    nome = "esquerda"

#frente
if op == 3:
    vermelho[::1,::1] = np.linspace(255-fatia,255-fatia,num=256)
    saida[::1,::1] = cv2.merge((azul,verde,vermelho))

    nome = "frente"

#tras
if op == 4:
    vermelho[::1,::1] = np.linspace(fatia,fatia,num=256)
    saida[::1,::1] = cv2.merge((azul,verde,vermelho))

    nome = "tras"

#baixo    
if op == 5:
    azul[::1,::1] = np.linspace(fatia,fatia,num=256)
    saida[::1,::1] = cv2.merge((azul,verde,vermelho))

    nome = "baixo"

#cima
if op == 6:
    azul[::1,::1] = np.linspace(255-fatia,255-fatia,num=256)
    saida[::1,::1] = cv2.merge((azul,verde,vermelho))
    
    nome = "cima"

cv2.imshow(nome,saida)
cv2.waitKey(0)
cv2.destroyAllWindows()   








