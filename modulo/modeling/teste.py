"""
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       ████████╗███████╗░██████╗████████╗███████╗                                     │
│                                       ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝                                     │
│                                       ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░█████╗░░                                     │
│                                       ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░                                     │
│                                       ░░░██║░░░███████╗██████╔╝░░░██║░░░███████╗                                     │
│                                       ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝                                     │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                    „ʇǝʇɥɔᴉɹǝƃ ɹᴉʍ ǝᴉʍ ʇʇo⅁ ʇǝʇɥɔᴉɹ ʇlǝzuǝuɹǝʇS ɯɹǝq∩„
"""

import matplotlib.pyplot as plt
import numpy as np
# def teste
import pandas as pd
from pycaret.classification import *
from pycaret.regression import *
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                        
                                                ╭━━━━╮╱╱╱╱╭╮
                                                ┃╭╮╭╮┃╱╱╱╭╯╰╮
                                                ╰╯┃┃┣┻━┳━┻╮╭╋━━╮
                                                ╱╱┃┃┃┃━┫━━┫┃┃┃━┫
                                                ╱╱┃┃┃┃━╋━━┃╰┫┃━┫
                                                ╱╱╰╯╰━━┻━━┻━┻━━╯

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""

def teste(caminho_csv, modelo_nome, task='regression'):

    """
    Testa modelo treinado com PyCaret. Retorna DataFrame com previsões e métricas principais.

    Args:
        caminho_csv (str ou pd.DataFrame): Caminho para o arquivo CSV de teste ou DataFrame.
        modelo_nome (str): Nome do modelo treinado/salvo (sem extensão).
        task (str): 'regression' ou 'classification' (default: 'regression')

    Returns:
        DataFrame com previsões e métricas geradas pelo PyCaret.

    Raises:
        ValueError: Se task não for válida.
        FileNotFoundError: Se arquivo ou modelo não for encontrado.
    """
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    # Valida task
    if task not in ['regression', 'classification']:
        raise ValueError(f"task deve ser 'regression' ou 'classification', '{task}' não é uma opção.")

    # Carrega dados (aceita caminho para CSV ou DataFrame)
    if isinstance(caminho_csv, pd.DataFrame):
        dados_teste = caminho_csv.copy()
    else:
        try:
            dados_teste = pd.read_csv(caminho_csv)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{caminho_csv}' não encontrado")

    # Carrega modelo treinado
    try:
        if task == 'regression':
            modelo = load_model(modelo_nome)
            resultado = predict_model(modelo, data=dados_teste)
        else:
            modelo = load_model(modelo_nome)
            resultado = predict_model(modelo, data=dados_teste)
    except FileNotFoundError:
        raise FileNotFoundError(f"Modelo '{modelo_nome}' não encontrado")

    print(f"✅ Teste do modelo '{modelo_nome}' concluído com sucesso!")
    return resultado

"""
#───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

                                        ╭━╮╭━╮╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╭━╮
                                        ┃┃╰╯┃┃╱╭╯╰╮╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱┃╭╯
                                        ┃╭╮╭╮┣━┻╮╭╋━┳┳━━━╮┃┃╱╰╋━━┳━┳╯╰┳╮╭┳━━━┳━━┳━━╮
                                        ┃┃┃┃┃┃╭╮┃┃┃╭╋╋━━┃┃┃┃╱╭┫╭╮┃╭╋╮╭┫┃┃┣━━┃┃╭╮┃╭╮┃
                                        ┃┃┃┃┃┃╭╮┃╰┫┃┃┃┃━━┫┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃┃━━┫╭╮┃╰╯┃
                                        ╰╯╰╯╰┻╯╰┻━┻╯╰┻━━━╯╰━━━┻━━┻╯╰┻╯╰━━┻━━━┻╯╰┻━━╯

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""

def matriz_confusao(
        resultado: pd.DataFrame,
        target_col: str = 'target',
        pred_col: str = 'prediction_label'
) -> np.ndarray:  # ✅ CORRETO: retorna NumPy array
    """
    Gera matriz de confusão a partir do DataFrame de resultado do teste.

    Args:
        resultado: DataFrame retornado pela função teste
        target_col: Nome da coluna target (default: 'target')
        pred_col: Nome da coluna de predição (default: 'prediction_label')

    Returns:
        Matriz de confusão como NumPy array
    """
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    cm: np.ndarray = confusion_matrix(resultado[target_col], resultado[pred_col])
    disp: ConfusionMatrixDisplay = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap='Blues', values_format='d')
    plt.title('Matriz de Confusão')
    plt.show()

    print(f"✅ Matriz de confusão gerada!")
    return cm
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────