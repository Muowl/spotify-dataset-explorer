# Verificação da manutenção de rastreabilidade

Data: **18/10/2026 UTC**. Base: `c310928b1dbea4f1ab0fcf44118ba70aea36f740`. Escopo: ambiente, entradas, limitações, redação e regra de apresentação de empates. Esta manutenção não define a pergunta nem a fonte central do TCC e não acrescenta um experimento.

## Executado

Os hashes foram recalculados sobre os CSVs preservados da auditoria, sem novo download ou edição dos dados:

| Entrada | SHA-256 |
|---|---|
| Spotify | `b202fa49909b2d5cef71a04b1d21243cfeb36414535f2ca9272aa646721177bd` |
| Emotify | `32229d7329e1245af3f9bd2e7005f51e1c8582ae1e48b9afa5cacb8cdcb65d71` |

Ambiente: Python **3.12.14**, pandas **2.2.3**, NumPy **2.3.5**, SciPy **1.17.0**, Matplotlib **3.10.8** e seaborn **0.13.2**. A amostra de dispersão mantém `random_state=42`.

As sete células de código do notebook foram executadas sequencialmente por `exec`, em processo Python novo, com `MPLBACKEND=Agg` e `OPENBLAS_NUM_THREADS=2`. A execução usou uma cópia separada do repositório e os CSVs verificados. Não foi uma execução por kernel Jupyter; expressões finais e figuras inline não foram tratadas como outputs ricos de notebook. As saídas antigas das células modificadas foram limpas no arquivo versionado para evitar exibir resultados anteriores como se fossem os novos.

As verificações dirigidas confirmaram:

- 89.741 IDs no recorte global e 113.550 pares ID–gênero; mesmos 157 IDs com tempo zero, 162 com time_signature zero e um registro sem título.
- Figura 1: corte de 996, 21 gêneros, incluindo os quatro empatados (`comedy`, `drum-and-bass`, `power-pop`, `psych-rock`).
- Figura 5: corte de 51, 13 gêneros, incluindo os três empatados (`deep-house`, `emo`, `psych-rock`).
- Amostra de 8.000 IDs idêntica à obtida pela regra anterior com semente 42; matriz de correlação igual à da auditoria, com tolerância absoluta de `1e-12`.
- `build_global_hits.py` e `build_emotify.py` concluíram e reproduziram, byte a byte, os dois JavaScripts versionados. As medianas e contagens desses derivados permaneceram iguais.
- Uma entrada temporária com bytes alterados foi rejeitada tanto pela célula de carregamento Spotify quanto pelo script Emotify. No teste Emotify, o arquivo de saída sentinela permaneceu intacto.
- Os dois gráficos modificados foram inspecionados visualmente para conferir rótulos, empates e ausência de cortes no conteúdo.

Os valores e stdout dessa execução estão em [maintenance-verification.json](maintenance-verification.json). O JSON registra os hashes e versões efetivamente observados; não é uma estimativa.

## Diff das figuras

| Arquivo | Alteração em relação a `c310928` |
|---|---|
| `docs/assets/fig1.png` | 20 → 21 gêneros; acrescenta `psych-rock` (996 IDs); título “com empates”; substitui “faixas” por “IDs”; contagens crescentes de cima para baixo e ordem alfabética nos empates; altura ajustada para 6,5 polegadas. |
| `docs/assets/fig5.png` | 12 → 13 gêneros; acrescenta `emo` (mediana 51); título “com empates”; ordem alfabética dentro de cada empate. |
| `docs/assets/fig2.png`, `fig3.png`, `fig4.jpg` | Sem alteração nos arquivos versionados. |
| `docs/assets/hits-data.js`, `emotify-data.js` | Sem alteração nos arquivos versionados. |

As figuras 1 e 5 foram renderizadas com Matplotlib 3.10.8. Também existem diferenças de renderização em relação aos PNGs anteriores; não se afirma identidade de pixels. A mudança inclui quais gêneros são mostrados, mas não altera os valores calculados para os gêneros existentes.

## Limites e ações não executadas

Não foram removidos registros adicionais, criadas classes de equivalência ou partições, treinados recomendadores, adicionadas páginas ou alterado o deploy. Nenhuma alteração foi aplicada à `main`. Não foi criada uma tag.

Uma tag poderá identificar a versão depois da revisão. A definição de um protocolo para o TCC permanece uma etapa futura, dependente da pergunta e da fonte escolhidas; esta manutenção não a substitui.
