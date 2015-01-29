#!/usr/bin/env python3
# coding: utf8
__author__ = 'fccoelho'

import pkgutil
import importlib
from collections import defaultdict
import random
import copy
import os
import pandas as pd
import matplotlib.pyplot as P

jogadores = [name for _,name,_ in pkgutil.iter_modules(['estrategias'])]
jogadores.remove('jogadores')



class Torneio(object):
    def __init__(self):
        self.historico = defaultdict(lambda: {"comida": [], "reputacao": [], "cacou": 0, "descansou": 0})
        self.jogadores = None # dicionario com as instancias dos jogadores;
        self.cemiterio = {}
        self.rodada = 0
        self.bugados = {}
        self.M = [] #série de m



    @property
    def p(self):
        if self.jogadores is None:
            return 0
        return len(self.jogadores)

    def inicializa_jogadores(self):
        self.jogadores = {x : importlib.import_module("estrategias.{}".format(x)).MeuJogador() for x in jogadores}
        for nome, jogador in self.jogadores.items():
            self.historico[nome]["comida"].append(300*(self.p-1))
            self.historico[nome]["reputacao"].append(0)
        self.inicializa_saida()

    def inicializa_saida(self):
        mode = "w"
        cabecalho = ','.join(self.historico.keys()) + '\n'
        with open("comida.csv", mode) as f:
            f.write(cabecalho)
        with open("reputacao.csv", mode) as f:
            f.write(cabecalho)
        with open("recompensa.csv", mode) as f:
            f.write("recompensa")

    def roda_rodada(self):
        """
        Coleta as escolhas de cada jogador

        """
        self.rodada += 1
        if self.rodada%5000 == 0:
            print("Iniciando Rodada {}".format(self.rodada))
        jogadores_randomizados = list(self.jogadores.keys())
        random.shuffle(jogadores_randomizados)
        m = random.randrange(0, self.p*(self.p-1))
        self.M.append(m)
        escolhas = {}
        
        for nome in jogadores_randomizados:
            jogador = self.jogadores[nome]
            adversarios = copy.copy(jogadores_randomizados)
            adversarios.remove(nome)
            reputacoes = tuple([self.historico[nome_adv]["reputacao"][-1] for nome_adv in adversarios])
            try:
                escolhas[nome] = (jogador.escolha_de_cacada(self.rodada, self.historico[nome]["comida"][-1],
                                      self.historico[nome]["reputacao"][-1],
                                      m, reputacoes), tuple(adversarios))
            except Exception as e:
                escolhas[nome] = (['c' for i in reputacoes],adversarios)
                self.bugados[nome] = (self.rodada, e)
                
            self.historico[nome]["cacou"] += sum(e == 'c' for e in escolhas[nome][0])
            self.historico[nome]["descansou"] += sum(e == 'd' for e in escolhas[nome][0])
        saldo = self.calcula_resultado_cacadas(escolhas)
        recompensa, cacadas = self.calcula_recompensa(escolhas)
        
        R.write(str(recompensa) + "\n")
        for nome, jogador in self.jogadores.items():
            jogador.resultado_da_cacada(saldo)
            jogador.fim_da_rodada(recompensa, self.M[-1], cacadas)
        self.atualiza_reputacao()
        self.atualiza_comida(saldo, recompensa)
        for nome in self.bugados.keys():
            if nome in self.cemiterio:
                continue
            self.enterra(nome)
            print("{} Morreu bugado, na rodada {}".format(nome, self.rodada))
                

    def calcula_resultado_cacadas(self, escolhas):
        """
        Calcula comida obtida em todas as caçadas e retorna o saldo por jogador

        :rtype : defaultdict
        :param escolhas:
        :return:
        """
        saldo = defaultdict(lambda: [])  # saldo de todos as cacadas por jogador
        cooperadores = []
        for nome_jogador, cacadas in escolhas.items():
            for decisao, adversario in zip(*cacadas):
                gasto = -2 if decisao == 'd' else -6
                ganho_pessoal = 6 if decisao == 'c' else 0
                #print len(escolhas[adversario][0]), tuple(escolhas[adversario][1]).index(nome_jogador)
                adversario_cooperou = escolhas[adversario][0][tuple(escolhas[adversario][1]).index(nome_jogador)] == 'c'
                ganho_adversario = 6 if adversario_cooperou else 0
                saldo[nome_jogador].append(gasto + (ganho_pessoal+ganho_adversario)/2.)
            self.jogadores[nome_jogador].resultado_da_cacada(saldo[nome_jogador])
        return saldo

    def atualiza_comida(self, saldo, recompensa):
        for nome, comida in saldo.items():
            if nome in self.cemiterio:
                print("alimentando um Morto!!")
                continue
            comida_atual = self.historico[nome]["comida"][-1]
            self.historico[nome]["comida"].append(comida_atual + sum(comida) + recompensa)
            if self.historico[nome]["comida"][-1] <= 0:
                self.enterra(nome, self.historico[nome]["comida"][-1])

    def atualiza_reputacao(self):
        for nome in self.jogadores.keys():
            self.historico[nome]["reputacao"].append(self.historico[nome]["cacou"] / (float(self.historico[nome]["cacou"] + self.historico[nome]["descansou"])))

    def enterra(self, nome, comida=None):
        del self.jogadores[nome]
        print("Restam {} jogadores".format(len(self.jogadores)))
        self.cemiterio[nome] = self.rodada
        print("{} Morreu na rodada {} com {} pontos".format(nome, self.rodada, comida))

    def calcula_recompensa(self, escolhas):
        cacadas = 0
        for e in escolhas.items():
            cacadas += sum([i == 'c' for i in e[1][0]]) # numero de vezes que este jogador cacou
        recompensa = 2*(self.p - 1) if cacadas > self.M[-1] else 0
        return recompensa, cacadas

    def checa_fim(self):
        if len(self.jogadores) == 1:
            return True
        return False

    def vai(self, max_rodadas=10000):
        f = open("comida.csv", "a")
        g = open("reputacao.csv", "a")
        while True:
            self.roda_rodada()
            self.salva_series(f,g)
            if self.checa_fim():
                self.anuncia_vencedor()
                break
            elif self.rodada > max_rodadas:
                for nome in self.historico.keys():
                    print (nome, self.historico[nome]["comida"][-1], self.historico[nome]["reputacao"][-1])
                self.anuncia_vencedor()
                break
        f.close()
        g.close()

    def anuncia_vencedor(self):
        ranking1 = [(nome, data["comida"][-1]) for nome,data in self.historico.items() if (data["comida"][-1]>0 and nome not in self.cemiterio and nome not in self.bugados)]
        ranking = sorted(ranking1, key=lambda x: x[1], reverse=True)
        print ("Sobreviventes:")
        print (ranking)
        if len(ranking1) >=3:
            print ("==> Em Terceiro lugar...: {} com {}".format(ranking[2][0], ranking[2][1]))
            print ("==> Em Segundo lugar...: {} com {}".format(ranking[1][0], ranking[1][1]))
            print ("==> Em Primeiro lugar...: {} com {}".format(ranking[0][0], ranking[0][1]))
        else:
            print ("==> Em Primeiro lugar e único sobrevivente:... {} com {}".format(ranking[0][0], ranking[0][1]))
        print ("Falecidos:")
        print(self.cemiterio)
        print ("Banidos (bugados):")
        print(self.bugados)

    def salva_series(self, f, g):
        
        comida_t = []
        reputacao_t = []
        for j in self.historico.values():
            comida_t.append(str(j["comida"][-1]))
            reputacao_t.append(str(j["reputacao"][-1]))
        f.write(",".join(comida_t) + "\n")
        g.write(",".join(reputacao_t) + "\n")
        
        
    def plota_series(self):
        comida = pd.read_csv('comida.csv')
        reputacao = pd.read_csv('reputacao.csv')
        comida.plot()
        P.figure()
        reputacao.plot()

if __name__ == "__main__":
    T = Torneio()
    #T.inicializa_jogadores()
    #R = open("recompensa.csv", "a")
    #T.vai(200000)
    #R.close()
    T.plota_series()
    P.show()





