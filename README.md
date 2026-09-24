# spotify-dataset-explorer

Repo simples para estudar e visualizar a base [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset).

Usado no TCC de Sistemas de Informação (UFJF) só como apoio para entender a base (gêneros, audio features, popularity etc.).

## Visualizar

O arquivo principal é o HTML em `docs/index.html`. A navegação também leva a `docs/hits-mundiais.html`, com um estudo exploratório de hits e faixas de nicho, e a `docs/emotify.html`, com uma análise de anotações de emoções evocadas pela música coletadas no Emotify.

Depois de ativar o GitHub Pages (Settings > Pages > branch `main`, pasta `/docs`), o link fica:

https://muowl.github.io/spotify-dataset-explorer/

Não precisa instalar nada nem rodar código.

## Estrutura

- `docs/index.html` - visualização estática com os gráficos
- `docs/hits-mundiais.html` - análise de cinco hits, cinco faixas de nicho e comparação com a base
- `docs/emotify.html` - introdução à GEMS e exploração das anotações do Emotify
- `docs/assets/emotify-data.js` - contagens reproduzíveis exibidas na página de música e emoção
- `scripts/build_emotify.py` - processa o CSV oficial do Emotify sem dependências externas
- `docs/assets/hits-data.js` - dados processados da página de hits
- `scripts/build_global_hits.py` - reproduz os números da página de hits
- `notebooks/01_eda_spotify_tracks.ipynb` - notebook com o código da exploração
- `data/README.md` - de onde veio a base e quais são as colunas

## Dados

A base não está versionada aqui (CSV de ~20 MB).

O CSV do Emotify também não é versionado. Para atualizar sua página, baixe as anotações na [página oficial](https://www2.projects.science.uu.nl/memotion/emotifydata/) em `data/emotify.csv` e execute `python scripts/build_emotify.py`. Não confunda os dois conjuntos: o Spotify Tracks Dataset descreve faixas; o Emotify registra avaliações feitas por ouvintes e não contém IDs de faixas do Spotify para união direta.

Para atualizar a análise, baixe o CSV em `data/dataset.csv` e execute `python scripts/build_global_hits.py` na raiz do projeto. O script usa apenas a biblioteca padrão do Python. A seleção dos hits segue os cinco clipes musicais mais vistos na [lista retrospectiva do YouTube de 2022](https://blog.youtube/creator-and-artist-stories/10-years-of-youtubes-billion-views-club-psy-gangnam-style/); cada clipe é associado a um `track_id` específico no CSV. As cinco faixas de nicho têm os maiores scores `popularity` em seus respectivos rótulos (`heavy-metal`, `bluegrass`, `classical`, `drum-and-bass` e `tango`), com desempate por ID fixado no script. Os grupos usam critérios de seleção diferentes; os dados de áudio são descritivos e não demonstram o motivo do sucesso.

Links:
- [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- [Hugging Face](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)
