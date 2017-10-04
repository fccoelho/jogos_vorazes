# Jogos vorazes


*Simulador de torneio de jogos repetidos do tipo "dilema do prisioneiro"*

Este jogo faz parte docurso de verão de Python da Escola de matemática aplicada da FGV.
Foi desenvolvido pelos professores Flávio Codeço Coelho e Renato Rocha Souza. e vem sendo melhorado a cada edição do curso.



## Regras do Jogo

Neste jogo, você faz parte de uma tribo de caçadores. Nesta tribo existe uam tradição de que cada caçada é feita em duplas.

Logo, a cada rodada do jogo, cada jogador tem de sair em caçada com cada outro caçador da tribo. Uma vez na caçada, cada caçador tem a opção de caçar ou descansar. Esta decisão tem as seguintes consequências: 
 
 Se o caçador descansar ele gasta **2** de energia e se ele caçar ele gasta **6** de energia. Ao final da caçada a caça é dividida igualmente entre os caçadores. Cada caçada resulta em **6** pontos de energia, enquanto que o descanso não traz nenhum ponto de energia.
 
 Portanto se o caçador caçar e seu companheiro também ambos, têm saldo **0** ao final. Se o caçador descansar enquanto o seu companheiro caça, o que descansou tem um saldo de **1** ao fimda caçada enquanto que seu companheiro tem um saldo negativo de **3**. Se ambos descansarem. Ambos perdem 2 pontos de energia.

 Ao final de cada Rodada de caçada, se o número de caçadores for maior do que $M~Uniform(0,n*(n-1))$ onde $n$ é o número de jogadores vivos, todos os menbros da tribo recebemuma recompensa de comida de $2*(n-1)$.


### Agradecimentos

Nós agradecemos aos vários alunos que aprenderam a programar em parte estimulados por este jogo.
Suas estratégias estão preservadas neste repositório.

Este jogo está licenciado sob a licença MIT.

Se você utiliza e material e gostaria de citá-lo, por favor use a seguinte referência:

**Coelho, Flavio codeço, & Souza, Renato Rocha. (2017, October 2). Jogos Vorazes. Zenodo. http://doi.org/10.5281/zenodo.1000761** 
