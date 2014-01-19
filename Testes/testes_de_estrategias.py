import unittest


from estrategias.jogadores import Jogador, JogadorViraLata

class Teste_Jogador(unittest.TestCase):
    def setUp(self):
        self.Jogador = JogadorViraLata()
    def tearDown(self):
        pass
    def testa_escolha_de_cacadas_retorna_lista(self):
        J = self.Jogador
        escolhas = J.escolha_de_cacada(1,100, 32, 65, range(123))
        self.assertEqual(len(escolhas), 123)

    def testa_estrutura_da_classe(self):
        self.assertIn("resultado_da_cacada", dir(self.Jogador))
        self.assertIn("fim_da_rodada", dir(self.Jogador))
    def testa_letras_da_escolha(self):
        escolhas = self.Jogador.escolha_de_cacada(1,100, 32, 65, range(123))
        assert all([x in ["c", "d"] for x in escolhas])

