"""
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           ████████╗██████╗░███████╗██╗███╗░░██╗░█████╗░                              │
│                                           ╚══██╔══╝██╔══██╗██╔════╝██║████╗░██║██╔══██╗                              │
│                                           ░░░██║░░░██████╔╝█████╗░░██║██╔██╗██║██║░░██║                              │
│                                           ░░░██║░░░██╔══██╗██╔══╝░░██║██║╚████║██║░░██║                              │
│                                           ░░░██║░░░██║░░██║███████╗██║██║░╚███║╚█████╔╝                              │
│                                           ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝░╚════╝░                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                          „ʇǝʇɥɔᴉɹǝƃ ɹᴉʍ ǝᴉʍ ʇʇo⅁ ʇǝʇɥɔᴉɹ ʇlǝzuǝuɹǝʇS ɯɹǝq∩„
"""

import pandas as pd

"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────        
         
                                                    ╭━━━━╮
                                                    ┃╭╮╭╮┃
                                                    ╰╯┃┃┣┻┳━━┳┳━╮╭━━╮
                                                    ╱╱┃┃┃╭┫┃━╋┫╭╮┫╭╮┃
                                                    ╱╱┃┃┃┃┃┃━┫┃┃┃┃╰╯┃
                                                    ╱╱╰╯╰╯╰━━┻┻╯╰┻━━╯

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""

def treino(caminho_csv, target, nome, task='regression', algoritmo='gbr', iterações=20, numero_seed=42):
    """
    Treina modelo automatizado com PyCaret (regressão ou classificação).

    Args:
        caminho_csv (str ou pd.DataFrame): Caminho para o arquivo CSV ou DataFrame
        target (str): Nome da coluna target
        nome (str): Nome do modelo a ser salvo
        task (str): 'regression' ou 'classification' (padrão: 'regression')
        algoritmo (str): Nome do algoritmo, ex: 'gbr', 'xgboost', 'lr' (padrão: 'gbr')
        iterações (int): Número de iterações no tuning (padrão: 20)
        numero_seed (int): Seed para reprodutibilidade (padrão: 42)

    Returns:
        model: Modelo treinado e finalizado

    Raises:
        ValueError: Se task não for 'regression' ou 'classification'
        FileNotFoundError: Se arquivo CSV não existir
    """
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    # Valida task
    if task not in ['regression', 'classification']:
        raise ValueError(f"task deve ser 'regression' ou 'classification', '{task}' não é uma opção.")

    # Importa o módulo correto baseado na task
    if task == 'regression':
        from pycaret.regression import setup, create_model, tune_model, finalize_model, save_model
    else:
        from pycaret.classification import setup, create_model, tune_model, finalize_model, save_model

    # Carrega dados
    if isinstance(caminho_csv, pd.DataFrame):
        data_nome = caminho_csv.copy()
    else:
        try:
            data_nome = pd.read_csv(caminho_csv)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{caminho_csv}' não encontrado")

    # Setup
    setup(data=data_nome, target=target, session_id=numero_seed, verbose=False)

    # Cria modelo base
    modelo = create_model(algoritmo)

    # Otimiza modelo
    tuned = tune_model(modelo, n_iter=iterações)

    # Finaliza
    final = finalize_model(tuned)

    # Salva modelo
    save_model(final, nome)

    print(f"✅ Modelo '{nome}' treinado e salvo com sucesso!")

    return final
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────