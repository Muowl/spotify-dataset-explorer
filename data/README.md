# Dados

A base **não** está versionada neste repositório (arquivo ~20 MB).

## Como obter

1. **Kaggle:** https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset  
2. **Hugging Face:** https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset  

Arquivo principal: `data/dataset.csv`. Para reproduzir a versão auditada, use o [CSV fixado na revisão `635b034f69257814eff850a5c2b3346fe458134f` do Hugging Face](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/resolve/635b034f69257814eff850a5c2b3346fe458134f/dataset.csv).

SHA-256 esperado: `b202fa49909b2d5cef71a04b1d21243cfeb36414535f2ca9272aa646721177bd`. O notebook e o script dos hits rejeitam arquivos diferentes. A cópia foi obtida em 17/10/2026 UTC e seu hash foi recalculado em 18/10/2026 UTC. Os links gerais Kaggle/Hugging Face podem apontar para versões diferentes no futuro.

Após baixar, execute `python scripts/build_global_hits.py` a partir da raiz do repositório para recriar `docs/assets/hits-data.js`. O CSV é ignorado pelo Git; o arquivo JavaScript gerado é versionado para o GitHub Pages funcionar sem processamento no servidor.

## Colunas principais

- `track_id`, `artists`, `album_name`, `track_name`
- `popularity` (0–100)
- `duration_ms`, `explicit`
- Audio features: `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `time_signature`
- `track_genre`

## Observação

Para o visualizador HTML (`docs/index.html`) a base já foi processada; não é necessário baixar o CSV apenas para visualizar.

## Entrada Emotify

Fonte: [CSV oficial da Universidade de Utrecht](https://www2.projects.science.uu.nl/memotion/emotifydata/data.csv), salvo em `data/emotify.csv`. Essa URL não é versionada. Observação/download: **17/10/2026 UTC**; hash da cópia reconferido em **18/10/2026 UTC**.

SHA-256 observado: `32229d7329e1245af3f9bd2e7005f51e1c8582ae1e48b9afa5cacb8cdcb65d71`. `scripts/build_emotify.py` registra a origem e a data e valida o hash antes de gerar `docs/assets/emotify-data.js`. Se a fonte mudar, é necessário conferir a nova entrada antes de atualizar o hash esperado.

Mantenha os CSVs brutos sem edição. Os scripts escrevem os derivados em `docs/assets/`, sem modificar as entradas. Spotify e Emotify são fontes distintas e não são unidos: não há chave de correspondência documentada entre seus registros.
