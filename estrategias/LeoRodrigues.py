# -*- coding: utf8 -*-
from .jogadores import Jogador
        
class MeuJogador(Jogador):
    def percent(self,data,percentil):
        data = sorted(data)
        n = len(data)
        if n == 0:
            pass
            #print ("Lista vazia")
        else:
            return int(round(percentil*n+1))
        
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        """
        Método principal que executa a cada rodada.
        você precisa criar uma lista de escolhas onde 'c' significa escolher caçar e 'd' representa descansar
        as decisãoes podem usar todas as informações disponíveis, por exemplo, as reputações dos outros jogadores.
        rodada: inteiro que é a rodada em que você está
        comida_atual: inteiro com a comida que você tem
        reputacao_atual: float representando sua reputação atual
        m: inteiro que é um limiarde cooperação/caçada desta rodada.
        reputacoes_dos_jogadores: lista de floats com as reputações dos outros jogadores
        """
        reput_oder = sorted(reputacoes_dos_jogadores)
        if comida_atual > 50:
            if rodada < 10:
                #print(reput_oder)
                escolhas = ['c' if max(reput_oder) > reput_oder[self.percent(reput_oder,0.25)-1] and min(reput_oder) < reput_oder[self.percent(reput_oder,0.75)-1]  else 'd' for i in reput_oder]
                return escolhas
            else:
                  
                if float(sum(reput_oder))/float(len(reput_oder)) >= 0.55:
                    escolhas = ['c' if max(reput_oder) > reput_oder[self.percent(reput_oder,0.20)-1] else 'd' for i in reputacoes_dos_jogadores]
                else:
                    escolhas = ['c' if max(reput_oder) > reput_oder[self.percent(reput_oder,0.40)-1] and min(reput_oder) < reput_oder[self.percent(reput_oder,0.60)-1]  else 'd' for i in reput_oder]
                return escolhas
        
        else:
            escolhas = ['d' for i in reput_oder]
            return escolhas
