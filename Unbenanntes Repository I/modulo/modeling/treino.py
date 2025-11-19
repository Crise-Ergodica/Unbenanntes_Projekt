import pandas as pd
from pycaret.classification import *
from pycaret.regression import *


def treino(caminhoCSV, target, nome, task='regression', algoritmo='gbr', iterações=20, seed=42):

    """
    Treina modelo automatizado com PyCaret (regressão ou classificação)
    .

    Args:
        caminhoCSV (str): Caminho para o arquivo CSV
        target (str): Nome da coluna target
        nome (str): Nome do modelo a ser salvo
        task (str): 'regression' ou 'classification' (padrão: 'regression')
        algoritmo (str): Nome do algoritmo, ex: 'gbr', 'xgboost', 'lr' (padrão: 'gbr')
        iterações (int): Número de iterações no tuning (padrão: 20)
        seed (int): Seed para reprodutibilidade (padrão: 42)

    Returns:
        model: Modelo treinado e finalizado

    Raises:
        ValueError: Se task não for 'regression' ou 'classification'
        FileNotFoundError: Se arquivo CSV não existir
    """

    # Valida task
    if task not in ['regression', 'classification']:
        raise ValueError(f"task deve ser 'regression' ou 'classification', '{task}' não é uma opção.")

    # Carrega dados
    try:
        dataNome = pd.read_csv(caminhoCSV)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{caminhoCSV}' não encontrado")

    setup(data=dataNome, target=target, seed=seed, verbose=False)

    # Cria modelo base
    modelo = create_model(algoritmo)

    # Otimiza modelo
    tuned = tune_model(modelo, n_iter=iterações)

    # Finaliza (treina em tudo)
    final = finalize_model(tuned)

    # Salva modelo
    save_model(final, nome)

    print(f"✅ Modelo '{nome}' treinado e salvo com sucesso!")

    return final
