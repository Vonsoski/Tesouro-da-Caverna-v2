import time
import random
import sys


def andar(mana, passos):

    if mana != 0:
        andando = random.randint(0,6)
        mana = mana - andando
        passos = passos + andando

        print(f"Andando {andando} casas")
 
    else:
       print("Você não possui mana suficiente")

    return mana, passos


def procurarTesouro(vida_char, eventos_caverna):

    for i in range(0,4):

        time.sleep(0.5)

        print("Procurando tesouro" + "." * i)

    vida, procura_tesouro = eventoAleatorio(vida_char, eventos_caverna)
    return vida, procura_tesouro

def eventoAleatorio(vida_char, eventos_caverna):

  evento = random.randint(0,4)

  for i, (chave, valor) in enumerate(eventos_caverna.items()):

    if valor == 1:
        procura_tesouro = True
        vida = vida_char
        print("Você achou um baú")
        break

    elif i == evento:
        procura_tesouro = False
        vida = vida_char - valor
        print(f"{chave}\nVida: {vida}")
        break

  return vida, procura_tesouro


def abrirBau(bau):
    item = random.randint(0,4)

    for i, (chave, valor) in enumerate(bau.items()):
     
     if i == item:
        if chave == "tesouro":
           tesouro = True
        else:
           items = chave
           tesouro = False
        break
    return items, tesouro

def checkLife(vida):
    if vida == 0:
       print("Você morreu!")
       sys.exit()
    else:
       print(f"Estado atual:\n vida:{vida}")


##Função para andar

##Função para realizar eventos\


##Função para checar o estado de vida e mana do personagem
def estadoPlayer(life, stealth):
   
   global vida
   global mana

   vida = life
   mana = stealth

##Função para checar o estado de vida do personagem

    