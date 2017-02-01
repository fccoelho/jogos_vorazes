# coding: utf8
from .jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if len(reputacoes_dos_jogadores) > 5:
            escolhas = [np.random.choice(['c', 'd', 'c', 'c', 'd', 'c']) for x in reputacoes_dos_jogadores]
        else:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
        return escolhas
