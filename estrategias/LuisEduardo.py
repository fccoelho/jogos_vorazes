from .jogadores import Jogador
import math


class MeuJogador(Jogador):
    def calcula_media(self, lista):
        self.media = (sum(lista)) / len(lista)
        return self.media

    def calcula_desvio(self, lista):
        lista_desvios = []
        for x in lista:
            lista_desvios.append(math.fabs(x - self.media))
        desvio = (sum(lista_desvios)) / (len(lista_desvios))
        return desvio

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        media = self.calcula_media(reputacoes_dos_jogadores)
        desvio = self.calcula_desvio(reputacoes_dos_jogadores)
        escolhas = ['c'] * len(reputacoes_dos_jogadores)

        if rodada < 31:

            for x in reputacoes_dos_jogadores:
                if (reputacao_atual < media):
                    if x < (media - 1.5 * desvio) or x > (media + 3 * desvio):
                        escolhas[reputacoes_dos_jogadores.index(x)] = 'd'
                else:
                    if x < (media - desvio) or x > (media + 2 * desvio):
                        escolhas[reputacoes_dos_jogadores.index(x)] = 'd'

        elif (rodada > 30 and rodada < 71):

            if reputacao_atual > media:
                if rodada % 7 == 0:
                    escolhas = ['d' for x in reputacoes_dos_jogadores]
                else:
                    for x in reputacoes_dos_jogadores:
                        if x < (media - desvio) or x > (media + 2 * desvio):
                            escolhas[reputacoes_dos_jogadores.index(x)] = 'd'
                        else:
                            if x < (media - 1.5 * desvio) or x > (media + 3 * desvio):
                                escolhas[reputacoes_dos_jogadores.index(x)] = 'd'

        else:

            if reputacao_atual > media:
                if rodada % 2 == 0:
                    escolhas = ['d' for x in reputacoes_dos_jogadores]
                else:
                    for x in reputacoes_dos_jogadores:
                        if x < (media - desvio) or x > (media + 2 * desvio):
                            escolhas[reputacoes_dos_jogadores.index(x)] = 'd'

                        else:
                            if x < (media - 1.5 * desvio) or x > (media + 3 * desvio):
                                escolhas[reputacoes_dos_jogadores.index(x)] = 'd'

        return escolhas