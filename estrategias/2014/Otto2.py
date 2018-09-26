from estrategias.jogadores import Jogador

# class MeuJogador(Jogador):
#
#         def basic_linear_regression(self, x,y):
#             length = len(x)
#             sum_x = sum(x)
#             sum_y = sum(y)
#             sum_x_squared = sum(map(lambda a: a * a,x))
#             sum_of_products = sum([x[i] * y[i] for i in range(length) ])
#             a = (sum_of_products - (sum_x * sum_y)/length)/(sum_x_squared - ((sum_x ** 2)/length))
#             b = (sum_y - a * sum_x)/length
#             return a,b
#
#         def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
#             dic = {"aleat": m,"rodada":rodada}
#             media_reputacao = sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)
#             if reputacao_atual > 0.3:
#                 escolhas = ['d' for x in reputacoes_dos_jogadores]
#             else:
#                 escolhas = []
#             while reputacao_atual < 0.3:
#                 dic["aleat"] = {dic["aleat"],m}
#                 dic["rodada"] += 1
#                 beta = self.basic_linear_regression(dic["aleat"],dic["rodada"])
#                 M_analise = beta[0] + beta[1]*m
#                 if media_reputacao < M_analise:
#                     escolhas.append('c')
#                 else:
#                     escolhas.append('d')
#             return escolhas

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        escolhas = ['c' for x in reputacoes_dos_jogadores]

        return escolhas
