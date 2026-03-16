"""
O projeto consiste em um jogo em texto no qual um jogador explora uma caverna em busca de um tesouro escondido.
Durante a exploração, eventos inesperados podem ocorrer, afetando o estado do jogador.
O jogo continua até que o tesouro seja encontrado ou o jogador morra.

Nova atualização: Ao encontrar um bau, os itens serão inseridos no inventario, sendo possivel utiliza-los, mas ao utilizar um item, o jogador não irá prosseguir no mapa.
"""

import logging
import modulos as mec

logging.basicConfig(level=logging.ERROR, format=" %(asctimes)s - %(levelname)s - %(message)s - linha %(lineno)d")



#Iniciar game
start = input("INICIAR O GAME: SIM / NAO: ")
start = start.upper()


if start == "SIM":
    nome = input("Digite o nome do seu personagem: ")
    personagem = mec.Personagem(nome)
    bau = mec.bau()
    carverna = mec.caverna
    print(personagem)
    print(f"Regras de mana:\nPara recuparar mana é necessário descansar o turno.\nPara cada turno, você perde 10 de vida para 10 de mana ou obter uma poção de mana.\n")


try:
    while True:
        acao = input("Para andar digite(s), para descansar digite (d): ")
        acao = acao.upper()

        if acao == "S":
            passos = personagem.andar()

        if passos < 1:
            print("Você não avançou")
            continue

        else:
            evento, dano = bau.procurarTesouro()
            if dano > 1:
                print(f"evento: {evento} e dano: {dano}")
                personagem.statuslife(dano)
            elif evento == True:
                tesouro, item, valor = bau.abrirBau()
                if tesouro == True:
                    print("VOCÊ ACHOU O BAÚ DO TESOURO, O JOGO ACABOU, PARABÉNS!!!")
                else:
                    personagem.inventario(item, valor)
                    bau.removerItem(item)
except:
    logging.ERROR("Ocorreu um erro")
