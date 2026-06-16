"""
AULA 3 - Análise do Catálogo
==========================

Neste arquivo, vamos responder perguntas com base nos dados do Spotify,
como:
- qual artista mais aparece em streams,
- quais músicas são mais dançantes,
- como os dados mudam por ano e por modo.
"""

import pandas as pd


def estatisticas_gerais(df: pd.DataFrame) -> dict:
    """
    Retorna um resumo rápido com os principais números do DataFrame.

    O dicionário contém:
    - total_streams: soma total de streams
    - media_bpm: média de BPM
    - media_danceability: média de danceability
    - ano_mais_recente: ano mais recente presente nos dados
    - ano_mais_antigo: ano mais antigo presente nos dados
    """
    # Soma todas as reproduções da coluna streams.
    total_streams = df["streams"].sum()

    # Calcula médias para colunas numéricas importantes.
    media_bpm = df["bpm"].mean()
    media_danceability = df["danceability_%"].mean()

    # Pega os extremos da coluna de ano.
    ano_mais_recente = df["released_year"].max()
    ano_mais_antigo = df["released_year"].min()

    return {
        "total_streams": total_streams,
        "media_bpm": media_bpm,
        "media_danceability": media_danceability,
        "ano_mais_recente": ano_mais_recente,
        "ano_mais_antigo": ano_mais_antigo,
    }


def top_n_artistas_por_streams(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Mostra os N artistas com mais streams somados.

    A lógica é:
    1. agrupar por artista,
    2. somar os streams,
    3. ordenar do maior para o menor,
    4. pegar apenas os primeiros N.
    """
    # Agrupa por artista, soma os streams e ordena em ordem decrescente.
    return (
        df.groupby("artist(s)_name")["streams"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def media_features_por_modo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a média das colunas de características por modo musical.

    O resultado mostra, por exemplo, se músicas em Major ou Minor tendem a
    ter mais danceability, energy ou valence.
    """
    # Agrupa por modo e calcula a média das colunas escolhidas.
    return (
        df.groupby("mode")[["danceability_%", "energy_%", "valence_%"]]
        .mean()
    )


def lancamentos_por_ano(df: pd.DataFrame) -> pd.Series:
    """
    Conta quantas músicas foram lançadas em cada ano.

    O resultado fica organizado do ano mais antigo para o mais recente.
    """
    # Conta quantas vezes cada ano aparece na coluna released_year.
    return df.groupby("released_year").size().sort_index()


def artista_mais_streamado_do_ano(df: pd.DataFrame, ano: int) -> str:
    """
    Retorna o nome do artista com mais streams em um ano específico.

    Se não existir nenhuma música para aquele ano, a função retorna uma
    mensagem clara informando isso.
    """
    # Filtra apenas as músicas do ano pedido.
    df_ano = df[df["released_year"] == ano]

    # Se o filtro vier vazio, não há dados para esse ano.
    if df_ano.empty:
        return f"Nenhuma musica encontrada para {ano}"

    # Soma streams por artista e pega o primeiro da lista ordenada.
    artista_mais_streamado = (
        df_ano.groupby("artist(s)_name")["streams"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    return artista_mais_streamado


def top_n_musicas_mais_dancantes(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Retorna as N músicas com maior valor de danceability.

    A saída contém apenas as colunas mais importantes para a análise.
    """
    # Ordena do maior para o menor danceability e seleciona as colunas desejadas.
    return (
        df.sort_values("danceability_%", ascending=False)
        .head(n)[["track_name", "artist(s)_name", "danceability_%"]]
    )


def streams_por_decada(df: pd.DataFrame) -> pd.Series:
    """
    Soma os streams por década de lançamento.

    Exemplo:
    - 2017 vira a década de 2010
    - 1985 vira a década de 1980
    """
    # Cria uma cópia para não modificar o DataFrame original.
    df_copia = df.copy()

    # Calcula a década usando divisão inteira e multiplicação por 10.
    df_copia["decada"] = (df_copia["released_year"] // 10) * 10

    # Soma os streams agrupando pela década e ordena pela década.
    return (
        df_copia.groupby("decada")["streams"]
        .sum()
        .sort_index()
    )


def bpm_medio_por_modo(df: pd.DataFrame) -> pd.Series:
    """
    Calcula o BPM médio para cada modo musical.
    """
    # Agrupa por modo e calcula a média da coluna bpm.
    return df.groupby("mode")["bpm"].mean()


def musicas_por_quantidade_de_artistas(df: pd.DataFrame) -> pd.Series:
    """
    Conta quantas músicas têm 1 artista, 2 artistas, 3 artistas, etc.

    O índice da Série mostra a quantidade de artistas, e os valores mostram
    quantas músicas pertencem a cada categoria.
    """
    # Conta a frequência da coluna artist_count e ordena pelo número de artistas.
    return df["artist_count"].value_counts().sort_index()


def ano_com_mais_streams(df: pd.DataFrame) -> int:
    """
    Retorna o ano em que a soma de streams foi maior.

    Em outras palavras, identifica o ano mais relevante em termos de
    volume total de reproduções.
    """
    # Agrupa por ano, soma os streams e pega o índice com valor máximo.
    return df.groupby("released_year")["streams"].sum().idxmax()
