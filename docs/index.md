---
title: Início
---

# 🌟 Unbenanntes_Projekt

<div class="ascii-banner">
██╗░░░██╗███╗░░██╗██████╗░███████╗███╗░░██╗░█████╗░███╗░░██╗███╗░░██╗████████╗███████╗░██████╗
██║░░░██║████╗░██║██╔══██╗██╔════╝████╗░██║██╔══██╗████╗░██║████╗░██║╚══██╔══╝██╔════╝██╔════╝
██║░░░██║██╔██╗██║██████╦╝█████╗░░██╔██╗██║███████║██╔██╗██║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
██║░░░██║██║╚████║██╔══██╗██╔══╝░░██║╚████║██╔══██║██║╚████║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
╚██████╔╝██║░╚███║██████╦╝███████╗██║░╚███║██║░░██║██║░╚███║██║░╚███║░░░██║░░░███████╗██████╔╝
░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░

██████╗░██████╗░░█████╗░░░░░░██╗███████╗██╗░░██╗████████╗  ░█████╗░░░░░█████╗░░░░░█████╗░
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██║░██╔╝╚══██╔══╝  ██╔══██╗░░░██╔══██╗░░░██╔══██╗
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░█████═╝░░░░██║░░░  ██║░░██║░░░██║░░██║░░░██║░░██║
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██╔═██╗░░░░██║░░░  ██║░░██║░░░██║░░██║░░░██║░░██║
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗██║░╚██╗░░░██║░░░  ╚█████╔╝██╗╚█████╔╝██╗╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░╚════╝░╚═╝░╚════╝░
</div>

<div class="subtitle-center">
„ʇǝʇɥɔᴉɹǝƃ ɹᴉʍ ǝᴉʍ ʇʇo⅁ ʇǝʇɥɔᴉɹ ʇlǝzuǝuɹǝʇS ɯɹǝq∩„
</div>

---

## 🎯 O Que É Este Projeto?

**Unbenanntes_Projekt** (Projeto Sem Nome) é uma biblioteca Python desenvolvida para **automatizar workflows de Machine Learning de ponta a ponta** — do pré-processamento de dados até a implementação e avaliação de modelos em produção.

!!! success "Filosofia do Projeto"
    Construído sobre o **PyCaret**, este projeto oferece uma interface **didática, simplificada e poderosa** para quem quer aprender, ensinar ou aplicar Machine Learning de forma profissional.

---

## ✨ Principais Funcionalidades

<div class="grid cards" markdown>

-   :material-brain: **Treinamento Automatizado**

    ---
    
    Configure e treine modelos de ML com poucas linhas de código. Suporte para regressão e classificação com otimização automática de hiperparâmetros.

    [:octicons-arrow-right-24: Ver Módulo de Treino](modulos/treino.md)

-   :material-chart-line: **Avaliação Completa**

    ---
    
    Teste modelos treinados, gere métricas detalhadas, matrizes de confusão profissionais e relatórios visuais.

    [:octicons-arrow-right-24: Ver Módulo de Teste](modulos/teste.md)

-   :material-table: **Gestão de Dados**

    ---
    
    Scripts prontos para carregar, limpar, transformar e preparar datasets para Machine Learning.

    [:octicons-arrow-right-24: Ver Módulo Dataset](modulos/dataset.md)

-   :material-feature-search: **Engenharia de Features**

    ---
    
    Crie atributos customizados, transformações e combinações de variáveis para melhorar performance dos modelos.

    [:octicons-arrow-right-24: Ver Módulo Features](modulos/features.md)

-   :material-chart-bell-curve: **Visualizações**

    ---
    
    Gere gráficos profissionais para análise exploratória, performance de modelos e apresentações.

    [:octicons-arrow-right-24: Ver Módulo Plots](modulos/plots.md)

-   :material-notebook: **Notebooks Didáticos**

    ---
    
    Exemplos práticos em Jupyter para exploração, aprendizado e experimentação rápida.

    [:octicons-arrow-right-24: Ver Exemplos](exemplos.md)

</div>

---

## 🚀 Início Rápido

### Instalação

# Clone o repositório
git clone https://github.com/Crise-Ergodica/Unbenanntes_Projekt.git
cd Unbenanntes_Projekt

# Crie ambiente virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt
pip install -e .

[:octicons-arrow-right-24: Guia Completo de Instalação](instalacao.md)

---

### Exemplo Básico: Treinar um Modelo

import pandas as pd
from modulo.modeling.treino import treino

# Carrega seus dados
dados = pd.read_csv('data/processed/meu_dataset.csv')

# Treina modelo de regressão com Gradient Boosting
modelo = treino(
    caminho_csv=dados,
    target='preco',           # Coluna alvo
    nome='modelo_preco',      # Nome para salvar
    task='regression',        # Tipo de tarefa
    algoritmo='gbr',          # Gradient Boosting Regressor
    iterações=50,             # Otimizações
    numero_seed=42            # Reprodutibilidade
)

# ✅ Modelo treinado e salvo em 'modelo_preco.pkl'!

[:octicons-arrow-right-24: Ver Documentação do Módulo de Treino](modulos/treino.md)

---

### Exemplo Básico: Testar e Avaliar

from modulo.modeling.teste import teste, matriz_confusao

# Testa modelo com novos dados
resultado = teste(
    caminho_csv='data/processed/dados_teste.csv',
    modelo_nome='modelo_preco',
    task='regression'
)

# Para classificação, gere matriz de confusão
# (descomente se sua task for 'classification')
# cm = matriz_confusao(
#     resultado=resultado,
#     target_col='categoria_real',
#     pred_col='prediction_label',
#     labels=['Classe A', 'Classe B', 'Classe C'],
#     show_metrics=True,
#     save_path='reports/figures/confusion_matrix.png'
# )

print(resultado.head())
# ✅ Predições e métricas calculadas!

[:octicons-arrow-right-24: Ver Documentação do Módulo de Teste](modulos/teste.md)

---

## 📚 Estrutura do Projeto

Unbenanntes_Projekt/
├── README.md               # Documentação principal
├── requirements.txt        # Dependências Python
├── setup.py               # Instalação do pacote
├── data/                  # Datasets organizados
│   ├── raw/              # Dados brutos originais
│   ├── processed/        # Dados preparados para ML
│   ├── interim/          # Dados intermediários
│   └── external/         # Dados de fontes externas
├── models/               # Modelos treinados (.pkl)
├── notebooks/            # Jupyter Notebooks exploratórios
├── reports/              # Relatórios e visualizações
│   └── figures/         # Gráficos e imagens
├── modulo/              # 📦 Código fonte principal
│   ├── __init__.py
│   ├── config.py        # Configurações
│   ├── dataset.py       # Gestão de dados
│   ├── features.py      # Engenharia de features
│   ├── plots.py         # Visualizações
│   └── modeling/        # 🧠 Machine Learning
│       ├── __init__.py
│       ├── treino.py    # Treinamento
│       └── teste.py     # Teste & Avaliação
└── docs/                # 📖 Esta documentação!

[:octicons-arrow-right-24: Explorar Estrutura Detalhada](estrutura.md)

---

## 🎓 Para Quem é Este Projeto?

!!! tip "Perfeito Para"
    - **Estudantes de ML/Data Science**: Aprenda conceitos com código comentado e exemplos práticos
    - **Professores**: Use como material didático com estrutura clara e documentação completa
    - **Profissionais**: Acelere workflows de ML com automação inteligente
    - **Pesquisadores**: Base sólida para experimentação e prototipagem rápida

---

## 🛠️ Tecnologias Utilizadas

<div class="tech-stack">

- **Python 3.8+** - Linguagem principal
- **PyCaret** - AutoML e pipeline de ML
- **Pandas** - Manipulação de dados
- **Scikit-learn** - Algoritmos e métricas
- **Matplotlib/Seaborn** - Visualizações
- **Jupyter** - Notebooks interativos

</div>

---

## 🗺️ Navegação Rápida

<div class="quick-nav">

| Seção | Descrição | Link |
|-------|-----------|------|
| 📖 **Sobre** | História e motivação do projeto | [Sobre](sobre.md) |
| 🔧 **Instalação** | Guia completo de setup | [Instalação](instalacao.md) |
| 🏗️ **Estrutura** | Organização de pastas e arquivos | [Estrutura](estrutura.md) |
| 🧩 **Módulos** | Documentação de cada módulo Python | [Módulos](modulos/index.md) |
| 💡 **Exemplos** | Casos de uso práticos | [Exemplos](exemplos.md) |
| 📚 **API Reference** | Referência completa de funções | [API](api.md) |
| 🤝 **Contribuindo** | Como colaborar com o projeto | [Contribuindo](contribuindo.md) |

</div>

---

## 👤 Autora

**Aurora Drumond Costa Magalhães**

- :fontawesome-brands-github: GitHub: [@Crise-Ergodica](https://github.com/Crise-Ergodica)
- :fontawesome-solid-envelope: Email: gdcm10@gmail.com
- :fontawesome-solid-star: **Se este projeto te ajudou, considere dar uma estrela!** ⭐

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](https://github.com/Crise-Ergodica/Unbenanntes_Projekt/blob/master/LICENSE) para mais detalhes.

---

<div class="footer-quote">
„ʇǝʇɥɔᴉɹǝƃ ɹᴉʍ ǝᴉʍ ʇʇo⅁ ʇǝʇɥɔᴉɹ ʇlǝzuǝuɹǝʇS ɯɹǝq∩„

*Feito com :material-coffee: e muito código Python*
</div>