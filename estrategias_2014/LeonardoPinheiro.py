from estrategias.jogadores import Jogador


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada <= 2:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            return escolhas
        elif comida_atual <= 300:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
            return escolhas
        elif reputacao_atual < 0.7:
            escolhas = ['c' if x > 0.8 else 'd' for x in reputacoes_dos_jogadores]
            return escolhas
        else:
            escolhas = ['d' if x > 0.9 or x < 0.5 else 'c' for x in reputacoes_dos_jogadores]
            return escolhas

