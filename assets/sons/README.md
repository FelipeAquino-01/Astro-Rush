# Sons — Astro Rush

Esta pasta contém os efeitos sonoros do jogo. O jogo funciona normalmente mesmo que os arquivos não estejam presentes — o carregamento é feito com segurança em `src/sons.py`.

## Arquivos esperados

| Arquivo        | Evento                                      |
|----------------|---------------------------------------------|
| `colisao.wav`  | Tocado quando a nave colide com um meteoro  |
| `ponto.wav`    | Tocado quando um meteoro passa pela tela    |
| `vitoria.wav`  | Tocado quando o jogador alcança a meta      |
| `derrota.wav`  | Tocado quando o jogador perde todas as vidas|

Todos os arquivos devem estar no formato `.wav` e colocados diretamente nesta pasta.

## Fontes de áudio gratuitas

Abaixo estão fontes recomendadas de sons com licenças livres para uso em projetos educacionais e não-comerciais:

- **Freesound** — https://freesound.org  
  Busque por termos como `explosion`, `coin`, `win`, `game over`. Verifique a licença de cada arquivo (prefira CC0 ou CC BY).

- **Kenney.nl** — https://kenney.nl/assets  
  Pacotes prontos de efeitos sonoros para jogos, todos em domínio público (CC0). Recomendado: *Interface Sounds*, *Impact Sounds*.

- **OpenGameArt** — https://opengameart.org  
  Acervo colaborativo com sons sob licenças CC0, CC BY e GPL. Filtre por `WAV` no campo de formato.

- **Mixkit** — https://mixkit.co/free-sound-effects/game  
  Efeitos prontos para jogos, gratuitos para uso sem atribuição obrigatória.

## Recomendações técnicas

- Use arquivos curtos (< 1 segundo) para efeitos de colisão e ponto.
- Normalize o volume antes de incluir para evitar diferenças bruscas entre os sons.
- Documente a origem de cada arquivo adicionado (nome do autor, URL, licença).
