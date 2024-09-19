# THE PLAIN

## Pré-requisitos

- O jogo foi desenvolvido na versão 3.12 do Python.
- Pygame: Para instalar, execute no terminal o comando `pip install pygame`.

## Descrição

    "The Plain" é um jogo ambientado em uma planície (e também porque eu estava sem criatividade). O jogador controla um mago que precisa enfrentar hordas de inimigos usando um livro mágico. O jogo possui 3 ondas de inimigos; a cada nova onda, aparecem novos inimigos. A dificuldade pode ser ajustada em "Options", quanto maior a dificuldade, menor o tempo necessário para invocar um novo inimigo. O jogo termina quando o jogador completa a última onda e a tela de "Win" é exibida.

## Como Jogar

- **Movimentação**: Use as teclas de seta ou WASD para mover o personagem.

- **Atirar**: Clique com o botão esquerdo do mouse para disparar projéteis.

- **Pausar**: Pressione TAB para pausar/despausar o jogo.

- **Iniciar onda**: Pressione Enter para iniciar a onda de inimigos.

## Arquivos

- **buttons**: Trata o sprite e o retângulo de cada botão.

- **config**: Armazena variáveis e funções de configuração, como o tamanho da tela.

- **enemies**: Gerencia a lista de inimigos e projéteis inimigos, o evento de invocação de inimigos e as classes de cada inimigo (mágico = de longo alcance).

- **main**: Gerencia tudo que acontece no loop principal do jogo.

- **player**: Gerencia variáveis e funções do jogador, como o livro mágico que foi substituído por uma pistola devido à versão antiga do personagem.

## Pastas

- **aud**: Armazena arquivos de áudio e um arquivo .py que carrega esses áudios e gerencia variáveis de controle de volume.

- **sprites**: Armazena os sprites usados no jogo.

- **font**: Armazena o arquivo da fonte usada no jogo (PressStart2.ttf).

## Bugs Não Corrigidos

- Em algumas telas, o clique do mouse produz som mesmo se nenhum botão for clicado.

- Em algumas telas, tanto o scroll do mouse quanto o botão direito podem selecionar botões, pois não foi filtrado para aceitar apenas o botão esquerdo.

- Problemas no reset: Não consegui apagar os projéteis inimigos quando o jogo é resetado, o que faz com que os projéteis permaneçam nas ondas 2 ou 1 após o reset.

## Ideias Não Exploradas

- **Criação de uma quarta onda**: Introduzir um chefe (boss) na quarta onda, com um design e mecânicas mais complexas do que os inimigos normais.

- **Armas e ataques diferentes para o jogador**: Adicionar uma variedade de armas e ataques que o jogador pode usar, proporcionando uma experiência mais dinâmica.

- **Itens coletáveis**: Implementar itens como poções de vida que o jogador pode coletar para recuperar saúde.

- **Sistema de mana**: Implementar um sistema de mana para controlar a quantidade de ataques. A mana aumentaria com o tempo após ser usada, adicionando uma camada extra de estratégia ao jogo.

- **Sistema de login**: Criar um sistema de login para armazenar dados de configurações em um arquivo `.json`. Isso permitiria aos jogadores salvar suas preferências e configurações de jogo.
# The-Plain-1.0
