# coding: utf8
from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada == 1:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        else:
            escolhas = []
            for x in reputacoes_dos_jogadores:
                if x <= 0.25:
                    if random.uniform(0,1)<0.25:
                        escolhas.append('d')
                    else:
                        escolhas.append('c')
                elif 0.25 < x <= 0.5:
                    if random.uniform(0,1)<0.5:
                        escolhas.append('d')
                    else:
                        escolhas.append('c')
                elif 0.5 < x <= 0.75:
                    if random.uniform(0,1)<0.5:
                        escolhas.append('d')
                    else:
                        escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas


