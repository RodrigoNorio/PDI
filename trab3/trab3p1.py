import numpy as np
import cv2



def carregarimagem():
    imagem = input('Digite o nome da imagem com sua entensão: ')
    img = cv2.imread(imagem,0)
    matimg = np.array(img)
    
    return matimg, img

def showimagemcv(img,imgblur,mascara,saida,naonormalizado):
    cv2.imshow('original',img)
    cv2.imshow('imagem borrada', imgblur)
    cv2.imshow('mascara', mascara)
    cv2.imshow('saida nao normalizada', naonormalizado)
    cv2.imshow('saida', saida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



matimg, img = carregarimagem()


#parte 1

imgblur = cv2.GaussianBlur(img, (3,3), 1)

mascara = np.int32(matimg) - np.int32(imgblur)

mascara1 = 2*np.int32(mascara)

saida = (np.int32(img) + mascara1)

naonormalizado = saida
naonormalizado = np.uint8(naonormalizado)


normalizamenor = saida < 0
saida[normalizamenor] = 0
normalizamaior = saida > 255
saida[normalizamaior] = 255

saida = np.uint8(saida)

img = np.uint8(img)
mascara1 = np.uint8(mascara1)
imgblur = np.uint8(imgblur)

showimagemcv(img,imgblur,mascara1,saida,naonormalizado)