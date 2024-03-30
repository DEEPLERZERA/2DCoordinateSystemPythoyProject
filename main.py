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
print("Ao final da caminhada o robô estará no ponto", "(",x,",",y,") do plano cartesiano.")

