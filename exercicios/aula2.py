"""
AULA 2 - Explorador de Faixas
==============================

Tópicos aplicados:
- Inspeção de conteúdo (describe, value_counts)
- Atribuição e criação de colunas
- Filtros simples e com AND/OR
- Dados faltantes e duplicados
"""

import pandas as pd


def carregar_e_limpar(caminho_csv: str) -> pd.DataFrame:
    """
    Carrega o CSV do Spotify e limpa os dados.

    Passos:
    1. Lê o CSV com encoding latin-1.
    2. Converte a coluna streams para numérica.
    3. Remove linhas sem valor em streams.
    4. Remove duplicatas.
    5. Retorna o DataFrame limpo.
    """
    # Usa o encoding correto para preservar caracteres especiais no arquivo.
    df = pd.read_csv(caminho_csv, encoding="latin-1")

    # Converte para numérico e marca valores inválidos como NaN.
    df["streams"] = pd.to_numeric(df["streams"], errors="coerce")

    # Remove linhas sem streams, pois elas não podem ser analisadas corretamente.
    df = df.dropna(subset=["streams"])

    # Elimina duplicatas para evitar repetições indevidas na análise.
    df = df.drop_duplicates()

    return df


def inspecionar_coluna(df: pd.DataFrame, coluna: str):
    """
    Retorna uma visão resumida da coluna.

    Colunas numéricas usam describe; colunas categóricas usam value_counts.
    """
    # A decisão é baseada no tipo da coluna para mostrar o resumo mais útil.
    if pd.api.types.is_numeric_dtype(df[coluna]):
        return df[coluna].describe()

    return df[coluna].value_counts()


def filtrar_por_artista(df: pd.DataFrame, artista: str) -> pd.DataFrame:
    """
    Retorna as linhas em que o nome do artista contém o texto buscado.
    """
    # Usa contains com case=False para tornar a busca insensível a maiúsculas.
    return df[df["artist(s)_name"].str.contains(artista, case=False, na=False)]


def filtrar_hits(df: pd.DataFrame, ano_min: int, streams_min: int) -> pd.DataFrame:
    """
    Aplica um filtro com AND entre ano mínimo e número mínimo de streams.
    """
    # O uso de & garante que as duas condições sejam satisfeitas ao mesmo tempo.
    return df[(df["released_year"] >= ano_min) & (df["streams"] >= streams_min)]


def criar_categoria_streams(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria uma coluna com categorias com base no volume de streams.
    """
    # Trabalha em uma cópia para não alterar o DataFrame original.
    df_novo = df.copy()
    df_novo["categoria_streams"] = "Underground"

    # As condições são organizadas em ordem crescente para sobrescrever corretamente.
    df_novo.loc[df_novo["streams"] >= 100_000_000, "categoria_streams"] = "Medio"
    df_novo.loc[df_novo["streams"] >= 500_000_000, "categoria_streams"] = "Hit"
    df_novo.loc[df_novo["streams"] >= 1_000_000_000, "categoria_streams"] = "Super Hit"

    return df_novo


def filtrar_por_modo(df: pd.DataFrame, modo: str) -> pd.DataFrame:
    """
    Filtra o DataFrame pelo modo musical informado.
    """
    # O filtro simples é suficiente porque a comparação é direta.
    return df[df["mode"] == modo]


def filtrar_por_intervalo_ano(
    df: pd.DataFrame,
    ano_inicio: int,
    ano_fim: int,
) -> pd.DataFrame:
    """
    Retorna as músicas lançadas entre dois anos, inclusive.
    """
    # Usa duas condições com AND para incluir os limites do intervalo.
    return df[(df["released_year"] >= ano_inicio) & (df["released_year"] <= ano_fim)]


def filtrar_super_dancante_ou_super_energica(
    df: pd.DataFrame,
    limite: int = 85,
) -> pd.DataFrame:
    """
    Retorna músicas com danceability ou energy acima do limite.
    """
    # O operador | representa a lógica de OR entre as duas colunas.
    return df[(df["danceability_%"] >= limite) | (df["energy_%"] >= limite)]


def contar_nulos_por_coluna(df: pd.DataFrame) -> pd.Series:
    """
    Retorna a quantidade de valores nulos em cada coluna.
    """
    # isnull().sum() é a forma mais direta de resumir dados faltantes.
    return df.isnull().sum()


def preencher_nulos_da_coluna(df: pd.DataFrame, coluna: str, valor) -> pd.DataFrame:
    """
    Preenche os valores nulos de uma coluna sem alterar o DataFrame original.
    """
    # Cria uma cópia para preservar os dados originais e aplicar a alteração em uma nova estrutura.
    df_novo = df.copy()
    df_novo[coluna] = df_novo[coluna].fillna(valor)

    return df_novo
