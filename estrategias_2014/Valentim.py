# -*- coding: cp1252 -*-
from estrategias.jogadores import Jogador


class MeuJogador(Jogador):
    def __init__(self):
        self.comida = 0
        self.reputacao = 0
        self.numero_de_cacadores = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        """
        Método principal que executa a cada rodada.
        você precisa criar uma lista de escolhas onde 'c' significa escolher caçar e 'd' representa descansar
        as decisãoes podem usar todas as informações disponíveis, por exemplo, as reputações dos outros jogadores.
        rodada: inteiro que é a rodada em que você está
        comida_atual: inteiro com a comida que você tem
        reputacao_atual: float representando sua reputação atual
        m: inteiro que é um limiarde cooperação/caçada desta rodada.
        reputacoes_dos_jogadores: lista de floats com as reputações dos outros jogadores
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
        else:  # Adicionado por flávio por ser um erro
            return ['c' for x in reputacoes_dos_jogadores]

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
        self.numero_de_cacadores = numero_de_cacadores
