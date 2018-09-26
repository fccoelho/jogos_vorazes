# coding: utf8

from estrategias.jogadores import Jogador

"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve 
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e 
"""

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
        self.historico = {}
        self.historico2 = {}
    
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
        
        self.rodada = rodada
        
        if rodada == 1:
            media_reputacoes = 0
            quantidade_hunters_inicial = len(reputacoes_dos_jogadores)
            quantidade_hunters = quantidade_hunters_inicial
            m_max = quantidade_hunters*(quantidade_hunters - 1)
        else:
            rodada_anterior = rodada - 1
            media_reputacoes = sum(self.historico[rodada_anterior][3])/len(self.historico[rodada_anterior][3])
            quantidade_hunters = len(self.historico[rodada_anterior][3])
            m_max = quantidade_hunters*(quantidade_hunters - 1)
        
        self.historico[rodada] = (comida_atual, reputacao_atual, m, reputacoes_dos_jogadores, media_reputacoes, m_max)
        
        if rodada > 21:
            rodadas_atras = rodada - 20
            media_reput_atras = self.historico[rodadas_atras][4]
            comida_atras = self.historico[rodadas_atras][0]
        else:
            media_reput_atras = self.historico[rodada][4]
            comida_atras = self.historico[rodada][0]
                
        #cada_hunter1 = 0
        #for cada_hunter in reputacoes_dos_jogadores:
        #    if cada_hunter >= cada_hunter1
        
        if reputacao_atual <= 0.45:
            if media_reputacoes < 0.25:
                if m <= (m_max/4):
                    Mini, Maxi = 0.10, 0.80
                else:
                    Mini, Maxi = 2*media_reputacoes, 0.80
                    
            if media_reputacoes > 0.65:
                if comida_atual < comida_atras:
                    Mini, Maxi = 0.6, 1.00
                else:
                    Mini, Maxi = 0.35, 1.00
                
            else:
                Mini, Maxi = 0.25, 0.80
        
        elif reputacao_atual >= 0.70:
            if media_reputacoes < 0.25:
                if m <= (m_max/4):
                    Mini, Maxi = 0.10, 1.00
                else:
                    Mini, Maxi = 0.60, 1.00

            elif media_reputacoes < media_reput_atras:
                Mini, Maxi = 0.75, 1.00
                
            else:
                Mini, Maxi = 0.60, 1.00
        
        else:
            if comida_atual < comida_atras:
                if media_reputacoes < media_reput_atras:
                    Mini, Maxi = 0.40, 0.50
                else:
                    Mini, Maxi = 0.75, 0.30
            else:
                Mini, Maxi = 0.40, 0.50
        
        
        if rodada == 1:
            escolhas = ['d' if x%3 == 0 else 'c' for x in range(0,len(reputacoes_dos_jogadores))]
            
        else:
            escolhas = ['c' if x <= Maxi and x >= Mini else 'd' for x in reputacoes_dos_jogadores]
        
        #escolhas = ['c' for x in reputacoes_dos_jogadores] # modifique com a sua próprio estratégia
        return escolhas

    def resultado_da_cacada(self, comida_ganha):
        """
        este método é chamado depois que todas as cacadas da rodada forem terminadas.
        comida_ganha é uma lista com inteiros representando a comida ganha em cada uma das caçadas feitas na rodada. 
        Estes números podem ser negativos.
        
        Sua comida total é a soma destes números e a comida atual.
        
        adicione código para atualizar suas variáveis internas 
        """
        self.comida_ganha = comida_ganha

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """
        Adicione código para alterar suas variaveis com base na cooperação que ocorreu na última rodada 
        recompensa: Comida total que você recebeu de jogadores que cooperaram na ultima rodada.
        numero_de_cacadores: inteiro que é o numero de caçadores que cooperou com você na última rodada.
        """
        self.historico2[self.rodada] = (self.comida_ganha, recompensa, m, numero_de_cacadores)
        pass 
