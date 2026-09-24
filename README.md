# spotify-dataset-explorer

Repo simples para estudar e visualizar a base [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset).

Usado no TCC de Sistemas de Informação (UFJF) só como apoio para entender a base (gêneros, audio features, popularity etc.).

## Visualizar

O arquivo principal é o HTML em `docs/index.html`. A navegação também leva a `docs/hits-mundiais.html`, com um estudo exploratório de cinco hits mundiais e quatro faixas populares em gêneros específicos.

Depois de ativar o GitHub Pages (Settings > Pages > branch `main`, pasta `/docs`), o link fica:

https://muowl.github.io/spotify-dataset-explorer/

Não precisa instalar nada nem rodar código.

## Estrutura

- `docs/index.html` - visualização estática com os gráficos
- `docs/hits-mundiais.html` - análise de cinco hits, quatro faixas de nicho e comparação com a base
- `docs/assets/hits-data.js` - dados processados da página de hits
- `scripts/build_global_hits.py` - reproduz os números da página de hits
- `notebooks/01_eda_spotify_tracks.ipynb` - notebook com o código da exploração
- `data/README.md` - de onde veio a base e quais são as colunas

## Dados

A base não está versionada aqui (CSV de ~20 MB).

Para atualizar a análise, baixe o CSV em `data/dataset.csv` e execute `python scripts/build_global_hits.py` na raiz do projeto. O script usa apenas a biblioteca padrão do Python. A seleção dos hits segue os cinco clipes musicais mais vistos na [lista retrospectiva do YouTube de 2022](https://blog.youtube/creator-and-artist-stories/10-years-of-youtubes-billion-views-club-psy-gangnam-style/); cada clipe é associado a um `track_id` específico no CSV. As quatro faixas de nicho têm os maiores scores `popularity` em seus respectivos rótulos (`heavy-metal`, `bluegrass`, `classical` e `drum-and-bass`), com desempate por ID fixado no script. Os grupos usam critérios de seleção diferentes; os dados de áudio são descritivos e não demonstram o motivo do sucesso.

Links:
- [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- [Hugging Face](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)
