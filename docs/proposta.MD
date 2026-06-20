# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

**Astro Rush**

## 2. Integrantes do grupo

* Nome 1: Felipe Gabriel Nogueira Aquino
* Nome 2: Leonardo Martins Macedo
* Nome 3: Pedro Henrique Oliveira Maia

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Nave desviando de meteoros / jogo de sobrevivência simples.

## 4. Descrição geral do jogo

Descrição:

> Astro Rush será um jogo simples desenvolvido em Python com a biblioteca Pygame. Na tela, aparecerá uma nave espacial controlada pelo jogador e meteoros que surgirão na parte superior da tela, caindo em direção à parte inferior. O jogador deverá mover a nave para a esquerda e para a direita para desviar dos meteoros. O principal desafio será sobreviver pelo maior tempo possível sem colidir com os obstáculos. Conforme a partida avança, a dificuldade poderá aumentar com meteoros mais rápidos ou mais frequentes.

## 5. Objetivo do jogador

Objetivo:

> O objetivo do jogador é controlar a nave espacial, desviar dos meteoros e sobreviver pelo maior tempo possível, acumulando pontos durante a partida. O jogador também poderá tentar superar o próprio recorde salvo pelo jogo.

## 6. Regras principais

Regras do grupo:

* Regra 1: O jogador começa a partida controlando uma nave espacial.
* Regra 2: Os meteoros surgem na parte superior da tela e se movimentam para baixo.
* Regra 3: O jogador deve desviar dos meteoros usando as setas do teclado.
* Regra 4: A pontuação aumenta enquanto o jogador permanece vivo.
* Regra 5: Cada colisão com um meteoro remove uma vida, e a partida termina quando as vidas chegam a zero.

## 7. Condição de vitória

Condição de vitória:

> Como Astro Rush será um jogo de sobrevivência, a vitória pode ser considerada quando o jogador atinge uma pontuação mínima, como 100 pontos. Mesmo após alcançar essa pontuação, o jogador poderá continuar jogando para tentar aumentar sua pontuação e superar o recorde.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> A derrota ocorre quando a nave colide com meteoros até perder todas as vidas disponíveis. Quando isso acontecer, a partida será encerrada e o jogo exibirá a pontuação final do jogador.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Descrição:

> O elemento principal será uma nave espacial controlada pelo jogador. A nave ficará inicialmente na parte inferior da tela e poderá se movimentar para a esquerda e para a direita.

## Obstáculos, inimigos ou desafios

Descrição:

> Os principais obstáculos serão meteoros que aparecerão em posições aleatórias na parte superior da tela e cairão em direção à nave. O jogador deverá desviar desses meteoros para continuar vivo.

## Itens, alvos ou objetos de interação

Descrição:

> Inicialmente, o jogo terá como principal interação o desvio dos meteoros. Caso haja tempo, poderão ser adicionados itens de bônus, como estrelas ou cristais espaciais, que aumentam a pontuação quando coletados.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador começará com 3 vidas. A pontuação aumentará conforme o tempo de sobrevivência durante a partida. O jogo também poderá salvar o maior recorde em um arquivo de texto.

## 10. Controles previstos

Controles do grupo:

* Seta para esquerda: mover a nave para a esquerda.
* Seta para direita: mover a nave para a direita.
* Tecla R: reiniciar a partida após o fim do jogo.
* Tecla ESC: sair do jogo.

## 11. Organização inicial do código

Organização planejada:

> O grupo pretende organizar o código de forma simples e clara, respeitando a estrutura do template oficial da disciplina. A organização inicial prevista é:

* `main.py`: arquivo principal responsável por iniciar o jogo.
* `src/config.py`: arquivo para guardar configurações, como tamanho da tela, cores e velocidade inicial.
* `src/jogo.py`: arquivo com o loop principal do jogo e controle da partida.
* `src/funcoes.py`: arquivo com funções auxiliares, como movimentação, criação de meteoros, colisão e pontuação.
* `src/dados.py`: arquivo com funções de leitura e escrita do recorde em arquivo.
* `tests/`: pasta destinada aos testes simples das funções de lógica do jogo.

## 12. Recursos externos previstos

Recursos previstos:

> O grupo poderá utilizar imagens simples de nave e meteoros obtidas de bancos gratuitos ou criadas manualmente. Caso algum recurso externo seja utilizado, sua origem será informada no README.md do projeto. Inicialmente, o jogo também poderá ser feito apenas com formas geométricas do próprio Pygame, sem necessidade de imagens externas.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

* Dificuldade 1: Implementar corretamente a movimentação da nave no Pygame.
* Dificuldade 2: Criar a colisão entre a nave e os meteoros.
* Dificuldade 3: Organizar o código em funções e arquivos separados.
* Dificuldade 4: Salvar e ler o recorde usando arquivo de texto.
* Dificuldade 5: Criar testes simples para as funções de lógica do jogo.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá uma janela funcionando no Pygame, uma nave controlada pelo teclado, meteoros caindo pela tela, sistema de vidas, sistema de pontuação, colisão entre nave e meteoros, condição de derrota, tela ou mensagem de fim de jogo e salvamento de recorde em arquivo. O código deverá estar organizado em funções e conter testes simples para algumas funções de lógica.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

* Melhoria 1: Adicionar tela inicial com nome do jogo e instruções.
* Melhoria 2: Adicionar sons de colisão, pontuação ou fundo.
* Melhoria 3: Adicionar aumento gradual de dificuldade.
* Melhoria 4: Adicionar itens de bônus para aumentar a pontuação.
* Melhoria 5: Adicionar ranking ou histórico de melhores pontuações.
