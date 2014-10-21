#-*- coding:utf-8 -*-
u"""
Created on 21/01/14
by fccoelho
license: GPL V3 or Later
"""

__docformat__ = 'restructuredtext en'

from .jogadores import Jogador
import random

class MeuJogador(Jogador):
    """
    Caca com quem tem reputação dentro de certo limite
    """
    def __init__(self, linf=0.3, lsup=0.6):
        self.linf = linf
        self.lsup = lsup
        self._name = "MediaAna"

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        rep_media = sum(reputacoes_dos_jogadores) / float(len(reputacoes_dos_jogadores))
        escolhas = ['c' if random.random() < rep_media else 'd' for x in reputacoes_dos_jogadores]
        return escolhas
