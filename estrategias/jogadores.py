# coding: utf8
"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e
"""

class Jogador:
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
        escolhas = ['c' for x in reputacoes_dos_jogadores] # modifique com a sua próprio estratégia
        return escolhas

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
        pass


class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['d' for x in reputacoes_dos_jogadores]
        return escolhas

class JogadorMaisEspertinho(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = ['c' if x>0.8 else 'd' for x in reputacoes_dos_jogadores]
        return escolhas