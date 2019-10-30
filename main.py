from players import *
from hash import *

player = Player('teste', 'o')#intancia do objeto do jogador
velha = Hash() #instancia do objeto velha

while True:
    velha.draw()

    opcao = int(input("Sua vez"))

    a, b = velha.translate_position(opcao) #passando retorno para variaveis

    if velha.verify_option(a, b) == False:
        print("Opcao invalida")
    else: 
        velha.mark_position(a, b)





