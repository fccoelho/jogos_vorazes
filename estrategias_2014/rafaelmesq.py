from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada <= 750 or len(reputacoes_dos_jogadores) < 4:
            escolhas = ['d' for i in reputacoes_dos_jogadores]
        else:
            escolhas = []
            for i in reputacoes_dos_jogadores:
                if 0.65 < i < 0.9:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas
