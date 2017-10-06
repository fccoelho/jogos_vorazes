# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador
class MeuJogador(Jogador):
	def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
		if rodada <= 2:
			escolhas = ['c' for x in reputacoes_dos_jogadores]
		else:
			escolhas = []
			ordenado = list(range(len(reputacoes_dos_jogadores)))
			for x in range(len(reputacoes_dos_jogadores)):
				ordenado[x] = reputacoes_dos_jogadores[x]
			ordenado.sort()

			if (len(ordenado)%2 == 0):
				mediana = (ordenado[len(ordenado)//2 - 1] + ordenado[len(ordenado)//2])/2.
			else:
				mediana = ordenado[(len(ordenado) - 1)//2]

			for x in reputacoes_dos_jogadores:
				if x <= 0.2 or x >= 0.8:
					escolhas.append('d')
				else:
					if x >= mediana:
						escolhas.append('c')
					else:
						escolhas.append('d')
		return escolhas
