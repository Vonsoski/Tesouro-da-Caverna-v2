import time
import random
import sys


def checkLife(vida):

    if vida == 0:
       print("Você morreu!")
       sys.exit()
    else:
       print(f"Estado atual:\n vida:{vida}")

def estadoPlayer(life, stealth):
   
   global vida
   global mana

   vida = life
   mana = stealth
