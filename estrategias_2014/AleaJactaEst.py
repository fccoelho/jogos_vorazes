#-*- coding:utf-8 -*-
u"""
Created on 21/01/14
by fccoelho
license: GPL V3 or Later
"""

__docformat__ = 'restructuredtext en'


from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):
    """
    Caca com probabilidade `p_caca`
    """
    def __init__(self, p_caca=0.8):
        assert p_caca >= 0 and p_caca <=1
        self.p_caca = p_caca
        self._name = "AleaJactaEst"

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['c' if random.random() < self.p_caca else 'd' for x in reputacoes_dos_jogadores]
        return escolhas
