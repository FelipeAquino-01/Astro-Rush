from src.funcoes import (
    criar_jogador,
    criar_lista_meteoros,
    atualizar_meteoros,
    verificar_colisao,
    jogador_perdeu,
    calcular_pontos,
    jogador_venceu,
    limitar_valor,
    sortear_posicao,
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


def test_calcular_pontos():
    assert calcular_pontos(10, 5) == 15


def test_jogador_venceu_com_pontos_suficientes():
    assert jogador_venceu(100, 100) is True


def test_jogador_nao_venceu_com_poucos_pontos():
    assert jogador_venceu(90, 100) is False


def test_limitar_valor_abaixo_do_minimo():
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_dentro_do_intervalo():
    assert limitar_valor(50, 0, 100) == 50


def test_sortear_posicao_dentro_dos_limites():
    for _ in range(50):
        x, y = sortear_posicao(100, 200)

        assert 0 <= x <= 100
        assert 0 <= y <= 200


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