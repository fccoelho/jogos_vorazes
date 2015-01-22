from .jogadores import Jogador


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['c' if x < 0.8 and x > 0.6 else 'd' for x in reputacoes_dos_jogadores]
        return escolhas