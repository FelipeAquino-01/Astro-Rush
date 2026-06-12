import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    QUANTIDADE_GEMAS,
    QUANTIDADE_INIMIGOS,
    PONTOS_VITORIA,
    PRETO,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    jogador_venceu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    sortear_posicao,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)


def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens recortadas do Spritesheet


    # Jogador: usando tamanho 110x110 para capturar o quadrado perfeitamente
    player_image = pegar_sprite(CAMINHO_SPRITES, x=110, y=120, width=190, height=190, scale=0.5)

    # Gema pequena: usando tamanho 64x64
    gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)

    # Morcego: usando tamanho 180x120 por causa das asas abertas
    bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.5)
    
    # 2. Criando a estrutura de Sprites usando Dicionários
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, 100))
    }

    # Listas de dicionários: cada gema e cada inimigo é um dicionário
    # com sua imagem e seu rect, guardados dentro de uma lista.
    gemas = []
    for _ in range(QUANTIDADE_GEMAS):
        posicao = sortear_posicao(
            LARGURA_TELA - gem_image.get_width(),
            ALTURA_TELA - gem_image.get_height(),
        )
        gemas.append({
            "imagem": gem_image,
            "rect": gem_image.get_rect(topleft=posicao)
        })

    inimigos = []
    for _ in range(QUANTIDADE_INIMIGOS):
        posicao = sortear_posicao(
            LARGURA_TELA - bat_image.get_width(),
            ALTURA_TELA - bat_image.get_height(),
        )
        inimigos.append({
            "imagem": bat_image,
            "rect": bat_image.get_rect(topleft=posicao)
        })

    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Guarda a mensagem mostrada no fim da partida (vitória ou derrota).
    mensagem_final = ""

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            # Encerramento: fechar a janela ou apertar ESC termina o jogo
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        teclas = pygame.key.get_pressed()

        # Movimentação alterando direto os eixos X e Y do retângulo do jogador
        if teclas[pygame.K_LEFT]:
            jogador["rect"].x -= velocidade
        if teclas[pygame.K_RIGHT]:
            jogador["rect"].x += velocidade
        if teclas[pygame.K_UP]:
            jogador["rect"].y -= velocidade
        if teclas[pygame.K_DOWN]:
            jogador["rect"].y += velocidade

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        jogador["rect"].x = limitar_valor(jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width)
        jogador["rect"].y = limitar_valor(jogador["rect"].y, 0, ALTURA_TELA - jogador["rect"].height)

        # Verificação de colisão com cada gema da lista
        for gema in gemas:
            if verificar_colisao(jogador["rect"], gema["rect"]):
                pontos = calcular_pontos(pontos, 10)

                # Move a gema para uma nova posição aleatória ao coletar
                gema["rect"].topleft = sortear_posicao(
                    LARGURA_TELA - gema["rect"].width,
                    ALTURA_TELA - gema["rect"].height,
                )

        # Verificação de colisão com cada inimigo da lista
        for inimigo in inimigos:
            if verificar_colisao(jogador["rect"], inimigo["rect"]):
                vidas = tomar_dano(vidas, 1)

                # Afasta o inimigo para uma nova posição aleatória ao colidir
                inimigo["rect"].topleft = sortear_posicao(
                    LARGURA_TELA - inimigo["rect"].width,
                    ALTURA_TELA - inimigo["rect"].height,
                )

        # Regras de fim de jogo e recorde
        # Condição de derrota: o jogador perdeu todas as vidas
        if jogador_perdeu(vidas):
            mensagem_final = "GAME OVER"
            rodando = False

        # Condição de vitória: o jogador alcançou a pontuação necessária
        if jogador_venceu(pontos, PONTOS_VITORIA):
            mensagem_final = "VOCÊ VENCEU!"
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # Desenhando os elementos na tela percorrendo as listas de dicionários
        for gema in gemas:
            tela.blit(gema["imagem"], gema["rect"])
        for inimigo in inimigos:
            tela.blit(inimigo["imagem"], inimigo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    # Se a partida terminou em vitória ou derrota, mostra a tela final
    if mensagem_final != "":
        mostrar_tela_final(tela, mensagem_final, pontos)

    pygame.quit()


def mostrar_tela_final(tela, mensagem, pontos):
    """Mostra a mensagem de fim de jogo até o jogador apertar uma tecla ou fechar."""
    fonte_grande = pygame.font.Font(None, 72)
    fonte_pequena = pygame.font.Font(None, 36)

    texto_mensagem = fonte_grande.render(mensagem, True, PRETO)
    texto_pontos = fonte_pequena.render(f"Pontuação final: {pontos}", True, PRETO)

    tela.fill(CINZA)
    tela.blit(texto_mensagem, texto_mensagem.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 - 30)))
    tela.blit(texto_pontos, texto_pontos.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2 + 30)))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN:
                esperando = False