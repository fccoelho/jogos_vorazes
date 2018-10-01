from .jogadores import Jogador
import random

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        if comida_atual > 60 * ((len(reputacoes_dos_jogadores) - 1) *(-2)) and reputacao_atual > media:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
                    
        elif comida_atual > 60 * ((len(reputacoes_dos_jogadores) - 1) *(-2)) and reputacao_atual < media:
            for rep in reputacoes_dos_jogadores:
                if (rep >= media) and random.uniform(0,1) > (rodada / 1000):
                    escolhas.append('c')
                else:
                    escolhas.append('d')
                        
        elif comida_atual < 60 * ((len(reputacoes_dos_jogadores) - 1) *(-2)) and reputacao_atual > media:
            for rep in reputacoes_dos_jogadores:
                if (rep >= media):
                    escolhas.append('d')
                else:
                    escolhas.append('c')
                        
        elif comida_atual < 60 * ((len(reputacoes_dos_jogadores) - 1) *(-2)) and reputacao_atual < media:
            for rep in reputacoes_dos_jogadores:
                if (rep >= media):
                    escolhas.append('d')
                else:
                    escolhas.append('c')
        else:
            escolhas = ['c' for i in reputacoes_dos_jogadores]

        return escolhas
