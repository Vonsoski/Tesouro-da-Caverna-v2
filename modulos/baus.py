"""
INSERIR INFOS SOBRE ESSA CLASS
"""
import time
import random

class bau:
#Criar baú
   def __init__(self):
      self.bau = {
         "pocao_Mana":10,"pocao_Vida":15,"pocaoManaMax":100,"pocaoVidaMax":100,"tesouro":1
         }
      self.eventos_caverna = {
         "Morcego":15,"Sapo venenoso ":30,"Nada":0,"Susto":10,"bau":1
         }
      

#Eventos na caverna ao andar
   def eventoAleatorio(self):

      evento = random.randint(0,4)

      for i, (chave, valor) in enumerate(self.eventos_caverna.items()):

         if valor == 1:
            self.evento = True
            self.dano = False
            print("Você achou um baú")
            break

         elif i == evento:
            self.evento = chave
            self.dano = valor
            print(f"Evento na caverna:{chave}")
            break
      return self.evento, self.dano
   
#Procura tesouros
   def procurarTesouro(self):
      for i in range(0,4):
         time.sleep(0.5)
         print("Procurando tesouro" + "." * i)
      self.evento, self.dano = self.eventoAleatorio()
      return self.evento, self.dano
   

      
#Manipulação do bau
   def abrirBau(self):
      item = random.randint(0,4)
      for i, (chave, valor) in enumerate(self.bau.items()):
         if i == item:
            if chave == "tesouro":
               tesouro = True
            else:
               tesouro = False
            break
      return tesouro, item, valor
   

   def removerItem(self, item):
      self.bau.pop(item)