from .jogadores import Jogador


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        if rodada == 1:
            escolhas = (len(reputacoes_dos_jogadores)) * ['c']
        else:
            for x in reputacoes_dos_jogadores:
                if x <= 0.5:
                    escolhas.append('d')
                elif 0.5 < x <= 0.75:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas




