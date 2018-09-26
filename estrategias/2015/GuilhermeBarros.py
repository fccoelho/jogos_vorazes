from .jogadores import Jogador
import random

class MeuJogador(Jogador):

    def __init__(self):
        Jogador.__init__(self)
        self.comida_anterior = 0
        self.mu = 0.7
        self.sigma = 0.1
        self.pesos = [0.5,0.5]
        self.variacao = 0.1
        self.anterior = 'd'


    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        peso_descanso = 1
        peso_cacada = 1

        num_jogadores = len(reputacoes_dos_jogadores)

        escolhas = []


        if comida_atual<self.comida_anterior:

            #if (self.anterior == 'd'):
            #    peso_descanso = 0.95
            #if (self.anterior == 'c'):
            #    peso_cacada = 0.95

            self.mu = self.mu + random.uniform(-self.variacao*peso_cacada,self.variacao*peso_descanso)

            if self.mu < 0.3:
                self.mu = 0.3

            self.sigma = abs(self.sigma + random.uniform(-0.1*self.variacao, 0.1*self.variacao))
            self.pesos[0] = self.pesos[0] + random.uniform(-self.variacao, self.variacao)


            if self.pesos[0]>1:
                self.pesos[0] = 1
            if self.pesos[0] < 0.3:
                self.pesos[0] = 0.3

            self.pesos[1] = 1- self.pesos[0]

        for reputacao in (reputacoes_dos_jogadores):

            mu_atual = (self.pesos[0]*self.mu) + (self.pesos[1]*reputacao)
            threshold = random.gauss(mu_atual, self.sigma)
            decisao = random.uniform(0,1)

            if reputacao <= 0.1:
                escolhas.append('d')
            elif decisao>threshold:
                escolhas.append('c')
            else:
                escolhas.append('d')

        self.comida_anterior = comida_atual

        #if rodada % 1000 == 0:
        #    print("mu: ", self.mu)
        #    print("sigma: ", self.sigma)
        #    print("peso_mu: ", self.pesos[0])
        #    print("variacao: ", self.variacao)

        descanso = escolhas.count('d')
        cacada = escolhas.count('c')
        if cacada>=descanso:
            self.anterior = 'c'
        else:
            self.anterior = 'd'

        return escolhas
