#-*- coding:utf-8 -*-
u"""
Created on 21/01/14
by fccoelho
license: GPL V3 or Later
"""

__docformat__ = 'restructuredtext en'
from .jogadores import Jogador

class MeuJogador(Jogador):
    """
    Só caça com que tem a reputação máxima
    """
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        max_rep = max(reputacoes_dos_jogadores)
        escolhas = ['c' if x==max_rep else 'd' for x in reputacoes_dos_jogadores]
        return escolhas
