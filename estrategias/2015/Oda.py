# coding: utf8
from .jogadores import Jogador
import numpy.random as npr
import os

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        if rodada == 1:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        else:
            npr.seed(seed=int.from_bytes(os.urandom(4), byteorder='big'))
            escolhas = []
            for rep in reputacoes_dos_jogadores:
                esc = npr.choice(['d', 'c'], 1, p=[1 - rep, rep])
                escolhas.append(esc)

        return escolhas
