```

██╗░░░██╗███╗░░██╗██████╗░███████╗███╗░░██╗░█████╗░███╗░░██╗███╗░░██╗████████╗███████╗░██████╗
██║░░░██║████╗░██║██╔══██╗██╔════╝████╗░██║██╔══██╗████╗░██║████╗░██║╚══██╔══╝██╔════╝██╔════╝
██║░░░██║██╔██╗██║██████╦╝█████╗░░██╔██╗██║███████║██╔██╗██║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
██║░░░██║██║╚████║██╔══██╗██╔══╝░░██║╚████║██╔══██║██║╚████║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
╚██████╔╝██║░╚███║██████╦╝███████╗██║░╚███║██║░░██║██║░╚███║██║░╚███║░░░██║░░░███████╗██████╔╝
░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░

██████╗░██████╗░░█████╗░░░░░░██╗███████╗██╗░░██╗████████╗  ░█████╗░░░░░█████╗░░░░░█████╗░
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██║░██╔╝╚══██╔══╝  ██╔══██╗░░░██╔══██╗░░░██╔══██╗
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░█████═╝░░░░██║░░░  ██║░░██║░░░██║░░██║░░░██║░░██║
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██╔═██╗░░░░██║░░░  ██║░░██║░░░██║░░██║░░░██║░░██║
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗██║░╚██╗░░░██║░░░  ╚█████╔╝██╗╚█████╔╝██╗╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░╚════╝░╚═╝░╚════╝░

                  „ʇǝʇɥɔᴉɹǝƃ ɹᴉʍ ǝᴉʍ ʇʇo⅁ ʇǝʇɥɔᴉɹ ʇlǝzuǝuɹǝʇS ɯɹǝq∩„
```
<div align="center">

**Um inferno em forma de arquivo Python, criado para estudos de Machine Learning**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyCaret](https://img.shields.io/badge/powered%20by-PyCaret-orange.svg)](https://pycaret.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
</div>

---

## Sobre

**Unbenanntes Projekt** (Projeto Sem Nome) é uma biblioteca Python desenvolvida para **automatizar workflows de Machine 
Learning**, desde o treinamento até a avaliação de modelos. Construída sobre o [PyCaret](https://pycaret.org/), oferece 
uma interface simplificada para:
- Pré-processamento de dados
- Treinamento de modelos
- Avaliação de modelos
- Implementação de modelos

---

## Iniciando
### Instalação

##### ~ Clone o repositório:

    git clone https://github.com/Crise-Ergodica/Unbenanntes_Projekt.git
    cd Unbenanntes_Projekt
    
    Crie um ambiente virtual (recomendado)
    python -m venv .venv
    source .venv/bin/activate # Linux/Mac
    
    ou
    .venv\Scripts\activate # Windows

##### ~ Instale as Dependências:
    pip install -r requirements.txt
    pip install -e .
##### ~ Carregue seus dados:
    dados = pd.read_csv('seu_dataset.csv')
##### ~ USe as funções Unbenanntes:
```
Localizadas em:

│
├── Modulo   
│   ├── modeling  <- AQUI

Servem para treinar, testar e criar matriz de confusão.
```

---

## Organização

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         Modulo and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── Modulo   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes Modulo a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------
_Aurora Drumond Costa Magalhães_
