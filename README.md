# Spotify Tracks Dataset — Exploração Visual

Visualização exploratória da base [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) para o **TCC de Sistemas de Informação (UFJF)**.

## Como visualizar (orientador / banca)

**Não é necessário instalar nada nem executar código.**

Abra o link do GitHub Pages (após ativação):

> **https://muowl.github.io/spotify-dataset-explorer/**

Se o Pages ainda não estiver ativo, abra o arquivo estático:

- [docs/index.html](docs/index.html) (baixe ou visualize no repositório)

O HTML já contém todos os gráficos e tabelas pré-renderizados.

## O que este repositório contém

| Caminho | Descrição |
|---------|-----------|
| `docs/index.html` | **Visualizador principal** — abra no navegador |
| `notebooks/01_eda_spotify_tracks.ipynb` | Notebook fonte (código da EDA) |
| `data/README.md` | Origem e descrição da base |

## Fonte dos dados

- **Dataset:** Spotify Tracks Dataset (maharshipandya)
- **Origem:** Spotify Web API
- **Tamanho aproximado:** ~114.000 tracks, ~114 gêneros
- **Formato:** CSV
- **Links:** [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) · [Hugging Face](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)

## Conteúdo da exploração

1. Visão geral (tamanho, gêneros, artistas, explicit)
2. Distribuição dos top 20 gêneros
3. Histogramas das audio features + popularity
4. Matriz de correlação
5. Scatters popularity × energy / valence / danceability
6. Boxplots de popularity por gênero
7. Observações relevantes para o desenho do TCC (recomendações baseadas em conteúdo)

## Ativar GitHub Pages (uma vez)

1. Vá em **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` · pasta: `/docs`
4. Salve. Em alguns minutos o link `https://muowl.github.io/spotify-dataset-explorer/` ficará disponível.

## Contexto do TCC

Este material apoia a fase de entendimento da base de dados que será utilizada nos experimentos de recomendação musical (abordagens content-based / features de áudio).
