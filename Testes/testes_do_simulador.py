import unittest
import os
os.chdir('..')
import simulador
from estrategias.jogadores import Jogador
from io import StringIO

simulador.R =  StringIO()

class TesteSimulador(unittest.TestCase):
    def setUp(self):
        self.torneio = simulador.Torneio()


    def testa_instanciacao_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        for i in self.torneio.jogadores.values():
            self.assertIsInstance(i, Jogador)

    def testa_comida_inicial(self):
        self.torneio.inicializa_jogadores()
        for J in self.torneio.jogadores.keys():
            self.assertEqual(self.torneio.historico[J]["comida"][0], 300*(self.torneio.p - 1))

    @unittest.skip
    def testa_escolhas_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        for nome, j in self.torneio.jogadores.iteritems():
            self.assertEqual(len(j.escolha_de_cacada(1, 100, 32, 65, range(len(self.torneio.jogadores)-1))), len(self.torneio.jogadores)-1)#, msg="Bug na Estrategia: {}".format(nome))

    def testa_nome_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        self.assertIn('FlavioCoelho', self.torneio.jogadores)

    def testa_propriedade_p(self):
        self.assertEqual(self.torneio.p, 0)
        self.torneio.inicializa_jogadores()
        assert self.torneio.p > 0

    def testa_1_rodada(self):
        self.torneio.inicializa_jogadores()
        self.torneio.vai(1)

    def testa_10_rodadas(self):
        self.torneio.inicializa_jogadores()
        self.torneio.vai(10)

    def testa_inicializacao_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        for dados in self.torneio.historico.values():
            self.assertEqual(dados["reputacao"][-1], 0)
            self.assertEqual(dados["comida"][-1], 300*(self.torneio.p -1))



