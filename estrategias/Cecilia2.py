# -*- coding: utf8 -*-
from .jogadores import Jogador
class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        ultimaescolha = 1
        reputacoes_copia = reputacoes_dos_jogadores
        reputacoes_ordenadas = list(reputacoes_copia)
        reputacoes_ordenadas.sort()
        p_30 = reputacoes_ordenadas[int((len(reputacoes_ordenadas)*0.30)-1)] #numero que define quem eu nao caco (baixa reputacao)
        p_80 = reputacoes_ordenadas[int((len(reputacoes_ordenadas)*0.80)-1)] #numero que define quem eu nao caco (alta reputacao)
        
        if rodada == 1:
            for i in range(0, len(reputacoes_dos_jogadores)):
                if ultimaescolha > 0:
                    escolhas.append('c')
                else: 
                    escolhas.append('d')
                ultimaescolha = ultimaescolha*(-1)
        else:
            for i in range(0, len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i] < p_30 or reputacoes_dos_jogadores[i] >= p_80:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
        return escolhas
