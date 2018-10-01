# -*- coding: cp1252 -*-
from estrategias.jogadores import Jogador


class MeuJogador(Jogador):
    def __init__(self):
        self.comida = 0
        self.reputacao = 0
        self.numero_de_cacadores = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        """
        M�todo principal que executa a cada rodada.
        voc� precisa criar uma lista de escolhas onde 'c' significa escolher ca�ar e 'd' representa descansar
        as decis�oes podem usar todas as informa��es dispon�veis, por exemplo, as reputa��es dos outros jogadores.
        rodada: inteiro que � a rodada em que voc� est�
        comida_atual: inteiro com a comida que voc� tem
        reputacao_atual: float representando sua reputa��o atual
        m: inteiro que � um limiarde coopera��o/ca�ada desta rodada.
        reputacoes_dos_jogadores: lista de floats com as reputa��es dos outros jogadores
        """
        if rodada < 100:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            return escolhas
        elif reputacao_atual > 0.8 and comida_atual > 10:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
            return escolhas
        elif (comida_atual < len(reputacoes_dos_jogadores) * 2) and (
            self.numero_de_cacadores <= len(reputacoes_dos_jogadores) / 2):
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            return escolhas
        elif comida_atual < 10:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            return escolhas
        else:  # Adicionado por fl�vio por ser um erro
            return ['c' for x in reputacoes_dos_jogadores]

    def resultado_da_cacada(self, comida_ganha):
        """
        este m�todo � chamado depois que todas as cacadas da rodada forem terminadas.
        comida_ganha � uma lista com inteiros representando a comida ganha em cada uma das ca�adas feitas na rodada. 
        Estes n�meros podem ser negativos.
        
        Sua comida total � a soma destes n�meros e a comida atual.
        
        adicione c�digo para atualizar suas vari�veis internas 
        """
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """
        Adicione c�digo para alterar suas variaveis com base na coopera��o que ocorreu na �ltima rodada 
        recompensa: Comida total que voc� recebeu de jogadores que cooperaram na ultima rodada.
        numero_de_cacadores: inteiro que � o numero de ca�adores que cooperou com voc� na �ltima rodada.
        """
        self.numero_de_cacadores = numero_de_cacadores
