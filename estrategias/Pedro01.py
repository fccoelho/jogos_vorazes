# coding: utf8
"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve 
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e 
"""

import random
from .jogadores import Jogador

class MeuJogador(Jogador):
    """
    Jogador 01, estratégia sorte
    
    """
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        from random import choice
        escolhas = [random.choice(['d','c']) for x in reputacoes_dos_jogadores]
        return escolhas
    
