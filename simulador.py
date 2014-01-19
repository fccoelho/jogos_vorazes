# coding: utf8
__author__ = 'fccoelho'



import pkgutil
import importlib
from collections import defaultdict
import random
import copy


jogadores = [name for _,name,_ in pkgutil.iter_modules(['estrategias'])]
jogadores.remove('jogadores')

class Torneio(object):
    def __init__(self):
        self.historico = defaultdict(lambda: {"comida": [], "reputacao": [], "cacou": 0, "descansou": 0})
        self.jogadores = None # dicionario com as instancias dos jogadores;
        self.cemiterio = []
        self.rodada = 0
        self.M = [] #série de m

    @property
    def p(self):
        if self.jogadores is None:
            return 0
        return len(self.jogadores)

    def inicializa_jogadores(self):
        self.jogadores = {x : importlib.import_module("estrategias.{}".format(x)).MeuJogador() for x in jogadores}
        for nome, jogador in self.jogadores.iteritems():
            self.historico[nome]["comida"].append(300*(self.p-1))
            self.historico[nome]["reputacao"].append(0)

    def roda_rodada(self):
        """
        Coleta as escolhas de cada jogador

        """
        self.rodada += 1
        print("Iniciando Rodada {}".format(self.rodada))
        jogadores_randomizados = self.jogadores.keys()
        random.shuffle(jogadores_randomizados)
        m = random.randrange(0, self.p-1)
        self.M.append(m)
        reputacoes = [self.historico[nome]["reputacao"][-1] for nome in jogadores_randomizados]
        escolhas = {}
        for nome, jogador in self.jogadores.iteritems():
            adversarios = copy.copy(jogadores_randomizados)
            adversarios.remove(nome)
            escolhas[nome] = (jogador.escolha_de_cacada(self.rodada, self.historico[nome]["comida"][-1],
                                      self.historico[nome]["reputacao"][-1],
                                      m, reputacoes), adversarios)
            self.historico[nome]["cacou"] += sum(e == 'c' for e in escolhas[nome][0])
            self.historico[nome]["descansou"] += sum(e == 'd' for e in escolhas[nome][0])
        saldo = self.calcula_resultado_cacadas(escolhas)
        recompensa, cacadas = self.calcula_recompensa(escolhas)
        print recompensa
        for nome, jogador in self.jogadores.iteritems():
            jogador.resultado_da_cacada(saldo)
            jogador.fim_da_rodada(recompensa, self.M[-1], cacadas)
        self.atualiza_reputacao()
        self.atualiza_comida(saldo, recompensa)



    def calcula_resultado_cacadas(self, escolhas):
        """
        Calcula comida obtida em todas as caçadas e retorna o saldo por jogador

        :rtype : defaultdict
        :param escolhas:
        :return:
        """
        saldo = defaultdict(lambda: [])  # saldo de todos as cacadas por jogador
        cooperadores = []
        for nome_jogador, cacadas in escolhas.iteritems():
            for decisao, adversario in zip(*cacadas):
                gasto = 2 if decisao == 'd' else 6
                ganho_pessoal = 6 if decisao == 'c' else 0
                adversario_cooperou = escolhas[adversario][0][tuple(escolhas[adversario][1]).index(nome_jogador)] == 'c'
                ganho_adversario = 6 if adversario_cooperou else 0
                saldo[nome_jogador].append(gasto + (ganho_pessoal+ganho_adversario)/2.)
            self.jogadores[nome_jogador].resultado_da_cacada(saldo[nome_jogador])
        print saldo
        return saldo

    def atualiza_comida(self, saldo, recompensa):
        for nome, comida in saldo.iteritems():
            comida_atual = self.historico[nome]["comida"][-1]
            self.historico[nome]["comida"].append(comida_atual + sum(comida) + recompensa)
            if self.historico[nome]["comida"][-1] <= 0:
                self.enterra(nome)

    def atualiza_reputacao(self):
        for nome in self.jogadores.iterkeys():
            self.historico[nome]["reputacao"].append(self.historico[nome]["cacou"] / (float(self.historico[nome]["cacou"] + self.historico[nome]["descansou"])))

    def enterra(self, nome):
        self.jogadores.pop(nome)
        self.cemiterio.append(nome)

    def calcula_recompensa(self, escolhas):
        cacadas = 0
        for e in escolhas.iteritems():
            cacadas += sum([i == 'c' for i in e[1][0]]) # numero de vezes que este jogador cacou
        recompensa = 2*(self.p - 1) if cacadas > self.M[-1] else 0
        return recompensa, cacadas

    def checa_fim(self):
        if len(self.jogadores) <= 1:
            return True
        return False

    def vai(self):
        while True:
            self.roda_rodada()
            if self.checa_fim():
                break
                print self.jogadores.keys()
            elif self.rodada > 10000:
                for nome in self.historico.keys():
                    print nome, self.historico[nome]["comida"][-1], self.historico[nome]["comida"][-1]
                break

if __name__ == "__main__":
    T = Torneio()
    T.inicializa_jogadores()
    T.vai()





