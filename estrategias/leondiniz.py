# coding: utf8
"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve 
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e 
"""
import math
from .jogadores import Jogador
def somar(*valores):
    soma = 0
    for v in valores:
        soma += v
    return soma
 
 
def media(*valores):
    soma = somar(*valores)
    qtd_elementos = len(valores)
    media = soma / float(qtd_elementos)
    return media
 
 
def variancia(*valores):
    _media = media(*valores)
    soma = 0
    _variancia = 0
 
    for valor in valores:
                   
        soma += math.pow( (valor - _media), 2)
    _variancia = soma / float( len(valores) )
    return _variancia
 
 
def desvio_padrao(*valores):
    return math.sqrt( variancia(*valores) )

        
class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if reputacao_atual<0.3:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        elif rodada==2 or rodada==3:
            escolhas =  ['d' for x in reputacoes_dos_jogadores]
        else:
            escolhas = ['c' if x>0.3 and x<0.9 else 'd' for x in reputacoes_dos_jogadores]
        return escolhas
   