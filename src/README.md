# Código-fonte (`src`)

Esta pasta contém os módulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, eventos, atualização e renderização (inclui tela de início, estrelas parallax e integração de sons).
- `config.py`: constantes globais (tela, cores, caminhos, FPS, parâmetros de dificuldade).
- `funcoes.py`: funções auxiliares de regra e lógica (movimentação, colisão, pontuação, dificuldade progressiva).
- `sprites.py`: carregamento e recorte de spritesheet.
- `dados.py`: leitura e gravação de dados (recorde/ranking).
- `sons.py`: carregamento seguro de efeitos sonoros `.wav`; o jogo roda normalmente se os arquivos não existirem.

## Dificuldade progressiva

A cada 10 pontos o nível sobe. As funções `calcular_nivel`, `calcular_velocidade_meteoro`, `calcular_quantidade_meteoros` e `ajustar_dificuldade` em `funcoes.py` controlam esse comportamento e são totalmente testáveis sem Pygame.

## Sons

Coloque arquivos `.wav` em `assets/sons/` (veja o README dessa pasta). O módulo `sons.py` carrega cada arquivo com segurança e expõe funções `tocar_colisao`, `tocar_ponto`, `tocar_vitoria` e `tocar_derrota`.

## Dica de evolução

Quando o projeto crescer, mantenha módulos pequenos e separados por responsabilidade.
