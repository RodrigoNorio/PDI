# PDI trab 1


BOX FILTER

O objetivo deste trabalho é implementar e testar o filtro conhecido como box filter, utilizado para a realização de subamostragem com redução de aliasing.

Você pode considerar, se necessário, para fins de simplificação, que o tamanho das imagens e a taxa de redução sejam potências de 2. 

Este trabalho NÃO É a aplicação de uma função pronta. Você deve desenvolver sua própria solução, mas pode utilizar funções auxiliares do OpenCV e do scikit-image em sua implementação. 

O método deve ser implementado em Python 3.x, usando-se a biblioteca Numpy. Use a biblioteca OpenCV ou scikit-image para carregar/salvar/mostrar as imagens. Priorize a utilização de fatiamento (slicing) no lugar de estruturas de repetição.

Deverá constar no relatório um texto introdutório explicando a teoria considerada no trabalho, o código-fonte, as imagens resultantes de um ou mais experimentos de comparação e a bibliografia consultada.

Para fins de comparação visual, realize um experimento comparativo entre o box filter e o downsampling simples feito por fatiamento.

O arquivo a ser entregue deve ser compactado e conter o relatório, o código-fonte e as imagens de teste usadas para o relatório.

Este trabalho pode ser realizado em dupla.

# PDI trab 2

CUBO RGB

O objetivo deste trabalho é implementar a geração de imagens coloridas que sejam "fatias" do cubo que representa o espaço de cor RGB. Você deve numerar os lados deste cubo para referência e escolher uma "fatia" a partir da "fatia inicial" que é uma das faces, a escolher, do cubo.

O programa deve receber como parâmetros:

a face escolhida à partir da qual será selecionada a "fatia" (a face deve ser indexada/rotulada por um valor de 1 a 6)
um valor i (de 0 a 255) para indexar a i-ésima fatia.
O programa deve gerar e mostrar a i-ésima "fatia" em relação à face escolhida como referência.

Considere que no cubo RGB em questão as cores tem profundidade de 24 bits. 

Este trabalho NÃO É a aplicação de uma função pronta. Você deve desenvolver sua própria solução. O método deve ser implementado em Python 3.x, usando-se a biblioteca Numpy. Use a biblioteca OpenCV ou scikit-image para carregar/salvar/mostrar as imagens.

Não há necessidade de utilização de estruturas de repetição explícitas. Priorize a utilização de fatiamento (slicing) no lugar de estruturas de repetição.

Deverá constar no relatório um texto introdutório explicando a teoria considerada no trabalho, o código-fonte, as imagens resultantes de um ou mais experimentos de comparação e a bibliografia consultada.

O arquivo a ser entregue deve ser compactado e conter o relatório, o código-fonte e as imagens de teste usadas para o relatório.

Este trabalho pode ser realizado em dupla.


# PDI trab 3
FILTRAGEM HIGH-BOOST

O objetivo destes trabalhos é implementar e testar o método de filtragem conhecido como high-boost, utilizado para o aumento de nitidez de imagens digitais. O método está descrito nas Seções 3.6.3 e 4.9.5 do livro do Gonzales&Woods, 3a. edição, nas páginas 107 e 188, respectivamente. Seu trabalho deve receber imagens como nitidez reduzida e devolver outra imagem com nitidez aguçada, conforme descrito pelo método. A página do livro do Gonzalez oferece o download das imagens utilizadas no livro

http://www.imageprocessingplace.com/root_files_V3/image_databases.htm 

e você pode aplicar seu trabalho, por exemplo, na Figura 3.40 como ilustração.

No Trabalho Três, a filtragem passa-baixa utilizada deve ser realizada no domínio espacial (convolução, Seção 3.6.3).

No Trabalho Quatro, a filtragem passa-baixa utilizada deve ser realizada no domínio da frequência (Fourier, Seção 4.9.5).

Em resumo, você deve realizar a filtragem high-boost utilizando duas abordagens, uma para cada trabalho. 

Você deve explicar as suas abordagens e os métodos que você escolheu como suporte para a sua solução. Você deve desenvolver suas próprias soluções, mas pode utilizar funções auxiliares do OpenCV e do scikit-image em suas implementações. Os métodos devem ser implementados em Python 3.x, usando-se a biblioteca Numpy. Use a biblioteca OpenCV ou scikit-image para carregar/salvar/mostrar as imagens. Priorize a utilização de fatiamento (slicing) no lugar de estruturas de repetição.

Deverá constar no relatório um texto introdutório explicando as teorias consideradas no trabalho, os códigos-fonte, as imagens resultantes de um ou mais experimentos de comparação e a bibliografia consultada.

Os dois trabalhos, 3 e 4, devem ser entregues juntos, no mesmo relatório. No relatório, acrescente uma Seção para cada uma das duas abordagens, destacando a teoria, os códigos-fonte e os resultados. Você pode até acrescentar uma Seção onde você compara o resultado das duas abordagens.

O arquivo a ser entregue deve ser compactado e conter o relatório, os códigos-fonte e as imagens de teste usadas para o relatório.

Estes trabalhos podem ser realizados em dupla, mas pela mesma dupla.
