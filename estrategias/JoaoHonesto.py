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
    Caca com probabilidade igual à do outro
    """
    def __init__(self):
        self._name = "JoaoHonesto"

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['c' if random.random() < x else 'd' for x in reputacoes_dos_jogadores]
        return escolhas
