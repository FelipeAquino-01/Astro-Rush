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
    calcular_nivel,
    calcular_velocidade_meteoro,
    calcular_quantidade_meteoros,
    ajustar_dificuldade,
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


# --- Testes de dificuldade progressiva ---

def test_calcular_nivel_inicial():
    assert calcular_nivel(0, 10) == 1


def test_calcular_nivel_sobe_a_cada_10_pontos():
    assert calcular_nivel(10, 10) == 2
    assert calcular_nivel(20, 10) == 3
    assert calcular_nivel(50, 10) == 6


def test_calcular_nivel_pontos_intermediarios():
    assert calcular_nivel(9, 10) == 1
    assert calcular_nivel(11, 10) == 2


def test_calcular_velocidade_nivel_1():
    assert calcular_velocidade_meteoro(1, 5, 14) == 5


def test_calcular_velocidade_aumenta_com_nivel():
    assert calcular_velocidade_meteoro(2, 5, 14) == 6
    assert calcular_velocidade_meteoro(5, 5, 14) == 9


def test_calcular_velocidade_respeita_maximo():
    assert calcular_velocidade_meteoro(100, 5, 14) == 14


def test_calcular_quantidade_nivel_1():
    assert calcular_quantidade_meteoros(1, 3, 8) == 3


def test_calcular_quantidade_aumenta_a_cada_2_niveis():
    assert calcular_quantidade_meteoros(3, 3, 8) == 4
    assert calcular_quantidade_meteoros(5, 3, 8) == 5


def test_calcular_quantidade_respeita_maximo():
    assert calcular_quantidade_meteoros(100, 3, 8) == 8


def test_ajustar_dificuldade_atualiza_velocidade():
    meteoros = criar_lista_meteoros(3)
    meteoros, nivel = ajustar_dificuldade(meteoros, 10, 5, 14, 3, 8, 10)
    assert nivel == 2
    for m in meteoros:
        assert m["velocidade"] == 6


def test_ajustar_dificuldade_adiciona_meteoros():
    meteoros = criar_lista_meteoros(3)
    meteoros, nivel = ajustar_dificuldade(meteoros, 20, 5, 14, 3, 8, 10)
    assert nivel == 3
    assert len(meteoros) == 4


def test_ajustar_dificuldade_sem_pontos_nao_muda_nada():
    meteoros = criar_lista_meteoros(3)
    meteoros, nivel = ajustar_dificuldade(meteoros, 0, 5, 14, 3, 8, 10)
    assert nivel == 1
    assert len(meteoros) == 3
    for m in meteoros:
        assert m["velocidade"] == 5