import time
import random

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
           tesouro = False
        break
    return chave, valor, tesouro