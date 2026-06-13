import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
    BRANCO,
    AZUL,
    VERMELHO,
    AMARELO,
    CAMINHO_RECORDE,
    QUANTIDADE_METEOROS,
    PONTOS_VITORIA,
)

from src.funcoes import (
    criar_jogador,
    criar_lista_meteoros,
    mover_jogador,
    mover_meteoros,
    atualizar_meteoros,
    verificar_colisao,
    jogador_perdeu,
    jogador_venceu,
    calcular_pontos,
    tomar_dano,
)

from src.dados import salvar_recorde, carregar_recorde


def desenhar_texto(tela, texto, tamanho, x, y, cor=BRANCO):
    """Desenha textos na tela."""
    fonte = pygame.font.SysFont("Arial", tamanho)
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))


def desenhar_nave(tela, jogador):
    """Desenha a nave do jogador."""
    rect = jogador["rect"]

    pygame.draw.polygon(
        tela,
        AZUL,
        [
            (rect.centerx, rect.top),
            (rect.left, rect.bottom),
            (rect.right, rect.bottom)
        ]
    )

    pygame.draw.polygon(
        tela,
        AMARELO,
        [
            (rect.centerx - 10, rect.bottom),
            (rect.centerx + 10, rect.bottom),
            (rect.centerx, rect.bottom + 15)
        ]
    )


def desenhar_meteoros(tela, meteoros):
    """Desenha todos os meteoros."""
    for meteoro in meteoros:
        pygame.draw.ellipse(tela, VERMELHO, meteoro["rect"])


def desenhar_tela_jogo(tela, jogador, meteoros, pontos, recorde):
    """Desenha todos os elementos do jogo."""
    tela.fill(PRETO)

    desenhar_nave(tela, jogador)
    desenhar_meteoros(tela, meteoros)

    desenhar_texto(tela, f"Pontos: {pontos}", 26, 10, 10)
    desenhar_texto(tela, f"Vidas: {jogador['vidas']}", 26, 10, 40)
    desenhar_texto(tela, f"Recorde: {recorde}", 26, 10, 70)
    desenhar_texto(tela, f"Meta: {PONTOS_VITORIA}", 26, 10, 100)

    pygame.display.update()


def desenhar_tela_fim(tela, mensagem, pontos, recorde):
    """Desenha a tela de fim de jogo."""
    tela.fill(PRETO)

    desenhar_texto(tela, mensagem, 50, 250, 190)
    desenhar_texto(tela, f"Pontuação final: {pontos}", 30, 270, 260)
    desenhar_texto(tela, f"Recorde: {recorde}", 30, 330, 300)
    desenhar_texto(tela, "Pressione R para reiniciar", 24, 260, 360)
    desenhar_texto(tela, "Pressione ESC para sair", 24, 280, 395)

    pygame.display.update()


def reiniciar_partida():
    """Reinicia os dados principais da partida."""
    jogador = criar_jogador()
    meteoros = criar_lista_meteoros(QUANTIDADE_METEOROS)
    pontos = 0

    return jogador, meteoros, pontos


def executar_jogo():
    """Executa o loop principal do jogo."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    jogador, meteoros, pontos = reiniciar_partida()
    recorde = carregar_recorde(CAMINHO_RECORDE)

    rodando = True
    fim_de_jogo = False
    mensagem_final = ""

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                if fim_de_jogo and evento.key == pygame.K_r:
                    jogador, meteoros, pontos = reiniciar_partida()
                    fim_de_jogo = False
                    mensagem_final = ""

        if not fim_de_jogo:
            teclas = pygame.key.get_pressed()

            mover_jogador(jogador, teclas)
            mover_meteoros(meteoros)

            pontos_ganhos = atualizar_meteoros(meteoros)
            pontos = calcular_pontos(pontos, pontos_ganhos)

            if verificar_colisao(jogador, meteoros):
                jogador["vidas"] = tomar_dano(jogador["vidas"], 1)

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(CAMINHO_RECORDE, recorde)

            if jogador_perdeu(jogador):
                fim_de_jogo = True
                mensagem_final = "FIM DE JOGO"

            if jogador_venceu(pontos, PONTOS_VITORIA):
                fim_de_jogo = True
                mensagem_final = "VOCE VENCEU!"

            pygame.display.set_caption(
                f"{TITULO_JOGO} | Pontos: {pontos} | Vidas: {jogador['vidas']} | Recorde: {recorde}"
            )

            desenhar_tela_jogo(tela, jogador, meteoros, pontos, recorde)

        else:
            desenhar_tela_fim(tela, mensagem_final, pontos, recorde)

    pygame.quit()