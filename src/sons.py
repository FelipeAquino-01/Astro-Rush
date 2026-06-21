import os
import pygame


def _carregar_som(caminho):
    """Carrega um arquivo .wav com segurança. Retorna None se não existir ou falhar."""
    if not os.path.isfile(caminho):
        return None
    try:
        return pygame.mixer.Sound(caminho)
    except Exception:
        return None


def _tocar(som):
    """Toca um som se ele estiver disponível."""
    if som is not None:
        som.play()


def carregar_sons(caminho_pasta):
    """
    Carrega todos os efeitos sonoros do jogo.
    Retorna um dicionário com os sons. Valores ausentes ficam como None.
    O jogo funciona normalmente mesmo sem os arquivos.
    """
    sons = {
        "colisao": _carregar_som(os.path.join(caminho_pasta, "colisao.wav")),
        "ponto":   _carregar_som(os.path.join(caminho_pasta, "ponto.wav")),
        "vitoria": _carregar_som(os.path.join(caminho_pasta, "vitoria.wav")),
        "derrota": _carregar_som(os.path.join(caminho_pasta, "derrota.wav")),
    }
    return sons


def tocar_colisao(sons):
    _tocar(sons.get("colisao"))


def tocar_ponto(sons):
    _tocar(sons.get("ponto"))


def tocar_vitoria(sons):
    _tocar(sons.get("vitoria"))


def tocar_derrota(sons):
    _tocar(sons.get("derrota"))
