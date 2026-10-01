# LSTM

## Configuração experimental

- Configuração: Modelo principal
- Target: `USD_BRL_t1`
- Janela temporal: 30 observações
- Divisão temporal: 80% treino / 20% teste
- Padronização: StandardScaler para X e y
- Scalers ajustados somente no treino
- Epochs máximas: 100
- Batch size: 32
- EarlyStopping: patience=10
- restore_best_weights=True
- shuffle=False
- Otimizador: Adam
- Loss: MSE

## Arquitetura

- LSTM(64)
- Dropout(0.2)
- LSTM(32)
- Dropout(0.2)
- Dense(16)
- Dense(1)

## Períodos

- Treino: 2016-05-02 a 2024-04-24
- Teste: 2024-04-25 a 2026-04-29

## Métricas

| Modelo   | Conjunto   |      MAE |     RMSE |        R2 |
|:---------|:-----------|---------:|---------:|----------:|
| LSTM     | Treino     | 0.320671 | 0.431562 |  0.754564 |
| LSTM     | Teste      | 0.460899 | 0.530491 | -2.92988  |

## Observação sobre as sequências

A primeira sequência de teste foi construída com as últimas 29 observações de treino e a primeira observação de teste. A observação de teste é utilizada como informação disponível em t para prever o target USD/BRL(t+1), evitando o uso de informação futura.
