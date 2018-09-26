from estrategias.jogadores import Jogador


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        mediaReputacoes = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        escolhas = []
        for rep in reputacoes_dos_jogadores:
            if rep >= mediaReputacoes:
                escolhas.append('d')
            else:
                escolhas.append('c')

        return escolhas
