# Astro Rush

Astro Rush é um jogo simples de sobrevivência e desvio de obstáculos desenvolvido em Python utilizando a biblioteca Pygame.

O projeto faz parte da atividade final da disciplina, com o objetivo de aplicar conceitos estudados durante o período, como variáveis, estruturas condicionais, laços de repetição, listas, dicionários, funções, modularização, leitura e escrita de arquivos, testes e organização de código.

## Descrição do jogo

Em Astro Rush, o jogador controla uma nave espacial que deve desviar de meteoros que caem pela tela.

O objetivo é sobreviver pelo maior tempo possível, acumulando pontos e tentando superar o próprio recorde. A dificuldade poderá aumentar conforme a partida avança, tornando os meteoros mais rápidos ou mais frequentes.

## Tipo de jogo

Jogo de sobrevivência simples / nave desviando de meteoros.

## Objetivo do jogador

O jogador deve controlar a nave espacial, desviar dos meteoros e alcançar a maior pontuação possível antes de perder todas as vidas.

## Regras principais

* O jogador controla uma nave espacial.
* Os meteoros aparecem na parte superior da tela.
* Os meteoros se movimentam para baixo.
* O jogador deve desviar dos meteoros usando o teclado.
* A pontuação aumenta enquanto o jogador permanece vivo.
* Cada colisão com um meteoro remove uma vida.
* A partida termina quando as vidas chegam a zero.
* O jogo poderá salvar o maior recorde em um arquivo.

## Controles previstos

* Seta para esquerda: mover a nave para a esquerda.
* Seta para direita: mover a nave para a direita.
* Tecla R: reiniciar a partida após o fim do jogo.
* Tecla ESC: sair do jogo.

## Funcionalidades previstas

* Janela principal do jogo com Pygame.
* Nave controlável pelo jogador.
* Meteoros caindo pela tela.
* Sistema de pontuação.
* Sistema de vidas.
* Detecção de colisão.
* Tela ou mensagem de fim de jogo.
* Salvamento de recorde em arquivo.
* Testes simples para funções da lógica do jogo.

## Tecnologias utilizadas

* Python
* Pygame
* Git
* GitHub

## Organização planejada do projeto

A organização inicial prevista para o projeto é:

```txt
projeto/
│
├── main.py
├── README.md
├── docs/
│   └── proposta.md
├── src/
│   ├── config.py
│   ├── jogo.py
│   ├── funcoes.py
│   └── dados.py
└── tests/
    └── test_funcoes.py
```

## Descrição dos arquivos planejados

* `main.py`: arquivo principal responsável por iniciar o jogo.
* `docs/proposta.md`: proposta inicial do jogo.
* `src/config.py`: configurações gerais, como tamanho da tela, cores e velocidades.
* `src/jogo.py`: loop principal e controle da partida.
* `src/funcoes.py`: funções auxiliares, como movimentação, colisão e pontuação.
* `src/dados.py`: leitura e escrita de dados em arquivo, como o recorde.
* `tests/test_funcoes.py`: testes simples para funções de lógica do jogo.

## Como executar

Instale as dependências:

```bash
python -m pip install -r requirements.txt

## Entregas do projeto

### Semana 1 — Proposta inicial

Nesta etapa, foi preenchido o arquivo `docs/proposta.md` com a ideia inicial do jogo, incluindo nome, tipo, descrição, objetivo, regras, controles, dificuldades esperadas e escopo mínimo.

### Semana 2 — Protótipo inicial

Será desenvolvida uma primeira versão executável do jogo, contendo janela do Pygame, loop principal, movimentação da nave e pelo menos um elemento interativo na tela.

### Semana 3 — Versão quase completa

Será implementada a maior parte das regras principais, incluindo pontuação, vidas, colisão, estruturas de dados, uso de arquivos e testes iniciais.

### Semana 4 — Entrega final

Será entregue a versão final do jogo, com código organizado, documentação atualizada, testes implementados, arquivos auxiliares necessários e preparação para apresentação.

## Recursos externos previstos

Inicialmente, o jogo poderá utilizar apenas formas geométricas criadas pelo próprio Pygame, sem imagens externas.

Caso sejam utilizadas imagens, sons, fontes ou outros recursos externos, eles serão indicados neste README com suas respectivas origens.

## Integrantes

* Felipe Gabriel Nogueira Aquino
* Leonardo Martins Macedo
* Pedro Henrique Oliveira Maia

## Status do projeto

Projeto em desenvolvimento.

Etapa atual: Semana 2 — Protótipo inicial executável.
