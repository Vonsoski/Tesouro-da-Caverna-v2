import time
import random
import sys

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mana = 50
        self.passos = 0
        print(f"Personagem criado com sucesso.\nNome: {self.nome}\nVida: {self.vida}\nMana: {self.mana}")

    def andar(self):
        if self.mana > 30:
            andando = random.randint(0,6)
            self.mana = self.mana - andando
            self.passos = self.passos + andando
            print(f"Andando {andando} casas")
    
        else:
            print("Você não possui mana suficiente")
        return self.passos

    def descansar(self):
        """
        """
        self.vida -=10
        self.mana +=10

    def estadoPlayer(self):
        print(f"Fim do turno, este é o seu status atual:\nVida:{self.vida}\nMana: {self.mana}")
        if self.vida <= 0:
            print("Você está morto")
            sys.exit()
        else:
            return self.mana, self.vida
    
    def inventario(self, itens):
        inventario = {}