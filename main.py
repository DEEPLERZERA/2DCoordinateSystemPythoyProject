#PARTE A

#Importando biblioteca math
import math 

#Recebendo coordenadas da origem do plano cartesiano
origem_x = int(input("Digite a coordenada X da origem abscissa: "))
origem_y = int(input("Digite a coordenada Y da origem ordenada: "))

#Recebendo quantidade de pontos que serão lidos
total_pontos = int(input("Digite a quantidade de pontos que serão lidos: "))

#Variáveis de registro
menor_distancia = float('inf')
ponto_menor_distancia = None
maior_distancia = 0
ponto_maior_distancia = None

primeiro_quadrante = 0
segundo_quadrante = 0
terceiro_quadrante = 0
quarto_quadrante = 0
sobre_eixo_ordenadas = 0
sobre_eixo_abscissas = 0
origem = 0

#Variável de controle
contador = 0

#Loop while para coletar pontos do usuário
while contador < total_pontos:
    #Recebendo coordenadas X e Y do ponto
    x = int(input("Digite a coordenada X do ponto {}: ".format(contador + 1)))
    y = int(input("Digite a coordenada Y do ponto {}: ".format(contador + 1)))

    #Condições para determinar em qual quadrante o ponto está
    if x > origem_x and y > origem_y:
        quadrante = "no 1o quadrante."
        primeiro_quadrante += 1
    elif x < origem_x and y > origem_y:
        quadrante = "no 2o quadrante."
        segundo_quadrante += 1
    elif x < origem_x and y < origem_y:
        quadrante = "no 3o quadrante"
        terceiro_quadrante += 1
    elif x > origem_x and y < origem_y:
        quadrante = "no 4o quadrante"
        quarto_quadrante += 1
    elif x == origem_x and y != origem_y:
        quadrante = "sobre o eixo de coordenadas."
        sobre_eixo_abscissas += 1
    elif x != origem_x and y == origem_y:
        quadrante = "sobre o eixo de coordenadas."
        sobre_eixo_ordenadas += 1
    else:
        origem += 1
        quadrante = "no ponto origem"
    #Imprimindo resultado na tela    
    print("Ponto ({},{}) está {}".format(x, y, quadrante))

    #Calculando distância do ponto à origem (Distância Euclidiana)
    distancia = math.sqrt((x - origem_x) ** 2 + (y - origem_y) ** 2)

    #Atualizando menor e maior distância
    if distancia < menor_distancia:
        menor_distancia = distancia
        ponto_menor_distancia = (x, y)
    if distancia > maior_distancia:
        maior_distancia = distancia
        ponto_maior_distancia = (x, y)

    contador += 1

#Imprimindo resultado na tela
print("Ponto ({},{}) eh o mais próximo, distância={:.2f}.".format(ponto_menor_distancia[0], ponto_menor_distancia[1], menor_distancia))
print("Ponto ({},{}) eh o mais distante, distância={:.2f}.".format(ponto_maior_distancia[0], ponto_maior_distancia[1], maior_distancia))

print("\nQuantidade de pontos em cada quadrante:")
print("Primeiro quadrante:", primeiro_quadrante)
print("Segundo quadrante:", segundo_quadrante)
print("Terceiro quadrante:", terceiro_quadrante)
print("Quarto quadrante:", quarto_quadrante)
print("Sobre o eixo das ordenadas:", sobre_eixo_ordenadas)
print("Sobre o eixo das abscissas:", sobre_eixo_abscissas)
print("Na origem:", origem)


#PARTE B

#Recebendo pontos X e Y do plano cartesiano do usuário
x = int(input("Digite a coordenada X do ponto de origem A do robô:")) 
y = int(input("Digite a coordenada Y do ponto de origem A do robô:"))

#Coletando tempo que o robô irá caminhar
tempo = int(input("Digite por quanto tempo o robô irá caminhar:"))

#Variáveis de controle, visando controlar loop while e processo de direcionamento do robô
contador = 0
controle = 0

#Loop while para garantir o tempo exato de caminhada do robô
while contador < tempo:
  #Condicionais que garantem em qual direção o robô deve ir
  if controle == 0: 
    y = y + 1
    controle = 1
  elif controle == 1:
    x = x + 1
    controle = 2
  else:
    x = x + 1
    controle = 0
  contador = contador + 1

#Imprimindo resultado na tela
print("Ao final da caminhada o robô estará no ponto ({},{}) do plano cartesiano.".format(x, y))

