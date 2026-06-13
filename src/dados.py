from pathlib import Path


def carregar_recorde(caminho_arquivo):
    """
    Carrega o maior recorde salvo no arquivo.

    Caso o arquivo não exista, esteja vazio ou tenha conteúdo inválido,
    a função retorna 0.
    """
    caminho = Path(caminho_arquivo)

    try:
        conteudo = caminho.read_text(encoding="utf-8").strip()

        if conteudo == "":
            return 0

        return int(conteudo)

    except FileNotFoundError:
        return 0

    except ValueError:
        return 0


def salvar_recorde(caminho_arquivo, pontuacao):
    """
    Salva a maior pontuação no arquivo de ranking.

    A função cria a pasta automaticamente, caso ela ainda não exista.
    O recorde só é atualizado se a nova pontuação for maior que a anterior.
    """
    caminho = Path(caminho_arquivo)

    caminho.parent.mkdir(parents=True, exist_ok=True)

    recorde_atual = carregar_recorde(caminho_arquivo)

    if pontuacao > recorde_atual:
        caminho.write_text(str(pontuacao), encoding="utf-8")
    else:
        caminho.write_text(str(recorde_atual), encoding="utf-8")