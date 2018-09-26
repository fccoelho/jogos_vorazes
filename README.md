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

+ Uma caçada com um caçador gera 12 pontos de energia
+ Uma caçada com um jogador gera 6 pontos de energia
+ Se nenhum jogador caça, não é gerado nenhum ponto de energia.

Portanto:

+ Se o caçador caçar e seu companheiro também caçar, ambos têm saldo **0** ao final. 
+ Se o caçador descansar enquanto o seu companheiro caça, o que descansou tem um saldo de **1** e seu companheiro tem um saldo de **-3** ao final. 
+ Se ambos descansarem, ambos têm saldo de **-2** pontos de energia.

 Ao final de cada Rodada de caçada, se o número de caçadores for maior do que $ M~Uniform(0,n*(n-1)) $ onde $ n $ é o número de jogadores vivos, todos os menbros da tribo recebem uma recompensa de comida de $ 2*(n-1) $.


### Agradecimentos

Nós agradecemos aos vários alunos que aprenderam a programar em parte estimulados por este jogo.
Suas estratégias estão preservadas neste repositório.

Este jogo está licenciado sob a licença MIT.

Se você utiliza e material e gostaria de citá-lo, por favor use a seguinte referência:

**Coelho, Flavio codeço, & Souza, Renato Rocha. (2017, October 2). Jogos Vorazes. Zenodo. http://doi.org/10.5281/zenodo.1000761** 
