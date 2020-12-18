import numpy as np
import cv2



def carregarimagem():
    imagem = input('Digite o nome da imagem com sua extensão: ')
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

kernel = np.ones([3, 3], dtype=np.uint8)
padding = np.zeros([len(matimg), len(matimg[0])], dtype='f')

altura = int(len(padding)/2)
largura = int(len(padding[0])/2)



shape = np.maximum(kernel.shape, padding.shape)
h = np.zeros((shape), dtype=np.float)
h[:padding.shape[0], :padding.shape[1]] = padding


h[altura][largura] = 4/16
h[altura-1][largura-1] = 1/16
h[altura+1][largura+1] = 1/16
h[altura+1][largura-1] = 1/16
h[altura-1][largura+1] = 1/16
h[altura][largura-1] = 2/16
h[altura][largura+1] = 2/16
h[altura+1][largura] = 2/16
h[altura-1][largura] = 2/16





#parte 2

fourier = np.fft.fft2(matimg)

h = np.absolute(np.fft.fft2(h))

fourier = fourier * h

fourier = np.absolute(np.fft.ifft2(fourier))




mascara = np.int32(matimg) - np.int32(fourier)

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
fourier = np.uint8(fourier)

showimagemcv(img,fourier,mascara1,saida,naonormalizado)







