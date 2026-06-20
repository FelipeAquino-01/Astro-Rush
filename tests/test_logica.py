from src.funcoes import (
    criar_jogador,
    criar_lista_meteoros,
    atualizar_meteoros,
    verificar_colisao,
    jogador_perdeu,
)

from src.dados import salvar_recorde, carregar_recorde
from src.config import ALTURA_TELA


def test_criar_jogador_com_3_vidas():
    jogador = criar_jogador()

    assert jogador["vidas"] == 3
    assert jogador["rect"].width > 0
    assert jogador["rect"].height > 0


def test_criar_lista_meteoros():
    meteoros = criar_lista_meteoros(3)

    assert len(meteoros) == 3


def test_atualizar_meteoros_soma_pontos_quando_meteoro_sai_da_tela():
    meteoros = criar_lista_meteoros(1)

    meteoros[0]["rect"].top = ALTURA_TELA + 10

    pontos = atualizar_meteoros(meteoros)

    assert pontos == 1


def test_verificar_colisao_retorna_true():
    jogador = criar_jogador()

    meteoros = [
        {
            "rect": jogador["rect"].copy(),
            "velocidade": 5
        }
    ]

    resultado = verificar_colisao(jogador, meteoros)

    assert resultado is True


def test_jogador_perdeu_com_zero_vidas():
    jogador = {
        "vidas": 0
    }

    assert jogador_perdeu(jogador) is True


def test_carregar_recorde_arquivo_inexistente(tmp_path):
    arquivo = tmp_path / "ranking.txt"

    resultado = carregar_recorde(arquivo)

    assert resultado == 0


def test_salvar_e_carregar_recorde(tmp_path):
    arquivo = tmp_path / "ranking.txt"

    salvar_recorde(arquivo, 50)

    resultado = carregar_recorde(arquivo)

    assert resultado == 50


def test_salvar_recorde_nao_diminui_pontuacao(tmp_path):
    arquivo = tmp_path / "ranking.txt"

    salvar_recorde(arquivo, 100)
    salvar_recorde(arquivo, 40)

    resultado = carregar_recorde(arquivo)

    assert resultado == 100