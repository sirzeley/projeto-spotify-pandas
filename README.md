# Spotify Insights — Projeto Pandas Harve

Bem-vindo(a) ao **seu primeiro projeto de portfólio com Pandas + Streamlit!**

Ao longo das aulas 2, 3 e 4 você vai construir um dashboard interativo que analisa as músicas mais tocadas no Spotify em 2023. Ao final, você tem um app rodando localmente e um repositório no seu GitHub que pode mostrar em entrevistas.

## O que é esse projeto?

Um app Streamlit dividido em **3 abas**, uma por aula:

- **Aula 2 — Explorador de Faixas**: carregar e limpar dados, inspecionar colunas, filtros, criar categorias.
- **Aula 3 — Análise do Catálogo**: estatísticas, top artistas, médias por gênero (Major/Minor), agrupamentos por ano.
- **Aula 4 — Dashboard Visual + Export**: gráficos (barras, pizza, linha), juntar bases (merge/concat) e exportar resultados.

O esqueleto do app **já está pronto**. Sua missão é **preencher as funções** dentro de `exercicios/aula2.py`, `aula3.py` e `aula4.py`. Cada função tem um `# TODO` explicando o que ela deve fazer.

## Passo a passo

### 1. Faça um fork

Clique em **Fork** no canto superior direito deste repositório. Isso cria uma cópia na sua conta.

### 2. Clone seu fork

```bash
git clone https://github.com/SEU-USUARIO/projeto-spotify-pandas.git
cd projeto-spotify-pandas
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o app

```bash
streamlit run app.py
```

Ele abre no navegador. No começo você verá "função ainda não implementada" — é normal. É o que você vai resolver.

### 5. Trabalhe nos exercícios

Abra `exercicios/aula2.py`, implemente as funções com `# TODO`. Salve. No navegador, clique **Rerun** (canto superior direito) e veja o resultado.

### 6. Suba para o GitHub

Ao fim de cada aula:

```bash
git add .
git commit -m "Aula 2 concluída"
git push
```

## Estrutura

```
projeto-spotify-pandas/
├── app.py                    # App Streamlit (não precisa mexer)
├── requirements.txt
├── data/
│   ├── spotify-2023.csv             # Base principal (Kaggle)
│   ├── artistas_info.csv            # Para o merge (aula 4)
│   └── spotify_novos_lancamentos.csv  # Para o concat (aula 4)
└── exercicios/
    ├── aula2.py              # ← VOCÊ PREENCHE
    ├── aula3.py              # ← VOCÊ PREENCHE
    └── aula4.py              # ← VOCÊ PREENCHE
```

## Sobre os dados

Dataset **"Most Streamed Spotify Songs 2023"** do Kaggle. Colunas principais:

| Coluna | O que é |
|---|---|
| `track_name` | Nome da música |
| `artist(s)_name` | Artista (note o `(s)` no nome da coluna!) |
| `artist_count` | Quantos artistas participam |
| `released_year` / `released_month` / `released_day` | Data de lançamento |
| `streams` | Streams no Spotify (pode estar como texto!) |
| `bpm` | Batidas por minuto |
| `key`, `mode` | Tom e modo (Major/Minor) |
| `danceability_%`, `energy_%`, `valence_%` | Features (0-100) |

**Atenção:** algumas colunas têm `%` ou `(s)` no nome. Use sempre aspas: `df["danceability_%"]`.

## Dicas

- Não tem problema errar. Use `print()` no terminal para depurar as funções.
- Se travar, releia os slides da aula e teste num notebook antes.
- Pergunte no grupo da turma.

Bom projeto. 🎧

_version 1.0
