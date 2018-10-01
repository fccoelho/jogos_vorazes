# -*- coding: utf8 -*-
from .jogadores import Jogador

class MeuJogador(Jogador):
    reputacao_meta = 0.5
    reputacao_minima_aceitavel = 0.3
    reputacao_atual_copia = 0
    historico_minha_reputacao =[0]
    historico_num_cacadores =[]
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        ultimaescolha = 1
        self.reputacao_atual_copia = reputacao_atual
        reputacoes_copia = reputacoes_dos_jogadores
        reputacoes_ordenadas = list(reputacoes_copia)
        reputacoes_ordenadas.sort()
        p_min = reputacoes_ordenadas[int((len(reputacoes_ordenadas)*self.reputacao_minima_aceitavel))] #numero que define quem eu nao caco (baixa reputacao)
        p_max = reputacoes_ordenadas[int((len(reputacoes_ordenadas)*(self.reputacao_minima_aceitavel+self.reputacao_meta)))] #numero que define quem eu nao caco (alta reputacao)
        self.historico_minha_reputacao.append(reputacao_atual)
        if rodada == 1:
            for i in range(0,len(reputacoes_dos_jogadores)):
                if ultimaescolha > 0:
                    escolhas.append('c')
                else: 
                    escolhas.append('d')
                ultimaescolha = ultimaescolha*(-1)
        else:
            for i in range(0,len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i] < p_min or reputacoes_dos_jogadores[i] >= p_max:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
        return escolhas
    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        import random
        self.historico_num_cacadores.append(numero_de_cacadores)
        maximo = 0
        pos = 0
        for i in range(len(self.historico_num_cacadores)):
            if maximo > self.historico_num_cacadores[i]:
                maximo = self.historico_num_cacadores[i]
                pos = i
        #print(pos, len(self.historico_minha_reputacao))
        self.reputacao_meta = self.historico_minha_reputacao[pos] + random.randrange(-100,100)/1000
        self.reputacao_meta = max(0.1, self.reputacao_meta)
        self.reputacao_meta = min(0.9,self.reputacao_meta)
        self.reputacao_minima_aceitavel = 0.7 * (1 - self.reputacao_meta)
