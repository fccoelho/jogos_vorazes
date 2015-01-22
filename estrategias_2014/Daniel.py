from .jogadores import Jogador
lista_de_reputacoes=[]

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        lista_de_reputacoes.append(reputacoes_dos_jogadores)
        if rodada==1:
            escolhas=[]
            num_jogadores = len(reputacoes_dos_jogadores)
            i=0
            while i<num_jogadores:
                if i%2 == 0:
                    escolhido = 'c'
                else:
                    escolhido = 'd'
                escolhas.append(escolhido)
                i=i+1
            return escolhas
        else:
            escolhas = []
            if reputacao_atual<0.3:
                    escolhas = ['c' for x in reputacoes_dos_jogadores]
                    return escolhas
            elif len(lista_de_reputacoes[rodada-2]) == len(reputacoes_dos_jogadores):
                variacao=[]
                for y in range(len(reputacoes_dos_jogadores)):
                    variacao_y = reputacoes_dos_jogadores[y] - lista_de_reputacoes[rodada-2][y]
                    variacao.append(variacao_y) 
                for n in range(len(reputacoes_dos_jogadores)): 
                    x=reputacoes_dos_jogadores[n]
                    if variacao[n]==0: 
                        escolhido = 'd'
                    elif variacao[n]<0:
                        escolhido = 'd'
                    elif variacao[n]>0 and x<0.5: 
                        escolhido = 'c'
                    elif variacao[n]>0 and 0.5<=x<=0.85:
                        escolhido = 'd'
                    elif variacao[n]>0 and x>0.85:
                        escolhido = 'c'
                    else:
                        escolhido = ['d' for x in reputacoes_dos_jogadores]
                    escolhas.append(escolhido)
                return escolhas
            else:
                escolhas=[]
                for x in reputacoes_dos_jogadores:
                    if x<=0.4 and x>0.2:
                        escolhido = 'c'
                        escolhas.append(escolhido)
                    elif x<=0.2:
                        escolhido = 'd'
                        escolhas.append(escolhido)
                    elif x>0.4 and x<=0.9:
                        escolhido = 'd'
                        escolhas.append(escolhido)
                    else:
                        escolhido = 'c'
                        escolhas.append(escolhido)
                return escolhas

    def resultado_da_cacada(self, comida_ganha):
        pass 

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        pass                     
                    
