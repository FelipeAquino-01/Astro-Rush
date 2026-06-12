from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    jogador_venceu,
    limitar_valor,
    sortear_posicao,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_jogador_venceu_com_pontos_suficientes():
    """Deve indicar vitoria quando os pontos alcancam a meta."""
    assert jogador_venceu(100, 100) is True


def test_jogador_nao_venceu_com_poucos_pontos():
    """Nao deve indicar vitoria quando os pontos estao abaixo da meta."""
    assert jogador_venceu(90, 100) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_sortear_posicao_dentro_dos_limites():
    """Deve sortear posicoes sempre dentro dos limites informados."""
    for _ in range(50):
        x, y = sortear_posicao(100, 200)
        assert 0 <= x <= 100
        assert 0 <= y <= 200