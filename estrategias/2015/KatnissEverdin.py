# -*- coding: utf8 -*-
from .jogadores import Jogador


class MeuJogador(Jogador):
    def __init__(self):
        Jogador.__init__(self)
        self.reputacao_anterior = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada <= 5:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        elif reputacao_atual < 0.3:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
        elif (self.reputacao_anterior - reputacao_atual) > 0.5:
            escolhas = ['d' if x >= 0.8 else 'c' for x in reputacoes_dos_jogadores]
        else:
            escolhas = []
            for x in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[x] <= 0.15 or reputacoes_dos_jogadores[x] >= 0.85:
                    escolhas.append('d')
                else:
                    escolhas.append('c')

        self.reputacao_anterior = reputacao_atual
        return escolhas
