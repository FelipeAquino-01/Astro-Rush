# Configurações centrais do jogo

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Astro Rush"

# Cores em RGB
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (80, 80, 80)
CINZA_CLARO = (170, 170, 180)
AZUL = (50, 120, 255)
AZUL_CLARO = (120, 190, 255)
CIANO = (120, 230, 255)
VERMELHO = (220, 50, 50)
AMARELO = (255, 220, 80)
LARANJA = (255, 150, 60)

# Cor de fundo (gradiente do espaço)
FUNDO_TOPO = (8, 10, 35)
FUNDO_BASE = (0, 0, 0)

# Jogador
LARGURA_NAVE = 50
ALTURA_NAVE = 40
VELOCIDADE_NAVE = 7

# Meteoro
LARGURA_METEORO = 40
ALTURA_METEORO = 40
VELOCIDADE_METEORO = 5
QUANTIDADE_METEOROS = 3
CORES_METEORO = [
    (190, 60, 40),
    (210, 95, 45),
    (165, 45, 45),
]

# Estrelas do fundo
QUANTIDADE_ESTRELAS = 90

# Dificuldades disponíveis (afetam velocidade e quantidade de meteoros)
DIFICULDADES = {
    "facil": {
        "nome": "Fácil",
        "velocidade_meteoro": 4,
        "quantidade_meteoros": 3,
    },
    "medio": {
        "nome": "Médio",
        "velocidade_meteoro": 6,
        "quantidade_meteoros": 4,
    },
    "dificil": {
        "nome": "Difícil",
        "velocidade_meteoro": 9,
        "quantidade_meteoros": 6,
    },
}
ORDEM_DIFICULDADES = ["facil", "medio", "dificil"]

# Arquivos
CAMINHO_RECORDE = "data/ranking.txt"

# Sons
PASTA_SONS = "assets/sons"
CAMINHO_SOM_PONTO = f"{PASTA_SONS}/ponto.wav"
CAMINHO_SOM_COLISAO = f"{PASTA_SONS}/colisao.wav"
CAMINHO_SOM_FIM = f"{PASTA_SONS}/fim_de_jogo.wav"
CAMINHO_SOM_SELECIONAR = f"{PASTA_SONS}/selecionar.wav"
CAMINHO_SOM_CONFIRMAR = f"{PASTA_SONS}/confirmar.wav"