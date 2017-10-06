# coding: utf8

class Jogador:
    def __init__(self):
        
        self.comida = 0
        self.reputacao = 0



    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
      
        escolhas = ['c' for x in reputacoes_dos_jogadores] # modifique com a sua próprio estratégia
        return escolhas

    def resultado_da_cacada(self, comida_ganha):
        """
        este método é chamado depois que todas as cacadas da rodada forem terminadas.
        comida_ganha é uma lista com inteiros representando a comida ganha em cada uma das caçadas feitas na rodada.
        Estes números podem ser negativos.

        Sua comida total é a soma destes números e a comida atual.

        adicione código para atualizar suas variáveis internas
        """
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """
        Adicione código para alterar suas variaveis com base na cooperação que ocorreu na última rodada
        recompensa: Comida total que você recebeu de jogadores que cooperaram na ultima rodada.
        numero_de_cacadores: inteiro que é o numero de caçadores que cooperou com você na última rodada.
        """
        pass


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada <2:        
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        else:
            if reputacao_atual>=0.4 and reputacao_atual<=0.6:
                escolhas = ['d' if x> 0.7 or x <0.3 else 'c' for x in reputacoes_dos_jogadores]
            
            elif reputacao_atual<0.4:
                    escolhas = ['c' for x in reputacoes_dos_jogadores]
            else:
                    escolhas = ['d' for x in reputacoes_dos_jogadores]
        return escolhas

