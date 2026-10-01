# Regressão Linear — Modelo principal

## Configuração

- Experimento: Modelo principal
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

| Modelo                    | Conjunto   |      MAE |     RMSE |         R2 |
|:--------------------------|:-----------|---------:|---------:|-----------:|
| Regressao Linear Baseline | Treino     | 0.238    | 0.303326 |   0.878892 |
| Regressao Linear Baseline | Teste      | 0.926661 | 1.04718  | -14.3132   |

## Coeficientes

| Variavel    |   Coeficiente |
|:------------|--------------:|
| Selic       |    -0.310769  |
| IPCA        |    -0.0566009 |
| PIB         |     1.32443   |
| Exportacoes |    -0.24737   |
| Importacoes |     0.0863685 |
| FEDFUNDS    |    -0.409211  |
| IBOV        |    -0.179294  |
| SP500       |     0.105496  |
| Petroleo    |    -0.179222  |

## Baseline Naive

Previsão: y(t+1) = USD/BRL(t)

| Modelo         | Conjunto   |       MAE |      RMSE |       R2 |
|:---------------|:-----------|----------:|----------:|---------:|
| Baseline Naive | Teste      | 0.0339086 | 0.0464168 | 0.969913 |

## Comparação

| Modelo                    | Conjunto   |       MAE |      RMSE |         R2 |
|:--------------------------|:-----------|----------:|----------:|-----------:|
| Regressao Linear Baseline | Teste      | 0.926661  | 1.04718   | -14.3132   |
| Baseline Naive            | Teste      | 0.0339086 | 0.0464168 |   0.969913 |

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