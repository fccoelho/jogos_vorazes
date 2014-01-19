import unittest
import os
os.chdir('..')
import simulador
from estrategias.jogadores import Jogador


class TesteSimulador(unittest.TestCase):
    def setUp(self):
        pass

    def testa_instanciacao_dos_jogadores(self):
        torneio = simulador.Torneio()
        torneio.inicializa_jogadores()
        for i in torneio.jogadores.itervalues():
            self.assertIsInstance(i, Jogador)

    def testa_nome_dos_jogadores(self):
        torneio = simulador.Torneio()
        torneio.inicializa_jogadores()
        self.assertIn('FlavioCoelho', torneio.jogadores)

    def testa_propriedade_p(self):
        torneio = simulador.Torneio()
        self.assertEqual(torneio.p, 0)
        torneio.inicializa_jogadores()
        assert torneio.p > 0

    def testa_inicializacao_dos_jogadores(self):
        torneio = simulador.Torneio()
        torneio.inicializa_jogadores()
        for dados in torneio.historico.itervalues():
            self.assertEqual(dados["reputacao"][-1], 0)
            self.assertEqual(dados["comida"][-1], 300*(torneio.p -1))

    @unittest.skip
    def testa_calcula_resultado_de_cacadas(self):
        torneio = simulador.Torneio()
        torneio.inicializa_jogadores()
        escolhas = {'joao': (['c', 'd', 'c'], ['maria', 'luisa', 'jose']), 'maria': (['d', 'c', 'd'], ['joao', 'luisa', 'jose']),
                    'luisa': (['c', 'd', 'd'], ['joao', 'maria', 'jose']), 'jose': (['c', 'c', 'c'], ['joao', 'maria', 'luisa'])}
        saldo = torneio.calcula_resultado_cacadas(escolhas)
        self.assertIsInstance(saldo, dict)
        self.assertIsInstance(saldo['maria'], list)

