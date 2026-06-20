import pygame

from src.config import (
    CAMINHO_SOM_PONTO,
    CAMINHO_SOM_COLISAO,
    CAMINHO_SOM_FIM,
    CAMINHO_SOM_SELECIONAR,
    CAMINHO_SOM_CONFIRMAR,
)

_CAMINHOS = {
    "ponto": CAMINHO_SOM_PONTO,
    "colisao": CAMINHO_SOM_COLISAO,
    "fim": CAMINHO_SOM_FIM,
    "selecionar": CAMINHO_SOM_SELECIONAR,
    "confirmar": CAMINHO_SOM_CONFIRMAR,
}


def carregar_sons():
    """
    Carrega os efeitos sonoros do jogo.

    Caso o áudio não esteja disponível no ambiente (sem placa de som,
    por exemplo), o jogo continua funcionando normalmente sem sons.
    """
    sons = {}

    for nome, caminho in _CAMINHOS.items():
        try:
            sons[nome] = pygame.mixer.Sound(caminho)
        except (pygame.error, FileNotFoundError):
            sons[nome] = None

    return sons


def tocar_som(sons, nome):
    """Toca um efeito sonoro pelo nome, se ele estiver disponível."""
    som = sons.get(nome)

    if som is not None:
        som.play()
