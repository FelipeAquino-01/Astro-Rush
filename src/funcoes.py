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
    VELOCIDADE_NAVE,
)


def sortear_posicao(largura_maxima, altura_maxima):
    """Sorteia uma posição (x, y) aleatória dentro dos limites informados."""
    x = random.randint(0, largura_maxima)
    y = random.randint(0, altura_maxima)
    return x, y


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_venceu(pontos, pontos_para_vencer):
    """Indica se o jogador alcançou a pontuação necessária para vencer."""
    return pontos >= pontos_para_vencer


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo

    if valor > maximo:
        return maximo

    return valor


def criar_jogador():
    """Cria o retângulo que representa a nave do jogador."""
    x = LARGURA_TELA // 2 - LARGURA_NAVE // 2
    y = ALTURA_TELA - ALTURA_NAVE - 20

    jogador = {
        "rect": pygame.Rect(x, y, LARGURA_NAVE, ALTURA_NAVE),
        "vidas": 3
    }

    return jogador


def criar_meteoro():
    """Cria um meteoro em uma posição aleatória no topo da tela."""
    x = random.randint(0, LARGURA_TELA - LARGURA_METEORO)
    y = random.randint(-300, -40)

    meteoro = {
        "rect": pygame.Rect(x, y, LARGURA_METEORO, ALTURA_METEORO),
        "velocidade": VELOCIDADE_METEORO
    }

    return meteoro


def criar_lista_meteoros(quantidade):
    """Cria uma lista com vários meteoros."""
    meteoros = []

    for _ in range(quantidade):
        meteoros.append(criar_meteoro())

    return meteoros


def mover_jogador(jogador, teclas):
    """Move a nave do jogador para esquerda e direita."""
    if teclas[pygame.K_LEFT]:
        jogador["rect"].x -= VELOCIDADE_NAVE

    if teclas[pygame.K_RIGHT]:
        jogador["rect"].x += VELOCIDADE_NAVE

    jogador["rect"].x = limitar_valor(
        jogador["rect"].x,
        0,
        LARGURA_TELA - jogador["rect"].width
    )


def mover_meteoros(meteoros):
    """Move todos os meteoros para baixo."""
    for meteoro in meteoros:
        meteoro["rect"].y += meteoro["velocidade"]


def reposicionar_meteoro(meteoro):
    """Reposiciona um meteoro no topo da tela."""
    meteoro["rect"].x = random.randint(0, LARGURA_TELA - LARGURA_METEORO)
    meteoro["rect"].y = random.randint(-300, -40)


def atualizar_meteoros(meteoros):
    """
    Verifica se os meteoros saíram da tela.
    Quando um meteoro passa pela tela, ele volta para o topo.
    Retorna quantos pontos o jogador ganhou.
    """
    pontos_ganhos = 0

    for meteoro in meteoros:
        if meteoro["rect"].top > ALTURA_TELA:
            reposicionar_meteoro(meteoro)
            pontos_ganhos += 1

    return pontos_ganhos


def verificar_colisao(objeto_1, objeto_2):
    """
    Verifica colisão.

    Pode receber:
    - jogador e lista de meteoros;
    - dois retângulos do Pygame.
    """
    if isinstance(objeto_2, list):
        jogador = objeto_1
        meteoros = objeto_2

        for meteoro in meteoros:
            if jogador["rect"].colliderect(meteoro["rect"]):
                reposicionar_meteoro(meteoro)
                return True

        return False

    return objeto_1.colliderect(objeto_2)


def jogador_perdeu(jogador_ou_vidas):
    """Verifica se o jogador ficou sem vidas."""
    if isinstance(jogador_ou_vidas, dict):
        return jogador_ou_vidas["vidas"] <= 0

    return jogador_ou_vidas <= 0