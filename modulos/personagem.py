import time
import random
import sys

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.mana = 50
        self.passos = 0
        self.myinventario = {}

        print(f"Personagem criado com sucesso.\nNome: {self.nome}\nVida: {self.vida}\nMana: {self.mana}")

#ANDAR
    def andar(self):
        if self.mana > 30:
            andando = random.randint(0,6)
            self.mana = self.mana - andando
            self.passos = self.passos + andando
            print(f"Andando {andando} casas")
        else:
            print("Você não possui mana suficiente")
        return self.passos

#INVENTARIO
    def inventario(self, item, valor):
        self.myinventario[item] = valor
        print(self.myinventario)
        print(f"Itens no inventario: {item}")
        for chave, valor in self.myinventario.items():
            print(f"Item: {chave}")

#ACESSAR E RECUPERAR STATUS

    def statuslife(self, dano):
        self.vida -= dano
        print(f"Você recebeu {dano}, sua vida atual: {self.vida}")

    def estadoPlayer(self):
        print(f"Fim do turno, este é o seu status atual:\nVida:{self.vida}\nMana: {self.mana}")
        if self.vida <= 0:
            print("Você está morto")
            sys.exit()
        elif self.mana <= 0:
            print("Mana insuficiaente")
            self.descansar = input("Deseja descansar para recuperar mana? ")
        else:
            return self.mana, self.vida

    def descansar(self):
        """
        """
        self.vida -=10
        self.mana +=10


    
