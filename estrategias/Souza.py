# coding: utf8
"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e
"""
from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    def __init__(self):
        """
        Este metodo é executado quando o seu jogador for instanciado no início do jogo.

        Você pode adicionar outras variáveis a seu critério.

        Você não precisa definir comida ou reputação pois o Controlador do jogo vai manter o registro
        destas variáveis para cada jogador informando-as aos jogadores a cada rodada, através do método
        escolha_de_cacada.


        """
        self.comida = 0
        self.reputacao = 0
        self.food = [0]
        self.ders = []
        self.rodada = 0
        self.falling = False
        self.actions = []



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
        
        escolhas = [self.think(rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores, x) for x in reputacoes_dos_jogadores] # modifique com a sua próprio estratégia
        return escolhas
    
    def think(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores, x):
        a = self.think2(rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores, x)
        if a:
            return 'c'
        else:
            return 'd'
    
    def think2(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores, x):
        #self.rodada = rodada
        #if rodada == 1
        #self.record_food(comida_atual)
        if rodada == 1:
            return True
        if rodada <= 400:
            if rodada % 20 <= 10:
                return True
            else:
                return self.str1(x)
        if len(reputacoes_dos_jogadores) >= 2 or True:
            return self.str1(x)
        else:
            return False
        
    def str1(self, x):
        if x == 0:
            return False
        elif x >= 8.5:
            p = np.random.rand()
            return p >= 0.5
        else:
            p = np.random.rand()
            if p >= 0.85:
                p = 0.85
                return np.random.rand() < p
        
    #def check_a(self):
    #    return sum(self.actions[-10:]) > 6
    
    def resultado_da_cacada(self, comida_ganha):
        """
        este método é chamado depois que todas as cacadas da rodada forem terminadas.
        comida_ganha é uma lista com inteiros representando a comida ganha em cada uma das caçadas feitas na rodada.
        Estes números podem ser negativos.

        Sua comida total é a soma destes números e a comida atual.

        adicione código para atualizar suas variáveis internas
        """
        
    
    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """
        Adicione código para alterar suas variaveis com base na cooperação que ocorreu na última rodada
        recompensa: Comida total que você recebeu de jogadores que cooperaram na ultima rodada.
        numero_de_cacadores: inteiro que é o numero de caçadores que cooperou com você na última rodada.
        """
        pass
