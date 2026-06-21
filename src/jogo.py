import random
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
    VERDE,
    LARANJA,
    CINZA_ESCURO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SONS,
    QUANTIDADE_METEOROS,
    PONTOS_VITORIA,
    VELOCIDADE_METEORO,
    VELOCIDADE_METEORO_MAX,
    QUANTIDADE_METEOROS_MAX,
    PONTOS_POR_NIVEL,
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
    ajustar_dificuldade,
)

from src.dados import salvar_recorde, carregar_recorde
from src.sons import carregar_sons, tocar_colisao, tocar_ponto, tocar_vitoria, tocar_derrota

# Número de estrelas no fundo
_QUANTIDADE_ESTRELAS = 80


def _criar_estrelas():
    """Cria lista de estrelas com posição e velocidade para efeito parallax."""
    estrelas = []
    for _ in range(_QUANTIDADE_ESTRELAS):
        x = random.randint(0, LARGURA_TELA)
        y = random.randint(0, ALTURA_TELA)
        velocidade = random.uniform(0.3, 1.5)
        tamanho = 1 if velocidade < 0.8 else 2
        estrelas.append({"x": x, "y": y, "vel": velocidade, "tam": tamanho})
    return estrelas


def _mover_estrelas(estrelas):
    for estrela in estrelas:
        estrela["y"] += estrela["vel"]
        if estrela["y"] > ALTURA_TELA:
            estrela["y"] = 0
            estrela["x"] = random.randint(0, LARGURA_TELA)


def _desenhar_estrelas(tela, estrelas):
    for estrela in estrelas:
        brilho = int(150 + estrela["vel"] * 60)
        cor = (brilho, brilho, brilho)
        pygame.draw.circle(tela, cor, (int(estrela["x"]), int(estrela["y"])), estrela["tam"])


def desenhar_texto(tela, texto, tamanho, x, y, cor=BRANCO):
    """Desenha texto na posição (x, y)."""
    fonte = pygame.font.SysFont("Arial", tamanho)
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))


def desenhar_texto_centralizado(tela, texto, tamanho, y, cor=BRANCO):
    """Desenha texto horizontalmente centralizado na tela."""
    fonte = pygame.font.SysFont("Arial", tamanho)
    imagem_texto = fonte.render(texto, True, cor)
    x = (LARGURA_TELA - imagem_texto.get_width()) // 2
    tela.blit(imagem_texto, (x, y))


def desenhar_nave(tela, jogador):
    """Desenha a nave com sombra e contorno."""
    rect = jogador["rect"]
    pontos = [
        (rect.centerx, rect.top),
        (rect.left, rect.bottom),
        (rect.right, rect.bottom),
    ]
    # Sombra
    sombra = [(x + 3, y + 3) for x, y in pontos]
    pygame.draw.polygon(tela, CINZA, sombra)
    # Contorno
    pygame.draw.polygon(tela, BRANCO, pontos, 2)
    # Preenchimento
    pygame.draw.polygon(tela, AZUL, pontos)
    # Chama
    chama = [
        (rect.centerx - 10, rect.bottom),
        (rect.centerx + 10, rect.bottom),
        (rect.centerx, rect.bottom + 15),
    ]
    pygame.draw.polygon(tela, AMARELO, chama)


def desenhar_meteoros(tela, meteoros):
    """Desenha meteoros com contorno."""
    for meteoro in meteoros:
        pygame.draw.ellipse(tela, VERMELHO, meteoro["rect"])
        pygame.draw.ellipse(tela, LARANJA, meteoro["rect"], 2)


def desenhar_tela_jogo(tela, jogador, meteoros, pontos, recorde, nivel, estrelas):
    """Desenha todos os elementos durante a partida."""
    tela.fill(CINZA_ESCURO)
    _desenhar_estrelas(tela, estrelas)

    desenhar_nave(tela, jogador)
    desenhar_meteoros(tela, meteoros)

    desenhar_texto(tela, f"Pontos: {pontos}", 26, 10, 10)
    desenhar_texto(tela, f"Vidas: {jogador['vidas']}", 26, 10, 40)
    desenhar_texto(tela, f"Recorde: {recorde}", 26, 10, 70)
    desenhar_texto(tela, f"Meta: {PONTOS_VITORIA}", 26, 10, 100)
    desenhar_texto(tela, f"Nível: {nivel}", 26, LARGURA_TELA - 120, 10)

    pygame.display.update()


def desenhar_tela_fim(tela, mensagem, pontos, recorde, venceu, estrelas):
    """Desenha a tela de fim de jogo com cores distintas para vitória/derrota."""
    cor_fundo = (0, 20, 0) if venceu else (30, 0, 0)
    cor_titulo = VERDE if venceu else VERMELHO
    tela.fill(cor_fundo)
    _desenhar_estrelas(tela, estrelas)

    desenhar_texto_centralizado(tela, mensagem, 60, 160, cor_titulo)
    desenhar_texto_centralizado(tela, f"Pontuação final: {pontos}", 32, 250, BRANCO)
    desenhar_texto_centralizado(tela, f"Recorde: {recorde}", 32, 295, AMARELO)
    desenhar_texto_centralizado(tela, "Pressione R para reiniciar", 26, 360, BRANCO)
    desenhar_texto_centralizado(tela, "Pressione ESC para sair", 26, 395, CINZA)

    pygame.display.update()


def desenhar_tela_inicio(tela, recorde, estrelas):
    """Desenha a tela de início antes da partida."""
    tela.fill(CINZA_ESCURO)
    _desenhar_estrelas(tela, estrelas)

    desenhar_texto_centralizado(tela, TITULO_JOGO, 72, 100, AMARELO)
    desenhar_texto_centralizado(tela, "Desvie dos meteoros e alcance a meta!", 24, 200, BRANCO)

    desenhar_texto_centralizado(tela, "Controles", 30, 270, LARANJA)
    desenhar_texto_centralizado(tela, "Seta Esquerda / Direita   —   mover a nave", 22, 308, BRANCO)
    desenhar_texto_centralizado(tela, "R   —   reiniciar após fim de jogo", 22, 336, BRANCO)
    desenhar_texto_centralizado(tela, "ESC   —   sair do jogo", 22, 364, BRANCO)

    desenhar_texto_centralizado(tela, f"Recorde atual: {recorde}", 26, 420, VERDE)

    desenhar_texto_centralizado(tela, "Pressione ENTER para começar", 30, 490, AMARELO)
    desenhar_texto_centralizado(tela, "ESC para sair", 20, 530, CINZA)

    pygame.display.update()


def reiniciar_partida():
    """Reinicia os dados principais da partida."""
    jogador = criar_jogador()
    meteoros = criar_lista_meteoros(QUANTIDADE_METEOROS)
    pontos = 0
    nivel = 1
    return jogador, meteoros, pontos, nivel


def executar_jogo():
    """Executa o loop principal do jogo."""
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    estrelas = _criar_estrelas()
    sons = carregar_sons(CAMINHO_SONS)

    jogador, meteoros, pontos, nivel = reiniciar_partida()
    recorde = carregar_recorde(CAMINHO_RECORDE)

    rodando = True
    fim_de_jogo = False
    na_tela_inicio = True
    venceu = False
    mensagem_final = ""
    som_fim_tocado = False

    while rodando:
        relogio.tick(FPS)
        _mover_estrelas(estrelas)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                if na_tela_inicio and evento.key == pygame.K_RETURN:
                    na_tela_inicio = False

                if fim_de_jogo and evento.key == pygame.K_r:
                    jogador, meteoros, pontos, nivel = reiniciar_partida()
                    fim_de_jogo = False
                    venceu = False
                    mensagem_final = ""
                    som_fim_tocado = False

        if na_tela_inicio:
            desenhar_tela_inicio(tela, recorde, estrelas)
            continue

        if not fim_de_jogo:
            teclas = pygame.key.get_pressed()

            mover_jogador(jogador, teclas)
            mover_meteoros(meteoros)

            pontos_ganhos = atualizar_meteoros(meteoros)
            if pontos_ganhos > 0:
                tocar_ponto(sons)
            pontos = calcular_pontos(pontos, pontos_ganhos)

            meteoros, nivel = ajustar_dificuldade(
                meteoros, pontos,
                VELOCIDADE_METEORO, VELOCIDADE_METEORO_MAX,
                QUANTIDADE_METEOROS, QUANTIDADE_METEOROS_MAX,
                PONTOS_POR_NIVEL,
            )

            if verificar_colisao(jogador, meteoros):
                tocar_colisao(sons)
                jogador["vidas"] = tomar_dano(jogador["vidas"], 1)

            if pontos > recorde:
                recorde = pontos
                salvar_recorde(CAMINHO_RECORDE, recorde)

            if jogador_perdeu(jogador):
                fim_de_jogo = True
                venceu = False
                mensagem_final = "FIM DE JOGO"

            if jogador_venceu(pontos, PONTOS_VITORIA):
                fim_de_jogo = True
                venceu = True
                mensagem_final = "VOCÊ VENCEU!"

            if fim_de_jogo and not som_fim_tocado:
                if venceu:
                    tocar_vitoria(sons)
                else:
                    tocar_derrota(sons)
                som_fim_tocado = True

            pygame.display.set_caption(
                f"{TITULO_JOGO} | Nível: {nivel} | Pontos: {pontos} | Recorde: {recorde}"
            )

            desenhar_tela_jogo(tela, jogador, meteoros, pontos, recorde, nivel, estrelas)

        else:
            desenhar_tela_fim(tela, mensagem_final, pontos, recorde, venceu, estrelas)

    pygame.quit()
