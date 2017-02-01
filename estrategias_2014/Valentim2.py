# -*- coding: cp1252 -*-
from estrategias.jogadores import Jogador
class MeuJogador(Jogador):
    def __init__(self):
        self.comida = 0
        self.reputacao = 0
        self.numero_de_cacadores = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        raciocinio=0
        count = 0
        if raciocinio==0:
            Media_Reputacoes = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
            escolhas = []
            for rep in reputacoes_dos_jogadores:
                if rep >= Media_Reputacoes:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
            for i in range(25000):
                count=count+1
            if count == 25000:
                raciocinio = 0
            return escolhas
        else:
            count = 0

            for i in range(25000):
                escolhas = ['c' for x in reputacoes_dos_jogadores]
                count=count+1
            if count == 25000:
                raciocinio = 1
            return escolhas
