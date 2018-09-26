from .jogadores import Jogador


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if comida_atual <= 10:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
            return escolhas
        else:
            escolhas = ['d' if x > 0.8333 else 'c' if x > 0.1667 else 'd' for x in reputacoes_dos_jogadores]
            return escolhas