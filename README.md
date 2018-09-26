# Jogos vorazes


*Simulador de torneio de jogos repetidos do tipo "dilema do prisioneiro"*

Este jogo faz parte do curso de verão de Python da FGV - EMAp (Escola de Matemática Aplicada).
Foi desenvolvido pelos professores Flávio Codeço Coelho e Renato Rocha Souza e vem sendo aprimorado a cada edição do curso.



## Regras do Jogo

Neste jogo, você faz parte de uma tribo de caçadores. Nesta tribo existe uma tradição de que cada caçada é feita em duplas.

Logo, a cada rodada do jogo, cada jogador tem de sair em caçada com cada um dos outros caçadores da tribo. Para cada parceiro, o caçador tem a opção de caçar ou descansar. Esta decisão tem as seguintes consequências:   
 
+ Se o caçador descansar ele gasta **2** de energia
+ Se ele caçar ele gasta **6** de energia. 

Ao final da caçada a caça é dividida igualmente entre os caçadores. 

+ Uma caçada com dois caçadores gera 12 pontos de energia
+ Uma caçada com um caçador gera 6 pontos de energia
+ Se nenhum jogador escolhe caçar, não é gerado nenhum ponto de energia.

Portanto:

+ Se o caçador caçar e seu companheiro também caçar, ambos têm saldo **0** ao final. 
+ Se o caçador descansar enquanto o seu companheiro caça, o que descansou tem um saldo de **1** e seu companheiro tem um saldo de **-3** ao final. 
+ Se ambos descansarem, ambos têm saldo de **-2** pontos de energia ao final.

 Ao final de cada rodada de caçadas, se o número de caçadores for maior do que: 
 
 <a href="http://www.codecogs.com/eqnedit.php?latex=M&space;~&space;Uniform(0,n*(n-1))" target="_blank"><img src="http://latex.codecogs.com/gif.latex?M&space;~&space;Uniform(0,n*(n-1))" title="M ~ Uniform(0,n*(n-1))" /></a>
 
 onde n é o número de jogadores vivos, todos os menbros da tribo recebem uma recompensa de comida com tamanho: 
 
 <a href="http://www.codecogs.com/eqnedit.php?latex=$&space;2*(n-1)&space;$" target="_blank"><img src="http://latex.codecogs.com/gif.latex?$&space;2*(n-1)&space;$" title="$ 2*(n-1) $" /></a>
 
Os jogadores vão acumulando uma variável "reputação", que é definida por:

<a href="http://www.codecogs.com/eqnedit.php?latex=reputacao&space;=&space;\frac{cacas}{cacas&space;&plus;&space;descansos}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?reputacao&space;=&space;\frac{cacas}{cacas&space;&plus;&space;descansos}" title="reputacao = \frac{cacas}{cacas + descansos}" /></a>

A cada rodada, são recebidas pelos jogadores as seguintes informações:

+ Número da rodada
+ Reputação dos caçadores (em ordem aleatória)
+ Valor M sorteado 

Deve-se retornar ao simulador do torneio suas escolhas de caça para cada um dos outros membros da tribo, na ordem recebida. 

### Agradecimentos

Nós agradecemos aos vários alunos que aprenderam a programar em parte estimulados por este jogo.
Suas estratégias estão preservadas neste repositório.

Este jogo está licenciado sob a licença MIT.

Se você utiliza e material e gostaria de citá-lo, por favor use a seguinte referência:

**Coelho, Flavio codeço, & Souza, Renato Rocha. (2017, October 2). Jogos Vorazes. Zenodo. http://doi.org/10.5281/zenodo.1000761** 
