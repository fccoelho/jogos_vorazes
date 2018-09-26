from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):

    def __init__(self):

        self.interacao = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        caçadas_rodada = round(m ** (1 / 2))
        n_jogadores = len(reputacoes_dos_jogadores)
        #self.interacao = self.interacao + len(reputacoes_dos_jogadores)
        #c = reputacao * interacao

        if rodada <= 1000:
            escolhas = list(np.random.choice(['c', 'd'], size= n_jogadores, p=(0.47, 1 - 0.47)))
        else:
            if comida_atual <= 200:
                escolhas = ['d' for x in reputacoes_dos_jogadores]
            else:
                if n_jogadores <= 4:
                    escolhas = ['d' for x in reputacoes_dos_jogadores]
                else:
                    if reputacao_atual < 0.47:
                        escolhas = []

                        for x in reputacoes_dos_jogadores:
                            if x >= 0.70:
                                escolhas.append(list(np.random.choice(['c', 'd'], size=1, p=(x, 1-x)))[0])
                            else:
                                escolhas.append(list(np.random.choice(['c', 'd'], size=1, p=(x*0.20, 1 - x*0.20)))[0])
                    else:
                        escolhas = []

                        for x in reputacoes_dos_jogadores:
                            if x >= 0.5:
                                escolhas.append(list(np.random.choice(['c', 'd'], size=1, p=(1 - x, x)))[0])
                            else:
                                escolhas.append(list(np.random.choice(['c', 'd'], size=1, p=(x, 1 - x)))[0])
        return escolhas