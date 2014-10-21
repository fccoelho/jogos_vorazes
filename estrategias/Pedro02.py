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
    Jogador 02, estratégia de intervalos. 
    Na verdade eu queria utilizar mais escolhas randomicas baseadas em probabilidade, (como gaussiana, por exemplo)
    como não soube implementar, dividi em trechos utilizano a seguinte estratégia:
    1- Não quero caçar com os extremos, nem com reputação muito baixa, pois perderei comida. Nem com reputação muito alta pois destes eu devo tirar proveito.
    2- Com a reputação mediana, vou sempre caçar, pois acredito o jogo convirja para isso.
    3- Nos outros intervalos, coloquei em função de m. Se m for baixo, vou arriscar caçar. Se m for alta voi arriscar descansar.
    4- Onde nenhuma das premissas se enquandram, deixei aleatório, pois acredito que não deve ter interferencia.
    
    """    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        from random import choice
        escolhas = []
        for x in reputacoes_dos_jogadores:
            if x < 0.2 or x > 0.8:
                escolhas.append('d')
            elif x > 0.5 and x <0.6:
                escolhas.append('c')
            else:
                if m < (len(reputacoes_dos_jogadores)*(len(reputacoes_dos_jogadores)-1))*0.30:
                    escolhas.append('c')
                elif m > (len(reputacoes_dos_jogadores)*(len(reputacoes_dos_jogadores)-1))*0.70:
                    escolhas.append('d')
                else:
                    escolhas.append(random.choice(['c','d']))
        return escolhas
    
