# spotify-dataset-explorer

Repo simples para estudar e visualizar a base [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset).

Usado no TCC de Sistemas de Informação (UFJF) só como apoio para entender a base (gêneros, audio features, popularity etc.).

## Visualizar

O arquivo principal é o HTML em `docs/index.html`. A navegação também leva a `docs/hits-mundiais.html`, com um estudo exploratório de hits e faixas de nicho, e a `docs/emotify.html`, com uma análise de anotações de emoções evocadas pela música coletadas no Emotify.

Depois de ativar o GitHub Pages (Settings > Pages > branch `main`, pasta `/docs`), o link fica:

https://muowl.github.io/spotify-dataset-explorer/

Não precisa instalar nada nem rodar código.

A página `docs/horarios-de-escuta.html` reúne literatura sobre horários de escuta e limitações das evidências. É uma síntese bibliográfica, não uma análise temporal do CSV de faixas.

## Estrutura

- `docs/index.html` - visualização estática com os gráficos
- `docs/hits-mundiais.html` - 30 vídeos em três seleções (global, metal e clássica), com visualizações e atributos do CSV
- `docs/horarios-de-escuta.html` - estudos sobre padrões temporais de escuta e limites de interpretação
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

Para reproduzir a comparação de músicas populares, baixe o CSV em `data/dataset.csv` e execute `python scripts/build_global_hits.py`. O script usa a biblioteca padrão do Python, confere o SHA-256 do CSV e os metadados dos IDs selecionados. As visualizações e evidências estão congeladas em `data/youtube-selection.json`; executar o script não atualiza o YouTube.

São dez vídeos por grupo: candidatos globais da lista do Kworb, metal e subgêneros a partir de uma matéria da Chaoszine e repertório clássico selecionado a partir das gravações do CSV. Não são três rankings universais. São 25 associações documentais usadas na comparação, três versões incertas excluídas dos cálculos e duas músicas sem registro localizado. Os detalhes de seleção e os limites estão em [research/youtube-method.md](research/youtube-method.md).

Links:
- [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- [Hugging Face](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)


## Ambiente de reprodução

Os cálculos da auditoria de 17/10/2026 (UTC) foram verificados com **Python 3.12.14**, pandas 2.2.3, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8 e seaborn 0.13.2. As dependências diretas estão em `requirements.txt`; `.python-version` registra a versão do Python. Não se trata de um lockfile das dependências transitivas.

```bash
python --version  # usar Python 3.12.14
python -m venv .venv
# Linux/macOS; no Windows, use .venv\Scripts\activate
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Para executar o notebook, selecione esse ambiente na sua ferramenta de notebooks e use `notebooks/` como diretório de trabalho. A interface Jupyter/VS Code não faz parte das dependências de cálculo fixadas acima. Os scripts em `scripts/` usam somente a biblioteca padrão e são executados a partir da raiz do repositório.

As figuras publicadas no commit `c310928` foram geradas com **Matplotlib 3.11.2**, conforme os metadados dos PNGs. O ambiente original completo não está registrado. O ambiente acima reproduziu os cálculos auditados, mas **não reproduziu as figuras de forma idêntica em bytes ou pixels**; fontes, dimensões e ordenação de empates podem diferir.
