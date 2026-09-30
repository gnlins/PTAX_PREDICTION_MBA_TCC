# Modelagem e Previsão da Taxa de Câmbio USD/BRL com Machine Learning

Projeto desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) do MBA em Data Science Analytics da Universidade de São Paulo (USP).

O objetivo do projeto é investigar a relação entre variáveis macroeconômicas e financeiras e a taxa de câmbio USD/BRL, avaliando a capacidade preditiva de diferentes técnicas de Machine Learning para a previsão da cotação do dólar.

---

## Objetivo

O projeto busca modelar e prever a taxa de câmbio USD/BRL para a próxima observação temporal:

\[
USD/BRL(t+1) = f(X_1(t), X_2(t), ..., X_n(t))
\]

A avaliação é realizada preservando a ordem temporal dos dados, evitando embaralhamento das observações e buscando evitar problemas de *data leakage* e *look-ahead bias*.

---

## Dados

Os dados possuem frequência diária e abrangem o período de maio de 2016 a maio de 2026.

As fontes utilizadas incluem:

- Banco Central do Brasil (BCB/SGS)
- Federal Reserve Economic Data (FRED)
- Yahoo Finance / `yfinance`

### Variáveis

O modelo principal utiliza nove variáveis explicativas:

- Selic
- IPCA
- PIB
- Exportações
- Importações
- FEDFUNDS
- IBOV
- SP500
- Petróleo

### Variável alvo

A variável dependente utilizada na modelagem é:

```text
USD_BRL_t1
```

que representa a cotação USD/BRL da próxima observação temporal.

---

## Tratamento dos dados

O processo de preparação dos dados inclui:

1. Conversão das datas para formato temporal;
2. Ordenação cronológica;
3. Definição da data como índice;
4. Remoção de observações sem USD/BRL;
5. Tratamento de valores ausentes;
6. Verificação de valores infinitos;
7. Análise exploratória dos dados;
8. Análise de correlação;
9. Análise de multicolinearidade por meio do VIF;
10. Teste de estacionariedade pelo ADF;
11. Preparação das variáveis para modelagem.

Os procedimentos são realizados de forma a preservar a estrutura temporal da série.

---

## Divisão entre treino e teste

A avaliação principal utiliza uma divisão temporal de:

- **80%:** treinamento;
- **20%:** teste.

Não é utilizado `shuffle`, de modo que as observações mais antigas permanecem no conjunto de treinamento e as observações mais recentes são utilizadas para avaliação.

A divisão é realizada utilizando a seguinte lógica:

```text
Dados históricos
       │
       ├─────────────── 80% ───────────────┐
       │                                   │
       │              TREINO               │
       │                                   │
       └───────────────────────────────────┤
                                           │
                         20%               │
                        TESTE              │
                                           │
                                           ▼
```

O conjunto de teste é mantido igual entre os modelos para permitir a comparação dos resultados.

---

## Modelos

São avaliados três modelos principais.

### 1. Regressão Linear Múltipla

Utilizada como modelo de referência linear.

Características:

- `LinearRegression`;
- `StandardScaler`;
- padronização ajustada somente no conjunto de treinamento;
- análise dos coeficientes;
- análise OLS;
- análise de resíduos.

### 2. Random Forest

Modelo baseado em árvores de decisão utilizado para avaliar relações não lineares.

Configuração inicial:

```python
RandomForestRegressor(
    n_estimators=500,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features=1.0,
    random_state=42,
    n_jobs=-1
)
```

Não é utilizada padronização para o Random Forest.

Além das métricas de previsão, é analisada a importância das variáveis.

### 3. LSTM

Modelo de redes neurais recorrentes destinado à modelagem de dependências temporais.

Configuração:

```text
Janela temporal: 30 observações

LSTM(64)
Dropout(0.2)
LSTM(32)
Dropout(0.2)
Dense(16)
Dense(1)
```

Configuração de treinamento:

```text
Otimizador: Adam
Loss: MSE
Epochs: 100
Batch size: 32
Early Stopping: patience = 10
restore_best_weights = True
shuffle = False
```

As variáveis de entrada e o target são padronizados utilizando `StandardScaler`, ajustados somente com os dados de treinamento.

---

## Baseline de persistência

Além dos modelos de Machine Learning, é utilizado um baseline ingênuo de persistência:

\[
\hat{y}(t+1) = USD/BRL(t)
\]

Ou seja, a previsão para a próxima observação é simplesmente igual ao último valor observado da taxa de câmbio.

Esse baseline serve como referência para avaliar se os modelos de Machine Learning apresentam capacidade preditiva adicional em relação a uma estratégia simples de persistência.

---

## Métricas

Os modelos são avaliados utilizando:

### MAE — Mean Absolute Error

Mede o erro absoluto médio entre os valores reais e previstos.

### RMSE — Root Mean Squared Error

Mede a raiz do erro quadrático médio, atribuindo maior peso a erros de maior magnitude.

### R² — Coeficiente de Determinação

Avalia a proporção da variabilidade da variável alvo explicada pelas previsões do modelo.

As métricas são calculadas principalmente no conjunto de teste para permitir a comparação entre os modelos.

---

## Estrutura do projeto

```text
MBA_TCC/
│
├── dados/
│   ├── bruto/
│   ├── tratado/
│   └── splits/
│
├── notebooks/
│
├── resultados/
│   ├── eda/
│   ├── correlacao/
│   ├── vif/
│   ├── adf/
│   ├── preparacao/
│   ├── regressao_linear/
│   ├── random_forest/
│   ├── lstm/
│   ├── baseline_naive/
│   ├── comparacao/
│   └── graficos/
│
├── tcc/
│
└── README.md
```

### `dados/`

Contém os dados utilizados no projeto.

```text
dados/
├── bruto/
├── tratado/
└── splits/
```

- `bruto/`: dados obtidos das fontes originais;
- `tratado/`: dados após o processo de tratamento e consolidação;
- `splits/`: conjuntos de treinamento e teste derivados da base definitiva.

### `notebooks/`

Contém os notebooks utilizados em cada etapa do projeto.

Exemplo:

```text
notebooks/
├── 01_EDA.ipynb
├── 02_Correlacao.ipynb
├── 03_VIF.ipynb
├── 04_ADF.ipynb
├── 05_Preparacao_Modelagem.ipynb
├── 06_Divisao_Treino_Teste.ipynb
├── 07_Regressao_Linear.ipynb
├── 08_Random_Forest.ipynb
├── 09_LSTM.ipynb
├── 10_Baseline_Naive.ipynb
├── 11_Comparacao_Modelos.ipynb
└── 12_Graficos_Resultados.ipynb
```

### `resultados/`

Armazena os resultados produzidos durante as análises e modelagens.

Cada modelo possui seu próprio diretório, contendo métricas, previsões, modelos treinados, diagnósticos e demais artefatos necessários.

### `tcc/`

Contém os materiais relacionados à elaboração do trabalho acadêmico, como textos, referências e figuras utilizadas no documento final.

---

## Fluxo do projeto

O desenvolvimento segue o seguinte fluxo:

```text
Coleta dos dados
       ↓
Tratamento e consolidação
       ↓
Análise exploratória
       ↓
Correlação / VIF / ADF
       ↓
Preparação para modelagem
       ↓
Divisão temporal 80/20
       ↓
┌──────────────┬──────────────┬──────────────┐
│  Regressão   │ Random       │    LSTM      │
│    Linear    │  Forest      │              │
└──────────────┴──────────────┴──────────────┘
       ↓
Baseline de persistência
       ↓
Avaliação das previsões
       ↓
Comparação dos modelos
       ↓
Geração dos gráficos
       ↓
Análise dos resultados
```

---

## Experimento adicional com USD/BRL(t)

Após a avaliação do modelo principal, é realizado um experimento adicional incluindo o valor contemporâneo da taxa de câmbio:

```text
USD/BRL(t)
```

como variável explicativa para prever:

```text
USD/BRL(t+1)
```

Nesse experimento, os demais aspectos da avaliação são mantidos, permitindo comparar a especificação principal com a especificação que incorpora o valor atual da própria taxa de câmbio.

---

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Statsmodels
- TensorFlow / Keras
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook

---

## Cuidados metodológicos

Durante o desenvolvimento são observados os seguintes cuidados:

- preservação da ordem temporal;
- ausência de *shuffle* na divisão principal;
- prevenção de *data leakage*;
- prevenção de *look-ahead bias*;
- ajuste dos scalers somente com dados de treinamento;
- utilização do mesmo período de teste para comparação dos modelos;
- separação entre dados de treinamento e avaliação;
- distinção entre análise exploratória e avaliação preditiva;
- interpretação das correlações como relações exploratórias, sem inferência automática de causalidade.

---

## Status do projeto

O projeto encontra-se em fase de desenvolvimento e consolidação dos experimentos computacionais.

Etapas principais:

- [x] Tratamento e consolidação dos dados
- [x] Análise exploratória
- [x] Análise de correlação
- [x] Análise de multicolinearidade
- [x] Teste ADF
- [x] Definição do target
- [x] Divisão temporal treino/teste
- [x] Regressão Linear
- [x] Random Forest
- [x] LSTM
- [x] Baseline de persistência
- [ ] Consolidação final das métricas
- [ ] Comparação final dos modelos
- [ ] Geração dos gráficos definitivos
- [ ] Redação dos resultados
- [ ] Discussão dos resultados
- [ ] Conclusão do TCC

---

## Autor

**Gustavo Lins**

MBA em Data Science Analytics — Universidade de São Paulo (USP)

Projeto desenvolvido para fins acadêmicos.
