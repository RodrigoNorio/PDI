#from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import cv2
import time


#carrega imagem
def carregarimagem():
    imagem = input('Digite o nome da imagem: ')
    img = cv2.imread(imagem)
    matimg = np.array(img)
    
    return matimg, img

#calcula matriz
def calculamatriz(newimg, auxiliar, matimg, saida):
    for i in range(len(newimg[0])):
        for j in range(len(newimg)):
            auxbool = auxiliar == newimg[i][j]
            res = matimg[auxbool]
            saida[i][j] = np.mean(res)
            
    saida = np.uint8(saida)
    return saida

#calcula slice
def calculaslice(matimg,redmen):
    saida1 = matimg[::redmen,::redmen]
    return saida1


#show imagem
def showimagemmatplot(img,saida):
    plt.subplot(121),plt.imshow(img),plt.title('entrada')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cv2.cvtColor(saida, cv2.COLOR_BGR2RGB)),plt.title('saida')
    plt.xticks([]), plt.yticks([])
    plt.show()



def showimagemcv(img,saida):
    cv2.imshow('entrada',img)
    cv2.imshow('saida', saida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


##MAIN
matimg, img = carregarimagem()
altura = len(matimg)
largura = len(matimg[0])
redmen = int(input('Digite a taxa de redução (potência de 2): '))
redalt = altura/redmen
redlarg = largura/redmen


b = redlarg*redalt
newimg = np.arange(b)
newimg = newimg.reshape(int(redlarg),int(redalt))
saida = np.arange(b)
saida = newimg.reshape(int(redlarg),int(redalt))
auxiliar = np.repeat((np.repeat(newimg,redmen,axis=0)),redmen,axis=1)

#Box filter
inicio = time.time()
saida = calculamatriz(newimg, auxiliar, matimg, saida)
fim = time.time()
print(fim - inicio)
saidaaux = np.repeat(np.repeat(saida, redmen, 0), redmen, 1)

showimagemcv(img,saidaaux)
#showimagemmatplot(img,saida)

#Fatiamento
inicio = time.time()
saida1 = calculaslice(matimg,redmen)
fim = time.time()
print(fim - inicio)
saida1aux = np.repeat(np.repeat(saida1, redmen, 0), redmen, 1)

showimagemcv(img,saida1aux)
#showimagemmatplot(img,saida1)




        















