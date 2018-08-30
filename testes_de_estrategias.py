import unittest
import pkgutil
import importlib


from estrategias.jogadores import Jogador, JogadorMaisEspertinho


class Teste_Jogador(unittest.TestCase):
    def setUp(self):
        jogadores = [importlib.import_module("estrategias.{}".format(name)).MeuJogador() for _,name,_ in pkgutil.iter_modules(['estrategias'])]
        self.Jogadores = [JogadorMaisEspertinho(), Jogador()] + jogadores

    def tearDown(self):
        pass

    def testa_escolha_de_cacadas_retorna_lista(self):
        for J in self.Jogadores:
            escolhas = J.escolha_de_cacada(1, 100, 32, 65, range(123))
            self.assertEqual(len(escolhas), 123)

    def testa_estrutura_da_classe(self):
        for J in self.Jogadores:
            self.assertIn("resultado_da_cacada", dir(J))
            self.assertIn("fim_da_rodada", dir(J))

    def testa_letras_da_escolha(self):
        for J in self.Jogadores:
            escolhas = J.escolha_de_cacada(1,100, 32, 65, range(123))
            assert all([x in ["c", "d"] for x in escolhas])

