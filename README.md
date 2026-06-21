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

## Controles

* Seta para esquerda: mover a nave para a esquerda.
* Seta para direita: mover a nave para a direita.
* ENTER: iniciar a partida a partir da tela de início.
* Tecla R: reiniciar a partida após o fim do jogo.
* Tecla ESC: sair do jogo (funciona na tela de início e durante a partida).

## Funcionalidades

* Tela de início com título, instruções de controles e recorde atual.
* Janela principal do jogo com Pygame.
* Nave controlável pelo jogador (com sombra e contorno).
* Meteoros caindo pela tela (com contorno colorido).
* Fundo com estrelas em movimento (efeito parallax).
* Sistema de pontuação com exibição do nível atual no HUD.
* Sistema de vidas.
* Detecção de colisão.
* Dificuldade progressiva: a cada 10 pontos o nível sobe, aumentando a velocidade dos meteoros; a cada 2 níveis, um meteoro extra aparece na tela.
* Tela de fim de jogo com cores distintas para vitória (verde) e derrota (vermelho).
* Salvamento de recorde em arquivo.
* Infraestrutura de efeitos sonoros: coloque arquivos `.wav` em `assets/sons/` e eles serão carregados automaticamente (sem erro se ausentes).
* Testes automatizados para funções de lógica e dificuldade.

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
```

Execute o jogo:

```bash
python main.py
```

## Como executar os testes

O projeto utiliza `pytest` para executar testes simples da lógica do jogo.

Para rodar os testes, use:

```bash
python -m pytest
```

Os testes verificam funções relacionadas à criação do jogador, criação dos meteoros, colisão, derrota, pontuação, vitória e leitura/escrita do ranking.

## Entregas do projeto

### Semana 1 — Proposta inicial

Preenchido o arquivo `docs/proposta.md` com a ideia inicial do jogo.

### Semana 2 — Protótipo inicial

Primeira versão executável: janela do Pygame, loop principal, movimentação da nave.

### Semana 3 — Interações e regras principais

Sistema de pontuação, vidas, ranking em arquivo, condição de vitória/derrota, estruturas de dados e testes automatizados.

### Semana 4 — Entrega final

- Tela de início com instruções e recorde.
- Dificuldade progressiva por nível (velocidade e quantidade de meteoros).
- Melhoria estética: estrelas com parallax, sombra/contorno na nave, contorno nos meteoros, cores distintas na tela de fim.
- Módulo `src/sons.py` com carregamento seguro de efeitos sonoros `.wav`.
- Novos testes automatizados para as funções de dificuldade (26 testes no total).

## Recursos externos previstos

Inicialmente, o jogo utiliza formas geométricas criadas pelo próprio Pygame, sem imagens externas obrigatórias.

Caso sejam utilizadas imagens, sons, fontes ou outros recursos externos, eles serão indicados neste README com suas respectivas origens.

## Integrantes

* Felipe Gabriel Nogueira Aquino
* Leonardo Martins Macedo
* Pedro Henrique Oliveira Maia

## Status do projeto

Versão final entregue — Semana 4.
