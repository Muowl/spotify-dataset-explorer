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

## Limitações conhecidas do Spotify Tracks Dataset

Estas observações se referem ao CSV com o SHA-256 acima, auditado em 17/10/2026 UTC. Não motivam exclusões adicionais de registros nesta exploração.

- **Unidade:** 89.741 são IDs únicos (`track_id`) após manter a primeira ocorrência de cada ID, não gravações únicas comprovadas. Uma gravação pode ter mais de um ID de catálogo.
- **Coincidências entre IDs distintos:** 9.305 dos 89.741 IDs (10,37%) têm pelo menos outro ID com os nove atributos contínuos idênticos: `danceability`, `energy`, `loudness`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence` e `tempo`. Já 10.000 IDs (11,14%) repetem a combinação literal de título, artistas e duração (`track_name`, `artists`, `duration_ms`). As porcentagens contam todos os IDs participantes dos grupos, não apenas as linhas excedentes; os conjuntos podem se sobrepor e não devem ser somados. Esse diagnóstico não verificou identidade acústica nem demonstrou vazamento ou inflação de métricas em um experimento.
- **Seleção:** há 1.000 linhas por gênero, mas o critério de seleção dessas linhas não está documentado no dataset card consultado. Isso não comprova amostragem aleatória ou representatividade do catálogo e dos ouvintes.
- **Número de gêneros:** o [card do Hugging Face](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/blob/635b034f69257814eff850a5c2b3346fe458134f/README.md) cita 125 gêneros; o CSV contém 114.
- **Condições de uso:** a tag `bsd` é uma declaração do autor do dataset. As condições aplicáveis ao conteúdo de origem Spotify não foram esclarecidas; a tag, sozinha, não comprova autorização para todo uso possível. Consulte também a [política do Spotify](https://developer.spotify.com/policy) antes de definir um novo uso dos dados.
- **Limite temporal e individual:** o CSV não contém eventos de escuta com usuário e timestamp. `popularity` é um score histórico agregado, não feedback individual. A base, isoladamente, não permite avaliar como a escolha de uma pessoa muda com o dia ou contexto.

A política existente de manter a primeira ocorrência por ID no recorte global e por par `(track_id, track_genre)` no recorte por gênero foi preservada. As coincidências entre IDs, os valores zero e o registro com metadados ausentes permanecem nos dados analisados.
