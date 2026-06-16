"""
AULA 4 - Dashboard Visual + Export
====================================

Topicos aplicados:
- Visualizacao de dados (matplotlib)
- Conectando dados (concat e merge)
- Salvando dados (to_csv, to_excel, download)

As funcoes de grafico devem RETORNAR a figura matplotlib (fig), nao chamar
plt.show(). O Streamlit cuida de exibir.
"""

import io
import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras_top_artistas(df: pd.DataFrame, n: int = 10):
    """
    Grafico de barras horizontais com os N artistas que mais somam streams.

    Dica: ax.barh(...). Retorne fig (sem plt.show()).
    """
    # Agrupa os streams por artista, soma e ordena do maior para o menor.
    top_artistas = (
        df.groupby("artist(s)_name")["streams"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

    # Cria o gráfico com barras horizontais.
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_artistas.index, top_artistas.values, color="#1DB954")

    # Ajusta a aparência para ficar mais legível.
    ax.invert_yaxis()
    ax.set_title("Top artistas por streams")
    ax.set_xlabel("Streams")
    ax.set_ylabel("Artista")
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    fig.tight_layout()

    return fig


def grafico_pizza_modo(df: pd.DataFrame):
    """
    Pizza com a proporcao de musicas em modo 'Major' x 'Minor'.

    Dica: ax.pie(valores, labels=rotulos, autopct='%1.1f%%').
    """
    # Conta quantas músicas estão em cada modo.
    contagem = df["mode"].value_counts()

    # Organiza os rótulos na ordem esperada.
    labels = ["Major", "Minor"]
    valores = [contagem.get("Major", 0), contagem.get("Minor", 0)]

    # Cria o gráfico de pizza.
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        valores,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#1DB954", "#BDBDBD"],
    )
    ax.set_title("Proporção entre Major e Minor")
    ax.axis("equal")

    return fig


def grafico_linha_lancamentos_por_ano(df: pd.DataFrame):
    """
    Linha com a quantidade de lancamentos por ano (>= 2000).
    """
    # Mantém apenas anos a partir de 2000.
    df_filtrado = df[df["released_year"] >= 2000]

    # Conta quantas músicas foram lançadas por ano.
    contagem_por_ano = (
        df_filtrado.groupby("released_year")
        .size()
        .sort_index()
    )

    # Cria a linha do gráfico.
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(contagem_por_ano.index, contagem_por_ano.values, marker="o")

    # Ajusta rótulos e título.
    ax.set_title("Lançamentos por ano (a partir de 2000)")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Quantidade de lançamentos")
    ax.grid(True, linestyle="--", alpha=0.3)
    fig.tight_layout()

    return fig


def juntar_com_info_artistas(df_spotify: pd.DataFrame, df_info: pd.DataFrame) -> pd.DataFrame:
    """
    MERGE entre Spotify e info dos artistas (pais_origem, gravadora, etc).
    No df_spotify a coluna do artista e 'artist(s)_name'; no df_info e 'artist_name'.
    Use how='left' para nao perder musicas.
    """
    return pd.merge(
        df_spotify,
        df_info,
        left_on="artist(s)_name",
        right_on="artist_name",
        how="left",
    )


def unir_novos_lancamentos(df_atual: pd.DataFrame, df_novos: pd.DataFrame) -> pd.DataFrame:
    """
    CONCAT vertical (axis=0) entre df_atual e df_novos. Depois drop_duplicates.
    """
    concatenado = pd.concat([df_atual, df_novos], axis=0, ignore_index=True)
    return concatenado.drop_duplicates()


def salvar_resultado(df: pd.DataFrame, caminho: str) -> None:
    """
    Salva o DataFrame em CSV no caminho informado, sem indice e encoding utf-8.
    """
    # Salva o DataFrame como CSV no caminho informado.
    # - `caminho` pode ser uma string ou um objeto Path.
    # - Salvamos sem índice (`index=False`) e com encoding UTF-8 para compatibilidade.
    df.to_csv(caminho, index=False, encoding="utf-8")


def grafico_dispersao_energia_dancabilidade(df: pd.DataFrame):
    """
    Scatter plot: eixo X = 'energy_%', eixo Y = 'danceability_%'.

    Passos:
      1) fig, ax = plt.subplots(figsize=(8, 6))
      2) ax.scatter(df['energy_%'], df['danceability_%'], alpha=0.5)
      3) Titulo e labels
      4) Retornar fig
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df['energy_%'], df['danceability_%'], alpha=0.5)
    ax.set_title("Energia vs Dancabilidade")
    ax.set_xlabel("Energy (%)")
    ax.set_ylabel("Danceability (%)")
    ax.grid(True, linestyle="--", alpha=0.3)
    fig.tight_layout()
    return fig


def grafico_histograma_bpm(df: pd.DataFrame, bins: int = 30):
    """
    Histograma do BPM (batidas por minuto).

    Passos:
      1) fig, ax = plt.subplots()
      2) ax.hist(df['bpm'], bins=bins)
      3) Titulo e labels
      4) Retornar fig
    """
    # Prepara os dados: remove valores ausentes para evitar erros no histograma.
    dados_bpm = df["bpm"].dropna()

    # Cria a figura e desenha o histograma.
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(dados_bpm, bins=bins, color="#1DB954", edgecolor="black", alpha=0.9)

    # Ajustes visuais e rótulos para facilitar a leitura por um leigo.
    ax.set_title("Distribuição de BPM (batidas por minuto)")
    ax.set_xlabel("BPM")
    ax.set_ylabel("Quantidade de faixas")
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    fig.tight_layout()
    return fig


def salvar_em_excel(df: pd.DataFrame, caminho: str) -> None:
    """
    Salva o DataFrame em formato Excel (.xlsx) no caminho informado, sem
    indice.

    Dica: df.to_excel(caminho, index=False). Precisa do pacote openpyxl
    instalado (ja esta no requirements.txt).
    """
    # Salva o DataFrame em formato Excel (.xlsx) sem índice.
    # Recomendação: passe um caminho com extensão .xlsx.
    df.to_excel(caminho, index=False)


def preparar_csv_para_download(df: pd.DataFrame) -> bytes:
    """
    Prepara o DataFrame como CSV pronto para ser baixado pelo botao
    st.download_button do Streamlit.

    DIFERENCA para salvar_resultado: aqui NAO escrevemos em arquivo. A funcao
    deve retornar os BYTES do CSV. O Streamlit recebe esses bytes diretamente.

    Passos:
      1) Use df.to_csv(index=False) (SEM passar caminho — retorna string).
      2) Converta a string para bytes com .encode('utf-8').
      3) Retorne os bytes.

    Exemplo de uso no Streamlit:
      bytes_csv = preparar_csv_para_download(df)
      st.download_button("Baixar", bytes_csv, "dados.csv", "text/csv")
    """
    # Converte o DataFrame para string CSV (sem salvar em disco) e retorna os bytes.
    # Isso permite que o Streamlit ofereça o download direto para o usuário.
    csv_text = df.to_csv(index=False)
    csv_bytes = csv_text.encode("utf-8")
    return csv_bytes
