from estrategias.jogadores import Jogador
import numpy as np


class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        total_jogadores = len(reputacoes_dos_jogadores)
        if rodada==1:
            escolhas = list(np.random.choice(['c', 'd'], size=total_jogadores, p=(0.45, 0.55)))
        else:
            if total_jogadores>6:
                escolhas = []
                for r in reputacoes_dos_jogadores:
                    if isinstance(r, np.ndarray):
                        r = r[0]
                    esc = np.random.choice(['d', 'c'], 1, p=[1 - r, r])[0]
                    escolhas.append(esc)
            else:
                escolhas = ['d' for x in reputacoes_dos_jogadores]
        return escolhas