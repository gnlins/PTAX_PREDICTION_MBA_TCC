# Random Forest — Modelo principal

## Configuração experimental

- Experimento: Modelo principal
- Base: `C:\Projetos\PTAX_PREDICTION_MBA_TCC\dados\tratado\consolidado_sem_nulos_final_usdt1.csv`
- Variáveis explicativas: 9
- Variáveis: Selic, IPCA, PIB, Exportacoes, Importacoes, FEDFUNDS, IBOV, SP500, Petroleo
- Target: `USD_BRL_t1`
- Divisão temporal: 80% treino / 20% teste
- StandardScaler: não utilizado

## Períodos

- Treino: 2016-05-02 a 2024-04-24
- Teste: 2024-04-25 a 2026-04-29

## Hiperparâmetros

| Parametro         | Valor   |
|:------------------|:--------|
| n_estimators      | 500     |
| max_depth         | None    |
| min_samples_split | 2       |
| min_samples_leaf  | 1       |
| max_features      | 1.0     |
| random_state      | 42      |
| n_jobs            | -1      |

## Métricas

| Modelo        | Conjunto   |       MAE |      RMSE |        R2 |
|:--------------|:-----------|----------:|----------:|----------:|
| Random Forest | Treino     | 0.0137834 | 0.0200231 |  0.999472 |
| Random Forest | Teste      | 0.712646  | 0.773474  | -7.35437  |

## Importância das variáveis

| Variavel    |   Importancia |
|:------------|--------------:|
| SP500       |    0.681264   |
| Selic       |    0.118321   |
| FEDFUNDS    |    0.0979972  |
| PIB         |    0.0702896  |
| Petroleo    |    0.0129856  |
| Exportacoes |    0.00754117 |
| IBOV        |    0.0058937  |
| Importacoes |    0.00349994 |
| IPCA        |    0.00220821 |

## Arquivos gerados

- `metricas_random_forest.csv`
- `previsoes_treino.csv`
- `previsoes_teste.csv`
- `residuos_treino.csv`
- `residuos_teste.csv`
- `grafico_residuos_treino.png`
- `grafico_residuos_teste.png`
- `grafico_real_vs_previsto.png`
- `feature_importance.csv`
- `feature_importance.png`
- `random_forest.joblib`
- `random_forest.md`