import os
import numpy as np
import pandas as pd


def dividir_treino_teste_tcc(
    caminho_csv,
    incluir_usd_t=False,
    proporcao_treino=0.80):
    
    """
    Divide a base em treino e teste utilizando divisão temporal.

    A coluna 0 do CSV é carregada diretamente como índice e
    convertida para DatetimeIndex.

    Parâmetros
    ----------
    caminho_csv : str
        Caminho para a base CSV.

    incluir_usd_t : bool, default=False
        Define se USD/BRL(t) será utilizada como variável explicativa.

        False:
            Utiliza somente as 9 variáveis macroeconômicas/financeiras.

        True:
            Adiciona USD/BRL(t) às variáveis explicativas.

    proporcao_treino : float, default=0.80
        Proporção da base utilizada para treinamento.

    Retorna
    -------
    X_train : pd.DataFrame
        Variáveis explicativas do conjunto de treino.

    y_train : pd.Series
        Target do conjunto de treino.

    X_test : pd.DataFrame
        Variáveis explicativas do conjunto de teste.

    y_test : pd.Series
        Target do conjunto de teste.
    """

    # ============================================================
    # 1. CONFIGURAÇÃO DAS VARIÁVEIS
    # ============================================================

    variaveis_base = [
        "Selic",
        "IPCA",
        "PIB",
        "Exportacoes",
        "Importacoes",
        "FEDFUNDS",
        "IBOV",
        "SP500",
        "Petroleo"
    ]

    target = "USD_BRL_t1"

    # ============================================================
    # 2. VALIDAÇÕES INICIAIS
    # ============================================================

    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(
            f"Arquivo não encontrado:\n{caminho_csv}"
        )

    if not 0 < proporcao_treino < 1:
        raise ValueError(
            "proporcao_treino deve estar entre 0 e 1."
        )

    # ============================================================
    # 3. CARREGAR BASE
    # ============================================================

    # A coluna 0 é carregada diretamente como índice
    df = pd.read_csv(
        caminho_csv,
        index_col=0
    )

    print("[OK] Base carregada.")
    print(f"[INFO] Dimensões iniciais: {df.shape}")

    # ============================================================
    # 4. CONVERTER ÍNDICE PARA DATETIME
    # ============================================================

    df.index = pd.to_datetime(
        df.index,
        errors="coerce"
    )

    if df.index.isna().any():

        quantidade = df.index.isna().sum()

        raise ValueError(
            f"Foram encontradas {quantidade} datas inválidas no índice."
        )

    if not isinstance(df.index, pd.DatetimeIndex):

        raise TypeError(
            "O índice da base não pôde ser convertido para "
            "DatetimeIndex."
        )

    # ============================================================
    # 5. ORDENAR CRONOLOGICAMENTE
    # ============================================================

    df = df.sort_index()

    print("[OK] Índice convertido para DatetimeIndex.")
    print("[OK] Base ordenada cronologicamente.")

    # ============================================================
    # 6. DEFINIR VARIÁVEIS EXPLICATIVAS
    # ============================================================

    variaveis_explicativas = variaveis_base.copy()

    if incluir_usd_t:

        if "USD/BRL" not in df.columns:
            raise KeyError(
                "A coluna 'USD/BRL' não foi encontrada na base."
            )

        variaveis_explicativas.append("USD/BRL")

    # ============================================================
    # 7. VALIDAR COLUNAS
    # ============================================================

    colunas_necessarias = (
        variaveis_explicativas +
        [target]
    )

    colunas_faltantes = [
        coluna
        for coluna in colunas_necessarias
        if coluna not in df.columns
    ]

    if colunas_faltantes:

        raise KeyError(
            "As seguintes colunas não foram encontradas na base: "
            f"{colunas_faltantes}"
        )

    # ============================================================
    # 8. SELECIONAR APENAS AS COLUNAS NECESSÁRIAS
    # ============================================================

    df_modelagem = df[
        variaveis_explicativas + [target]
    ].copy()

    # ============================================================
    # 9. VERIFICAR VALORES AUSENTES
    # ============================================================

    colunas_modelagem = (
        variaveis_explicativas + [target]
    )

    if df_modelagem[colunas_modelagem].isna().any().any():

        nulos = (
            df_modelagem[colunas_modelagem]
            .isna()
            .sum()
        )

        nulos = nulos[nulos > 0]

        raise ValueError(
            "Existem valores nulos nas variáveis utilizadas "
            "na modelagem:\n"
            f"{nulos}"
        )

    print("[OK] Não existem valores nulos.")

    # ============================================================
    # 10. VERIFICAR VALORES INFINITOS
    # ============================================================

    valores_numericos = df_modelagem[
        colunas_modelagem
    ]

    if np.isinf(
        valores_numericos.to_numpy(dtype=float)
    ).any():

        raise ValueError(
            "Foram encontrados valores infinitos na base."
        )

    print("[OK] Não existem valores infinitos.")

    # ============================================================
    # 11. DEFINIR TAMANHO DO TREINO
    # ============================================================

    n_observacoes = len(df_modelagem)

    n_treino = int(
        n_observacoes * proporcao_treino
    )

    if n_treino <= 0 or n_treino >= n_observacoes:

        raise ValueError(
            "A proporção de treino resultou em um "
            "conjunto de treino ou teste vazio."
        )

    # ============================================================
    # 12. DIVISÃO TEMPORAL
    # ============================================================

    df_train = df_modelagem.iloc[
        :n_treino
    ].copy()

    df_test = df_modelagem.iloc[
        n_treino:
    ].copy()

    # ============================================================
    # 13. CRIAR X E y
    # ============================================================

    X_train = df_train[
        variaveis_explicativas
    ].copy()

    y_train = df_train[
        target
    ].copy()

    X_test = df_test[
        variaveis_explicativas
    ].copy()

    y_test = df_test[
        target
    ].copy()

    # ============================================================
    # 14. VALIDAÇÕES DA DIVISÃO
    # ============================================================

    if not isinstance(X_train.index, pd.DatetimeIndex):
        raise TypeError(
            "O índice de X_train não é um DatetimeIndex."
        )

    if not isinstance(X_test.index, pd.DatetimeIndex):
        raise TypeError(
            "O índice de X_test não é um DatetimeIndex."
        )

    if not X_train.index.is_monotonic_increasing:
        raise ValueError(
            "X_train não está em ordem cronológica."
        )

    if not X_test.index.is_monotonic_increasing:
        raise ValueError(
            "X_test não está em ordem cronológica."
        )

    if X_train.index.max() >= X_test.index.min():
        raise ValueError(
            "Existe sobreposição temporal entre treino e teste."
        )

    if len(X_train) + len(X_test) != n_observacoes:
        raise ValueError(
            "A quantidade de observações após a divisão "
            "não corresponde à base original."
        )

    # ============================================================
    # 15. INFORMAÇÕES DA DIVISÃO
    # ============================================================

    modelo = (
        "Experimento com USD/BRL(t)"
        if incluir_usd_t
        else "Modelo principal"
    )

    print("\n" + "=" * 60)
    print("DIVISÃO TREINO / TESTE")
    print("=" * 60)

    print(f"[INFO] Configuração: {modelo}")

    print(
        f"[INFO] Variáveis explicativas: "
        f"{len(variaveis_explicativas)}"
    )

    print(
        f"[INFO] Variáveis: "
        f"{variaveis_explicativas}"
    )

    print(
        f"[INFO] Observações totais: "
        f"{n_observacoes}"
    )

    print(
        f"[INFO] Treino: "
        f"{len(X_train)} "
        f"({len(X_train) / n_observacoes:.1%})"
    )

    print(
        f"[INFO] Teste: "
        f"{len(X_test)} "
        f"({len(X_test) / n_observacoes:.1%})"
    )

    print(
        f"[INFO] Período treino: "
        f"{X_train.index.min().date()} "
        f"a "
        f"{X_train.index.max().date()}"
    )

    print(
        f"[INFO] Período teste: "
        f"{X_test.index.min().date()} "
        f"a "
        f"{X_test.index.max().date()}"
    )

    print("[OK] Ordem temporal preservada.")
    print("[OK] Sem sobreposição temporal.")
    print(f"[OK] Target: {target}")

    print("=" * 60)

    return X_train, y_train, X_test, y_test