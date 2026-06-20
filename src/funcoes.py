import random
import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    LARGURA_NAVE,
    ALTURA_NAVE,
    LARGURA_METEORO,
    ALTURA_METEORO,
    VELOCIDADE_METEORO,
)


def criar_jogador():
    """Cria o retângulo que representa a nave do jogador."""
    x = LARGURA_TELA // 2 - LARGURA_NAVE // 2
    y = ALTURA_TELA - ALTURA_NAVE - 20

    jogador = {
        "rect": pygame.Rect(x, y, LARGURA_NAVE, ALTURA_NAVE),
        "vidas": 3
    }

    return jogador


def criar_meteoro(velocidade_base=None):
    """Cria um meteoro em uma posição aleatória no topo da tela."""
    if velocidade_base is None:
        velocidade_base = VELOCIDADE_METEORO

    x = random.randint(0, LARGURA_TELA - LARGURA_METEORO)
    y = random.randint(-300, -40)

    meteoro = {
        "rect": pygame.Rect(x, y, LARGURA_METEORO, ALTURA_METEORO),
        "velocidade": velocidade_base + random.randint(-1, 2),
        "tom": random.randint(0, 2),
    }

    return meteoro


def criar_lista_meteoros(quantidade, velocidade_base=None):
    """Cria uma lista com vários meteoros."""
    meteoros = []

    for i in range(quantidade):
        meteoros.append(criar_meteoro(velocidade_base))

    return meteoros


def mover_jogador(jogador, teclas):
    """Move a nave do jogador para esquerda e direita."""
    if teclas[pygame.K_LEFT]:
        jogador["rect"].x -= 7

    if teclas[pygame.K_RIGHT]:
        jogador["rect"].x += 7

    # Impede a nave de sair da tela
    if jogador["rect"].left < 0:
        jogador["rect"].left = 0

    if jogador["rect"].right > LARGURA_TELA:
        jogador["rect"].right = LARGURA_TELA


def mover_meteoros(meteoros):
    """Move todos os meteoros para baixo."""
    for meteoro in meteoros:
        meteoro["rect"].y += meteoro["velocidade"]


def reposicionar_meteoro(meteoro, velocidade_base=None):
    """Reposiciona um meteoro no topo da tela."""
    meteoro["rect"].x = random.randint(0, LARGURA_TELA - LARGURA_METEORO)
    meteoro["rect"].y = random.randint(-300, -40)

    if velocidade_base is not None:
        meteoro["velocidade"] = velocidade_base + random.randint(-1, 2)


def atualizar_meteoros(meteoros, velocidade_base=None):
    """
    Verifica se os meteoros saíram da tela.
    Quando um meteoro passa pela tela, ele volta para o topo.
    Retorna quantos pontos o jogador ganhou.
    """
    pontos_ganhos = 0

    for meteoro in meteoros:
        if meteoro["rect"].top > ALTURA_TELA:
            reposicionar_meteoro(meteoro, velocidade_base)
            pontos_ganhos += 1

    return pontos_ganhos


def verificar_colisao(jogador, meteoros, velocidade_base=None):
    """Verifica se a nave colidiu com algum meteoro."""
    for meteoro in meteoros:
        if jogador["rect"].colliderect(meteoro["rect"]):
            reposicionar_meteoro(meteoro, velocidade_base)
            return True

    return False


def jogador_perdeu(jogador):
    """Verifica se o jogador ficou sem vidas."""
    return jogador["vidas"] <= 0