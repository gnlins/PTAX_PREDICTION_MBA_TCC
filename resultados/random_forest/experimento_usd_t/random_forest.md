# Random Forest — Experimento com USD/BRL(t)

## Configuração experimental

- Experimento: Experimento com USD/BRL(t)
- Base: `C:\Projetos\PTAX_PREDICTION_MBA_TCC\dados\tratado\consolidado_sem_nulos_final_usdt1.csv`
- Variáveis explicativas: 10
- Variáveis: Selic, IPCA, PIB, Exportacoes, Importacoes, FEDFUNDS, IBOV, SP500, Petroleo, USD/BRL
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

| Modelo        | Conjunto   |       MAE |      RMSE |       R2 |
|:--------------|:-----------|----------:|----------:|---------:|
| Random Forest | Treino     | 0.0135273 | 0.0188912 | 0.99953  |
| Random Forest | Teste      | 0.0869511 | 0.137606  | 0.735577 |

## Importância das variáveis

| Variavel    |   Importancia |
|:------------|--------------:|
| USD/BRL     |   0.997617    |
| IBOV        |   0.00055238  |
| SP500       |   0.000487694 |
| Petroleo    |   0.000472557 |
| Exportacoes |   0.000185121 |
| IPCA        |   0.000164787 |
| PIB         |   0.000158093 |
| Importacoes |   0.000144075 |
| Selic       |   0.000109798 |
| FEDFUNDS    |   0.000108305 |

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