"""
O projeto consiste em um jogo em texto no qual um jogador explora uma caverna em busca de um tesouro escondido.
Durante a exploração, eventos inesperados podem ocorrer, afetando o estado do jogador.
O jogo continua até que o tesouro seja encontrado ou o jogador morra.

Nova atualização: Ao encontrar um bau, os itens serão inseridos no inventario, sendo possivel utiliza-los, mas ao utilizar um item, o jogador não irá prosseguir no mapa.
"""

import logging
import mecanicas as mec

logging.basicConfig(level=logging.ERROR, format=" %(asctimes)s - %(levelname)s - %(message)s - linha %(lineno)d")

vida = 100
mana = 100
tamanho_caverna = 150
passos = 0
cont = 0


bau = {
   "pocao_Mana":10,"pocao_Vida":15,"pocaoManaMax":100,"pocaoVidaMax":100,"tesouro":1
   }

eventos_caverna = {
   "Morcego":15,"Sapo venenoso ":30,"Nada":0,"Susto":10,"bau":1
   }

inventario = {}

while True:
    start = input(
       "Bem vindo a busca ao tesouro, deseja iniciar? S/N "
       )
    
    if start == 'S' or 's':
        break
    else:
        print("Selecione a opção válida")

try:
    while True:

       if passos == 0:
        mana, passos = mec.andar(mana, passos)

       if passos != 0:
        continuar_jogada = input("Deseja rolar o dado? Ou Usar items no inventário?: INICIO(s)/INVENTARIO(i): ")

        if continuar_jogada == "s" or "S":
            mana, passos = mec.andar(mana, passos)
        else:

            for i, chave, valor in inventario,items():
             print(f"Escolher item{chave} selecione o número{i}")

        vida, procura_tesouro = mec.procurarTesouro(vida, eventos_caverna)

        if procura_tesouro == True:

            items, item, tesouro = mec.abrirBau(bau)

            checa_item = inventario.get(items)

            if checa_item == None:
                inventario[items] = items
            else:
                valor = valor + 1
                inventario.update({items: valor})

        else:
         mec.checkLife(vida)

        checar_status = input("Deseja checar status do seu personagem: S/N ")
        if checar_status == 'S' or 's':
            print(
            f"Vida: {vida}\nMana: {mana}\nInventário: {inventario}"
            )
        

except:
    logging.ERROR("Ocorreu um erro")