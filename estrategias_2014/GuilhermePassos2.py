# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador
class MeuJogador(Jogador):
	def __init__(self):
		Jogador.__init__(self)	
		self.reputacoes_anteriores = 0

	def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
		if rodada <= 3:
			escolhas = ['c' for x in reputacoes_dos_jogadores]
		elif reputacao_atual < 0.3:
			escolhas = ['c' for x in reputacoes_dos_jogadores]
		else:
			escolhas = []
			for x in range(len(reputacoes_dos_jogadores)):				
				if reputacoes_dos_jogadores[x] <= 0.15 or reputacoes_dos_jogadores[x] >= 0.85:
					escolhas.append('d')
				else:
					if(self.reputacoes_anteriores[x] < reputacoes_dos_jogadores[x]):
						escolhas.append('d')
					else:
						escolhas.append('c')
#escolhas = ['d' if (self.reputacoes_anteriores[x] < reputacoes_dos_jogadores[x]) else 'c' for x in range(len(reputacoes_dos_jogadores))]
		self.reputacoes_anteriores = reputacoes_dos_jogadores
		return escolhas
