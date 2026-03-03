import random

def andar(mana, passos):

    if mana != 0:
        andando = random.randint(0,6)
        mana = mana - andando
        passos = passos + andando

        print(f"Andando {andando} casas")
 
    else:
       print("Você não possui mana suficiente")

    return mana, passos