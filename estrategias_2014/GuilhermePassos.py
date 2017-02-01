# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador
class MeuJogador(Jogador):
	def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
		if rodada <= 3:
			escolhas = ['c' for x in reputacoes_dos_jogadores]
		else:
			escolhas = []
			media = 0
			for x in reputacoes_dos_jogadores:
				media = media + x
			media = float(media)/len(reputacoes_dos_jogadores)	

			for x in reputacoes_dos_jogadores:
				if x <= 0.2 or x >= 0.8:
					escolhas.append('d')
				else:
					if x >= media:
						escolhas.append('c')
					else:
						escolhas.append('d')
		return escolhas
