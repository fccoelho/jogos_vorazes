# coding: utf8
"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve 
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e 
"""

import random
from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    """
    Tiro livre 2
    
    """
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        from random import choice
        
        qtd_jogadores = len(reputacoes_dos_jogadores)
        media_reputacoes = sum(reputacoes_dos_jogadores) / qtd_jogadores
        m_estimado = qtd_jogadores * (qtd_jogadores-1) * media_reputacoes
        
        if qtd_jogadores < 4:
            escolhas = [ 'd' for x in reputacoes_dos_jogadores ]
            return escolhas
              
        if m_estimado > m * (1 + qtd_jogadores/10) and reputacao_atual > 0.5:
            escolhas = [random.choice(['d','d','d','d','c']) for x in reputacoes_dos_jogadores]
        else:
            escolhas = [random.choice(['d','c','c']) for x in reputacoes_dos_jogadores]
        return escolhas
    
