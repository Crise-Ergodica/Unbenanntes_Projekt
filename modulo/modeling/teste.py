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
    import pandas as pd

    """
    Testa modelo treinado com PyCaret. Retorna DataFrame com previsões e métricas principais.

    Args:
        caminho_csv (str ou pd.DataFrame): Caminho para o arquivo CSV de teste ou DataFrame.
        modelo_nome (str): Nome do modelo treinado/salvo (sem extensão).
        task (str): 'regression' ou 'classification' (default: 'regression')

    Returns:
        DataFrame com previsões e métricas geradas pelo PyCaret.

    Raises:
        ValueError: Se task for inválida.
        FileNotFoundError: Se arquivo ou modelo não for encontrado.
    """
    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    if task not in ['regression', 'classification']:
        raise ValueError(f"task deve ser 'regression' ou 'classification', '{task}' não é uma opção.")

        # Importa o módulo correto
    if task == 'regression':
        from pycaret.regression import load_model, predict_model
    else:
        from pycaret.classification import load_model, predict_model

        # Carrega dados
    if isinstance(caminho_csv, pd.DataFrame):
        dados_teste = caminho_csv.copy()
    else:
        try:
            dados_teste = pd.read_csv(caminho_csv)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{caminho_csv}' não encontrado")

        # Carrega modelo e faz predição
    try:
        modelo = load_model(modelo_nome)
        resultado = predict_model(modelo, data=dados_teste)
    except FileNotFoundError:
        raise FileNotFoundError(f"Modelo '{modelo_nome}' não encontrado")

    print(f"✅ Teste do modelo '{modelo_nome}' concluído com sucesso!")
    return resultado


"""
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

                                        ╭━╮╭━╮╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╭━╮
                                        ┃┃╰╯┃┃╱╭╯╰╮╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱┃╭╯
                                        ┃╭╮╭╮┣━┻╮╭╋━┳┳━━━╮┃┃╱╰╋━━┳━┳╯╰┳╮╭┳━━━┳━━┳━━╮
                                        ┃┃┃┃┃┃╭╮┃┃┃╭╋╋━━┃┃┃┃╱╭┫╭╮┃╭╋╮╭┫┃┃┣━━┃┃╭╮┃╭╮┃
                                        ┃┃┃┃┃┃╭╮┃╰┫┃┃┃┃━━┫┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃┃━━┫╭╮┃╰╯┃
                                        ╰╯╰╯╰┻╯╰┻━┻╯╰┻━━━╯╰━━━┻━━┻╯╰┻╯╰━━┻━━━┻╯╰┻━━╯

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""
# IMPORTAÇÕES
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# FUNÇÃO MATRIZ CONFUSAO
def matriz_confusao(
        resultado: pd.DataFrame,
        target_col: str = 'target',
        pred_col: str = 'prediction_label',
        labels: list = None,
        normalize: bool = False,
        figsize: tuple = (10, 8),
        cmap: str = 'Blues',
        title: str = None,
        show_metrics: bool = True,
        save_path: str = None) -> np.ndarray:
    """
       Gera matriz de confusão profissional com métricas detalhadas.

       Args:
           resultado: DataFrame retornado pela função teste
           target_col: Nome da coluna target (default: 'target')
           pred_col: Nome da coluna de predição (default: 'prediction_label')
           labels: Lista com nomes das classes (ex: ['Setosa', 'Versicolor', 'Virginica'])
           normalize: Se True, mostra percentuais ao invés de contagens (default: False)
           figsize: Tamanho da figura (largura, altura) (default: (10, 8))
           cmap: Colormap do matplotlib (default: 'Blues')
           title: Título customizado (default: automático)
           show_metrics: Se True, mostra métricas detalhadas (default: True)
           save_path: Caminho para salvar a figura (default: None, não salva)

       Returns:
           Matriz de confusão como NumPy array
       """

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    # Extrai valores verdadeiros e preditos
    y_true = resultado[target_col]
    y_pred = resultado[pred_col]

    # Calcula matriz de confusão
    if normalize:
        cm = confusion_matrix(y_true, y_pred, normalize='true')
        values_format = '.2%'
    else:
        cm = confusion_matrix(y_true, y_pred)
        values_format = 'd'

    # Calcula métricas
    accuracy = accuracy_score(y_true, y_pred)
    precision_macro = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall_macro = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1_macro = f1_score(y_true, y_pred, average='macro', zero_division=0)

    # Cria figura com subplot
    fig, ax = plt.subplots(figsize=figsize)

    # Display da matriz
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=labels
    )
    disp.plot(
        cmap=cmap,
        values_format=values_format,
        ax=ax,
        colorbar=True,
        im_kw=dict(interpolation='nearest')
    )

    # Título
    if title is None:
        if normalize:
            title = f'Matriz de Confusão (Normalizada)\nAcurácia: {accuracy:.2%}'
        else:
            title = f'Matriz de Confusão\nAcurácia: {accuracy:.2%}'

    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

    # Labels dos eixos mais claros
    ax.set_xlabel('Classe Predita', fontsize=12, fontweight='bold')
    ax.set_ylabel('Classe Verdadeira', fontsize=12, fontweight='bold')

    # Grid sutil
    ax.grid(False)

    # Ajusta layout
    plt.tight_layout()# Ajusta layout

    # Salva se solicitado
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Figura salva em '{save_path}'")

    plt.show()

    print("=" * 70)
    print("✅ MATRIZ DE CONFUSÃO GERADA COM SUCESSO!")
    print("=" * 70)

    if show_metrics:
        print(f"\n MÉTRICAS GLOBAIS:")
        print(f"Acurácia: {accuracy:.2%}")
        print(f"Precision (Macro): {precision_macro:.2%}")
        print(f"Recall (Macro): {recall_macro:.2%}")
        print(f"F1-Score (Macro): {f1_macro:.2%}")

    return cm
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
