from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):

    def __init__(self):
        Jogador.__init__(self)


    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):


        escolhas = []
        media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        for rep in reputacoes_dos_jogadores:
            if (rep >= media) and random.uniform(0,1) > (rodada / 20000):
                escolhas.append('c')
            else:
                escolhas.append('d')
        return escolhas
