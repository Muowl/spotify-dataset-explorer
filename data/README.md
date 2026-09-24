# Dados

A base **não** está versionada neste repositório (arquivo ~20 MB).

## Como obter

1. **Kaggle:** https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset  
2. **Hugging Face:** https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset  

Arquivo principal: `dataset.csv`

Após baixar, execute `python scripts/build_global_hits.py` a partir da raiz do repositório para recriar `docs/assets/hits-data.js`. O CSV é ignorado pelo Git; o arquivo JavaScript gerado é versionado para o GitHub Pages funcionar sem processamento no servidor.

## Colunas principais

- `track_id`, `artists`, `album_name`, `track_name`
- `popularity` (0–100)
- `duration_ms`, `explicit`
- Audio features: `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `time_signature`
- `track_genre`

## Observação

Para o visualizador HTML (`docs/index.html`) a base já foi processada; não é necessário baixar o CSV apenas para visualizar.
