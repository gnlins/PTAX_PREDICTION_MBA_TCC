# Regressão Linear — Experimento com USD/BRL(t)

## Configuração

- Experimento: Experimento com USD/BRL(t)
- Base: `C:\Projetos\PTAX_PREDICTION_MBA_TCC\dados\tratado\consolidado_sem_nulos_final_usdt1.csv`
- Variáveis explicativas: 10
- Variáveis: Selic, IPCA, PIB, Exportacoes, Importacoes, FEDFUNDS, IBOV, SP500, Petroleo, USD/BRL
- Target: `USD_BRL_t1`
- Divisão temporal: 80% treino / 20% teste
- Padronização: StandardScaler ajustado somente no treino

## Períodos

- Treino: 2016-05-02 a 2024-04-24
- Teste: 2024-04-25 a 2026-04-29

## Métricas

| Modelo                    | Conjunto   |       MAE |      RMSE |       R2 |
|:--------------------------|:-----------|----------:|----------:|---------:|
| Regressao Linear Baseline | Treino     | 0.0340866 | 0.0481291 | 0.996951 |
| Regressao Linear Baseline | Teste      | 0.0351456 | 0.0470562 | 0.969079 |

## Coeficientes

| Variavel    |   Coeficiente |
|:------------|--------------:|
| Selic       |   -0.0105332  |
| IPCA        |   -0.00172136 |
| PIB         |    0.0335564  |
| Exportacoes |   -0.00805097 |
| Importacoes |    0.00276025 |
| FEDFUNDS    |   -0.00633385 |
| IBOV        |   -0.00975607 |
| SP500       |   -0.00240769 |
| Petroleo    |   -0.00206121 |
| USD/BRL     |    0.857781   |

## Baseline Naive

Previsão: y(t+1) = USD/BRL(t)

| Modelo         | Conjunto   |       MAE |      RMSE |       R2 |
|:---------------|:-----------|----------:|----------:|---------:|
| Baseline Naive | Teste      | 0.0339086 | 0.0464168 | 0.969913 |

## Comparação

| Modelo                    | Conjunto   |       MAE |      RMSE |       R2 |
|:--------------------------|:-----------|----------:|----------:|---------:|
| Regressao Linear Baseline | Teste      | 0.0351456 | 0.0470562 | 0.969079 |
| Baseline Naive            | Teste      | 0.0339086 | 0.0464168 | 0.969913 |

## Arquivos gerados

- `metricas_regressao_linear.csv`
- `previsoes_treino.csv`
- `previsoes_teste.csv`
- `regressao_linear.joblib`
- `standard_scaler.joblib`
- `coeficientes.csv`
- `ols_summary.txt`
- `metricas_baseline_naive.csv`
- `previsoes_baseline_naive.csv`
- `comparacao_modelos.csv`
- `residuos_treino.csv`
- `residuos_teste.csv`
- `residuos_treino.png`
- `residuos_teste.png`
- `real_vs_previsto_teste.png`