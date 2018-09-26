from estrategias.jogadores import Jogador
import random
from numpy import random

class MeuJogador(Jogador):

    def __init__(self):
        self.rodadabol = False


    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        try:
            if self.rodadabol:
                if len(reputacoes_dos_jogadores)>0.750*float(self.numjog): #estrategia 1: primeiro quarto da partida (acumular pontos)
                    if m>len(reputacoes_dos_jogadores): #se o m vale a pena
                        A=[]
                        for item in reputacoes_dos_jogadores:
                            a=random.random()
                            if a<0.7+item**2:
                                A.append('c')
                            else:
                                A.append('d')
                        return A
                    else: #se o m nao vale a pena
                        A=[]
                        for item in reputacoes_dos_jogadores:
                            a=random.random()
                            if a<0.35+item**2:
                                A.append('c')
                            else:
                                A.append('d')
                        return A
                elif len(reputacoes_dos_jogadores)>0.333*float(self.numjog): #estrategia 2: estrategia dominante (manter reputação)
                    if self.j==0 and reputacao_atual<0.6:
                        self.j=5
                    if self.j!=0: #procedimento de recuperação
                        if m>len(reputacoes_dos_jogadores):
                            A=[]
                            self.j-=1
                            for item in reputacoes_dos_jogadores:
                                a=random.random()
                                if a<0.7+item**2:
                                    A.append('c')
                                else:
                                    A.append('d')
                            return A
                        else:
                            A=[]
                            self.j-=1
                            for item in reputacoes_dos_jogadores:
                                a=random.random()
                                if a<0.4+item**2:
                                    A.append('c')
                                else:
                                    A.append('d')
                            return A
                    else: #procedimento babaca
                        if m>len(reputacoes_dos_jogadores):
                            A=[]
                            for item in reputacoes_dos_jogadores:
                                a=random.random()
                                if a<0.1+item**2:
                                    A.append('c')
                                else:
                                    A.append('d')
                            return A
                        else:
                            A=[]
                            for item in reputacoes_dos_jogadores:
                                a=random.random()
                                if a<item**2:
                                    A.append('c')
                                else:
                                    A.append('d')
                            return A
                else: #estrategia 3: chuta o balde
                    a=numpy.random.normal(0.5,0.1666, 1)
                    a=a[0]
                    A=[]
                    for item in reputacoes_dos_jogadores:
                        if a<0.333+item**3:
                            A.append('c')
                        else:
                            A.append('d')
                    return A
            else:
                self.numjog = len(reputacoes_dos_jogadores)+1
                self.rodadabol = True
                self.j = 0
                A=[]
                for item in reputacoes_dos_jogadores:
                    A.append('c')
                return A
        except:
            A=[]
            for item in reputacoes_dos_jogadores:
                A.append('c')
            return A
