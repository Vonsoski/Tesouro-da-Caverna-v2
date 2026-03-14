"""
INSERIR INFOS SOBRE ESSA CLASS
"""
import time
import random

class bau:

   def __init__(self):
      self.bau = {
         "pocao_Mana":10,"pocao_Vida":15,"pocaoManaMax":100,"pocaoVidaMax":100,"tesouro":1
         }
      self.eventos_caverna = {
         "Morcego":15,"Sapo venenoso ":30,"Nada":0,"Susto":10,"bau":1
         }

   def procurarTesouro(self):
      for i in range(0,4):
         time.sleep(0.5)
         print("Procurando tesouro" + "." * i)

      self.evento, self.dano = self.eventoAleatorio(self.eventos_caverna)

      return self.evento, self.dano
   

   def eventoAleatorio(self):

      evento = random.randint(0,4)

      for i, (chave, valor) in enumerate(self.eventos_caverna.items()):

         if valor == 1:
            self.evento = True
            self.dano = False
            print("Você achou um baú")
            break

         elif i == evento:
            self.evento = False
            self.dano = valor
            print(f"Evento na caverna: {chave}")
            break

      return self.evento, self.dano