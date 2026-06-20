import math
import random

import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
    BRANCO,
    CINZA_CLARO,
    AZUL,
    AZUL_CLARO,
    CIANO,
    VERMELHO,
    AMARELO,
    LARANJA,
    FUNDO_TOPO,
    FUNDO_BASE,
    CORES_METEORO,
    QUANTIDADE_ESTRELAS,
    DIFICULDADES,
    ORDEM_DIFICULDADES,
    CAMINHO_RECORDE,
)

from src.funcoes import (
    criar_jogador,
    criar_lista_meteoros,
    mover_jogador,
    mover_meteoros,
    atualizar_meteoros,
    verificar_colisao,
    jogador_perdeu,
)

from src.dados import salvar_recorde, carregar_recorde
from src.som import carregar_sons, tocar_som

ESTADO_MENU = "menu"
ESTADO_JOGANDO = "jogando"
ESTADO_FIM = "fim"

OPCOES_DIFICULDADE = [DIFICULDADES[chave] for chave in ORDEM_DIFICULDADES]


def desenhar_texto(tela, texto, tamanho, x, y, cor=BRANCO, negrito=False):
    """Desenha um texto alinhado à esquerda na tela."""
    fonte = pygame.font.SysFont("Arial", tamanho, bold=negrito)
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))


def desenhar_texto_centralizado(tela, texto, tamanho, y, cor=BRANCO, negrito=False):
    """Desenha um texto centralizado horizontalmente na tela."""
    fonte = pygame.font.SysFont("Arial", tamanho, bold=negrito)
    imagem_texto = fonte.render(texto, True, cor)
    x = LARGURA_TELA // 2 - imagem_texto.get_width() // 2
    tela.blit(imagem_texto, (x, y))


def criar_estrelas(quantidade):
    """Cria as estrelas do fundo, usadas no menu e durante a partida."""
    estrelas = []

    for _ in range(quantidade):
        estrelas.append({
            "x": random.uniform(0, LARGURA_TELA),
            "y": random.uniform(0, ALTURA_TELA),
            "tamanho": random.choice([1, 1, 2]),
            "velocidade": random.uniform(0.4, 2.2),
        })

    return estrelas


def mover_estrelas(estrelas):
    """Move as estrelas para baixo, criando um efeito de profundidade."""
    for estrela in estrelas:
        estrela["y"] += estrela["velocidade"]

        if estrela["y"] > ALTURA_TELA:
            estrela["y"] = 0
            estrela["x"] = random.uniform(0, LARGURA_TELA)


def desenhar_fundo(tela, estrelas):
    """Desenha um gradiente espacial e as estrelas por cima dele."""
    for y in range(0, ALTURA_TELA, 4):
        t = y / ALTURA_TELA
        cor = (
            int(FUNDO_TOPO[0] + (FUNDO_BASE[0] - FUNDO_TOPO[0]) * t),
            int(FUNDO_TOPO[1] + (FUNDO_BASE[1] - FUNDO_TOPO[1]) * t),
            int(FUNDO_TOPO[2] + (FUNDO_BASE[2] - FUNDO_TOPO[2]) * t),
        )
        pygame.draw.line(tela, cor, (0, y), (LARGURA_TELA, y), 4)

    for estrela in estrelas:
        cor = BRANCO if estrela["tamanho"] > 1 else CINZA_CLARO
        pygame.draw.circle(
            tela, cor, (int(estrela["x"]), int(estrela["y"])), estrela["tamanho"]
        )


def desenhar_nave(tela, jogador, tempo=0):
    """Desenha a nave do jogador com um brilho e chama animada."""
    rect = jogador["rect"]

    brilho = pygame.Surface((rect.width * 2, rect.height * 2), pygame.SRCALPHA)
    pygame.draw.ellipse(brilho, (*AZUL, 70), brilho.get_rect())
    tela.blit(brilho, (rect.centerx - rect.width, rect.centery - rect.height))

    pontos_corpo = [
        (rect.centerx, rect.top),
        (rect.left, rect.bottom),
        (rect.right, rect.bottom),
    ]
    pygame.draw.polygon(tela, AZUL, pontos_corpo)
    pygame.draw.polygon(tela, BRANCO, pontos_corpo, 2)

    pygame.draw.circle(tela, CIANO, (rect.centerx, rect.top + rect.height // 3), 6)

    oscilacao = int(4 * math.sin(tempo / 80))
    pygame.draw.polygon(
        tela,
        AMARELO,
        [
            (rect.centerx - 8, rect.bottom),
            (rect.centerx + 8, rect.bottom),
            (rect.centerx, rect.bottom + 14 + oscilacao),
        ],
    )
    pygame.draw.polygon(
        tela,
        LARANJA,
        [
            (rect.centerx - 4, rect.bottom),
            (rect.centerx + 4, rect.bottom),
            (rect.centerx, rect.bottom + 7 + oscilacao // 2),
        ],
    )


def desenhar_meteoros(tela, meteoros):
    """Desenha todos os meteoros com crateras e variação de tom."""
    for meteoro in meteoros:
        rect = meteoro["rect"]
        cor_base = CORES_METEORO[meteoro.get("tom", 0) % len(CORES_METEORO)]

        pygame.draw.ellipse(tela, cor_base, rect)
        pygame.draw.ellipse(tela, PRETO, rect, 2)

        for offset_x, offset_y, raio in ((0.3, 0.3, 0.12), (0.65, 0.5, 0.1), (0.4, 0.7, 0.08)):
            centro = (
                rect.left + int(rect.width * offset_x),
                rect.top + int(rect.height * offset_y),
            )
            pygame.draw.circle(tela, PRETO, centro, max(2, int(rect.width * raio)))


def desenhar_hud(tela, jogador, pontos, recorde, dificuldade):
    """Desenha o painel de informações no topo da tela."""
    painel = pygame.Surface((LARGURA_TELA, 60), pygame.SRCALPHA)
    painel.fill((0, 0, 0, 130))
    tela.blit(painel, (0, 0))

    desenhar_texto(tela, f"Pontos: {pontos}", 24, 10, 8)
    desenhar_texto(tela, f"Recorde: {recorde}", 24, 10, 32)

    for i in range(jogador["vidas"]):
        x = LARGURA_TELA - 30 - i * 28
        pygame.draw.polygon(
            tela, VERMELHO, [(x, 12), (x - 8, 28), (x + 8, 28)]
        )

    desenhar_texto(
        tela, f"Dificuldade: {dificuldade['nome']}", 18, LARGURA_TELA - 230, 36, CINZA_CLARO
    )


def desenhar_tela_jogo(tela, estrelas, jogador, meteoros, pontos, recorde, dificuldade, tempo):
    """Desenha todos os elementos do jogo."""
    desenhar_fundo(tela, estrelas)

    desenhar_nave(tela, jogador, tempo)
    desenhar_meteoros(tela, meteoros)

    desenhar_hud(tela, jogador, pontos, recorde, dificuldade)

    pygame.display.update()


def desenhar_tela_fim(tela, estrelas, pontos, recorde):
    """Desenha a tela de fim de jogo."""
    desenhar_fundo(tela, estrelas)

    desenhar_texto_centralizado(tela, "FIM DE JOGO", 54, 190, VERMELHO, negrito=True)
    desenhar_texto_centralizado(tela, f"Pontuação final: {pontos}", 30, 270)
    desenhar_texto_centralizado(tela, f"Recorde: {recorde}", 30, 312, AMARELO)
    desenhar_texto_centralizado(tela, "Pressione R para jogar novamente", 24, 380)
    desenhar_texto_centralizado(tela, "Pressione M para voltar ao menu", 24, 412)
    desenhar_texto_centralizado(tela, "Pressione ESC para sair", 22, 444, CINZA_CLARO)

    pygame.display.update()


def desenhar_menu(tela, estrelas, indice_selecionado):
    """Desenha o menu principal com a seleção de dificuldade."""
    desenhar_fundo(tela, estrelas)

    desenhar_texto_centralizado(tela, "ASTRO RUSH", 64, 90, AZUL_CLARO, negrito=True)
    desenhar_texto_centralizado(tela, "Escolha a dificuldade", 26, 190, CINZA_CLARO)

    for indice, dificuldade in enumerate(OPCOES_DIFICULDADE):
        selecionado = indice == indice_selecionado
        cor = AMARELO if selecionado else BRANCO
        prefixo = "> " if selecionado else "   "
        y = 260 + indice * 60

        desenhar_texto_centralizado(tela, f"{prefixo}{dificuldade['nome']}", 34, y, cor)

    desenhar_texto_centralizado(
        tela, "Use as setas para escolher e ENTER para começar", 20, 470, CINZA_CLARO
    )
    desenhar_texto_centralizado(tela, "ESC para sair", 18, 500, CINZA_CLARO)

    pygame.display.update()


def reiniciar_partida(dificuldade):
    """Cria os dados principais de uma nova partida para a dificuldade escolhida."""
    jogador = criar_jogador()
    meteoros = criar_lista_meteoros(
        dificuldade["quantidade_meteoros"], dificuldade["velocidade_meteoro"]
    )
    pontos = 0

    return jogador, meteoros, pontos


def executar_jogo():
    """Executa o loop principal do jogo, incluindo menu e dificuldade."""
    pygame.init()

    try:
        pygame.mixer.init()
    except pygame.error:
        pass

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()

    sons = carregar_sons()
    estrelas = criar_estrelas(QUANTIDADE_ESTRELAS)

    recorde = carregar_recorde(CAMINHO_RECORDE)

    estado = ESTADO_MENU
    indice_selecionado = 0
    dificuldade_atual = OPCOES_DIFICULDADE[0]

    jogador, meteoros, pontos = None, None, 0

    rodando = True

    while rodando:
        relogio.tick(FPS)
        tempo = pygame.time.get_ticks()

        mover_estrelas(estrelas)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if estado == ESTADO_MENU:
                        rodando = False
                    else:
                        estado = ESTADO_MENU

                elif estado == ESTADO_MENU:
                    if evento.key in (pygame.K_UP, pygame.K_w):
                        indice_selecionado = (indice_selecionado - 1) % len(OPCOES_DIFICULDADE)
                        tocar_som(sons, "selecionar")

                    elif evento.key in (pygame.K_DOWN, pygame.K_s):
                        indice_selecionado = (indice_selecionado + 1) % len(OPCOES_DIFICULDADE)
                        tocar_som(sons, "selecionar")

                    elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                        dificuldade_atual = OPCOES_DIFICULDADE[indice_selecionado]
                        jogador, meteoros, pontos = reiniciar_partida(dificuldade_atual)
                        estado = ESTADO_JOGANDO
                        tocar_som(sons, "confirmar")

                elif estado == ESTADO_FIM:
                    if evento.key == pygame.K_r:
                        jogador, meteoros, pontos = reiniciar_partida(dificuldade_atual)
                        estado = ESTADO_JOGANDO

                    elif evento.key == pygame.K_m:
                        estado = ESTADO_MENU

        if estado == ESTADO_JOGANDO:
            velocidade_base = dificuldade_atual["velocidade_meteoro"]

            teclas = pygame.key.get_pressed()
            mover_jogador(jogador, teclas)
            mover_meteoros(meteoros)

            pontos_ganhos = atualizar_meteoros(meteoros, velocidade_base)
            if pontos_ganhos:
                pontos += pontos_ganhos
                tocar_som(sons, "ponto")

            if verificar_colisao(jogador, meteoros, velocidade_base):
                jogador["vidas"] -= 1
                tocar_som(sons, "colisao")

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(CAMINHO_RECORDE, recorde)

            if jogador_perdeu(jogador):
                estado = ESTADO_FIM
                tocar_som(sons, "fim")

            pygame.display.set_caption(
                f"{TITULO_JOGO} | Pontos: {pontos} | Vidas: {jogador['vidas']} | Recorde: {recorde}"
            )

            desenhar_tela_jogo(
                tela, estrelas, jogador, meteoros, pontos, recorde, dificuldade_atual, tempo
            )

        elif estado == ESTADO_MENU:
            pygame.display.set_caption(TITULO_JOGO)
            desenhar_menu(tela, estrelas, indice_selecionado)

        elif estado == ESTADO_FIM:
            desenhar_tela_fim(tela, estrelas, pontos, recorde)

    pygame.quit()
