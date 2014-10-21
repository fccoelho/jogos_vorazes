from .jogadores import Jogador

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        media_reputacao = sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)
        reputacao_mais_alta = max(reputacoes_dos_jogadores)
        reputacao_mais_baixa = min(reputacoes_dos_jogadores)
        
        if rodada == 1 or rodada == 2:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            
        elif len(reputacoes_dos_jogadores) <=3:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
            
        else:
            if reputacao_atual >= media_reputacao:
                
                escolhas = ['c' if (x > ((media_reputacao - reputacao_mais_baixa)/2. + reputacao_mais_baixa) or x > (reputacao_mais_alta - (reputacao_mais_alta - media_reputacao)/2.)) else 'd' for x in reputacoes_dos_jogadores]
            
            else:
                escolhas = ['d' if ((x == reputacao_mais_alta) or (x == reputacao_mais_baixa)) else 'c' for x in 	reputacoes_dos_jogadores]

        return escolhas
