#!/usr/bin/env python3
"""
Unbenanntes Projekt - Interactive Configuration CLI
Usando Rich para criar uma interface terminal artística
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt
from rich.table import Table
from rich.markdown import Markdown
from rich import box
from rich.text import Text
import json
from datetime import datetime
from pathlib import Path

console = Console()

BANNER = """
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
"""


def show_banner():
    """Exibe o banner ASCII artístico"""
    console.clear()
    banner_text = Text(BANNER, style="bold cyan")
    console.print(banner_text)
    console.print(
        Panel(
            "[italic]„ʇǝʇɥɔᴉɹǝƃ ɹᴉʍ ǝᴉʍ ʇʇo⅁ ʇǝʇɥɔᴉɹ ʇlǝzuǝuɹǝʇS ɯɹǝq∩„[/italic]",
            style="dim white",
            border_style="cyan",
            box=box.DOUBLE
        )
    )
    console.print("\n")


def get_data_config():
    """Coleta configurações de dados"""
    console.print(Panel.fit(
        "📊 [bold cyan]CONFIGURAÇÃO DE DADOS[/bold cyan]",
        border_style="cyan"
    ))
    
    data_path = Prompt.ask(
        "[yellow]📁 Caminho do Dataset[/yellow]",
        default="data/raw/dataset.csv"
    )
    
    target_column = Prompt.ask(
        "[yellow]🎯 Coluna Target (variável alvo)[/yellow]",
        default="target"
    )
    
    problem_type = Prompt.ask(
        "[yellow]🔍 Tipo de Problema[/yellow]",
        choices=["classification", "regression"],
        default="classification"
    )
    
    test_size = FloatPrompt.ask(
        "[yellow]📊 Tamanho do conjunto de teste (%)[/yellow]",
        default=20.0
    )
    
    console.print("✅ [green]Configuração de dados completa![/green]\n")
    
    return {
        "path": data_path,
        "target_column": target_column,
        "problem_type": problem_type,
        "test_size": test_size / 100
    }


def get_model_config():
    """Coleta configurações de modelos"""
    console.print(Panel.fit(
        "🤖 [bold cyan]CONFIGURAÇÃO DE MODELOS[/bold cyan]",
        border_style="cyan"
    ))
    
    # Tabela de modelos disponíveis
    table = Table(title="Modelos Disponíveis", box=box.ROUNDED)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Nome", style="yellow")
    table.add_column("Tipo", style="green")
    
    models_info = [
        ("rf", "Random Forest", "Ensemble"),
        ("lr", "Logistic Regression", "Linear"),
        ("dt", "Decision Tree", "Tree-based"),
        ("xgboost", "XGBoost", "Boosting"),
        ("lightgbm", "LightGBM", "Boosting"),
        ("knn", "K-Nearest Neighbors", "Instance-based"),
        ("svm", "Support Vector Machine", "Kernel"),
        ("nb", "Naive Bayes", "Probabilistic")
    ]
    
    for model_id, name, tipo in models_info:
        table.add_row(model_id, name, tipo)
    
    console.print(table)
    console.print()
    
    models_input = Prompt.ask(
        "[yellow]🎯 Modelos para treinar (separados por vírgula)[/yellow]",
        default="rf,xgboost,lightgbm"
    )
    selected_models = [m.strip() for m in models_input.split(",")]
    
    n_folds = IntPrompt.ask(
        "[yellow]🔄 Número de folds (Cross-Validation)[/yellow]",
        default=5
    )
    
    metric_choices = ["Accuracy", "AUC", "Recall", "Precision", "F1", "MAE", "RMSE", "R2"]
    metric = Prompt.ask(
        "[yellow]📈 Métrica de avaliação principal[/yellow]",
        choices=metric_choices,
        default="Accuracy"
    )
    
    console.print("✅ [green]Configuração de modelos completa![/green]\n")
    
    return {
        "selected": selected_models,
        "n_folds": n_folds,
        "metric": metric
    }


def get_preprocessing_config():
    """Coleta configurações de pré-processamento"""
    console.print(Panel.fit(
        "⚙️ [bold cyan]PRÉ-PROCESSAMENTO[/bold cyan]",
        border_style="cyan"
    ))
    
    normalize = Confirm.ask(
        "[yellow]🔧 Normalizar features numéricas?[/yellow]",
        default=True
    )
    
    remove_outliers = Confirm.ask(
        "[yellow]🚫 Remover outliers automaticamente?[/yellow]",
        default=False
    )
    
    handle_imbalance = Confirm.ask(
        "[yellow]⚖️ Balancear classes (SMOTE)?[/yellow]",
        default=False
    )
    
    console.print("✅ [green]Configuração de pré-processamento completa![/green]\n")
    
    return {
        "normalize": normalize,
        "remove_outliers": remove_outliers,
        "handle_imbalance": handle_imbalance
    }


def get_output_config():
    """Coleta configurações de saída"""
    console.print(Panel.fit(
        "💾 [bold cyan]CONFIGURAÇÃO DE SAÍDA[/bold cyan]",
        border_style="cyan"
    ))
    
    model_dir = Prompt.ask(
        "[yellow]📁 Diretório para salvar modelos[/yellow]",
        default="models/"
    )
    
    experiment_name = Prompt.ask(
        "[yellow]🏷️ Nome do experimento[/yellow]",
        default=f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    
    save_plots = Confirm.ask(
        "[yellow]📊 Salvar gráficos e matriz de confusão?[/yellow]",
        default=True
    )
    
    console.print("✅ [green]Configuração de saída completa![/green]\n")
    
    return {
        "model_dir": model_dir,
        "experiment_name": experiment_name,
        "save_plots": save_plots
    }


def get_advanced_config():
    """Coleta configurações avançadas"""
    console.print(Panel.fit(
        "🔬 [bold cyan]CONFIGURAÇÕES AVANÇADAS[/bold cyan]",
        border_style="cyan"
    ))
    
    random_seed = IntPrompt.ask(
        "[yellow]🎲 Random seed (reprodutibilidade)[/yellow]",
        default=42
    )
    
    verbose = Confirm.ask(
        "[yellow]📢 Modo verbose (logs detalhados)?[/yellow]",
        default=True
    )
    
    notes = Prompt.ask(
        "[yellow]📝 Notas adicionais (opcional)[/yellow]",
        default=""
    )
    
    console.print("✅ [green]Configuração avançada completa![/green]\n")
    
    return {
        "random_seed": random_seed,
        "verbose": verbose,
        "notes": notes
    }


def show_config_summary(config):
    """Exibe resumo das configurações"""
    console.print("\n")
    console.print(Panel.fit(
        "📋 [bold green]RESUMO DA CONFIGURAÇÃO[/bold green]",
        border_style="green"
    ))
    
    # Criar tabela de resumo
    table = Table(box=box.ROUNDED, show_header=False, border_style="cyan")
    table.add_column("Campo", style="yellow")
    table.add_column("Valor", style="white")
    
    table.add_row("Dataset", config["data"]["path"])
    table.add_row("Target", config["data"]["target_column"])
    table.add_row("Tipo", config["data"]["problem_type"])
    table.add_row("Modelos", ", ".join(config["models"]["selected"]))
    table.add_row("Métrica", config["models"]["metric"])
    table.add_row("CV Folds", str(config["models"]["n_folds"]))
    table.add_row("Normalizar", "✓" if config["preprocessing"]["normalize"] else "✗")
    table.add_row("Experimento", config["output"]["experiment_name"])
    
    console.print(table)


def generate_python_script(config):
    """Gera o script Python PyCaret"""
    script = f"""# Unbenanntes Projekt - Configuração Gerada Automaticamente
# Experimento: {config['output']['experiment_name']}
# Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

import pandas as pd
from pycaret.{config['data']['problem_type']} import *

# ═══════════════════════════════════════════════════════════
# 📊 CARREGAMENTO DE DADOS
# ═══════════════════════════════════════════════════════════
data = pd.read_csv('{config['data']['path']}')

# ═══════════════════════════════════════════════════════════
# ⚙️ SETUP DO AMBIENTE PYCARET
# ═══════════════════════════════════════════════════════════
exp = setup(
    data=data,
    target='{config['data']['target_column']}',
    train_size={1 - config['data']['test_size']:.2f},
    session_id={config['advanced']['random_seed']},
    normalize={config['preprocessing']['normalize']},
    remove_outliers={config['preprocessing']['remove_outliers']},
    fix_imbalance={config['preprocessing']['handle_imbalance']},
    fold={config['models']['n_folds']},
    verbose={config['advanced']['verbose']}
)

# ═══════════════════════════════════════════════════════════
# 🤖 TREINAMENTO DE MODELOS
# ═══════════════════════════════════════════════════════════
models_to_train = {config['models']['selected']}

best_models = {{}}
for model_id in models_to_train:
    print(f"\\n🔄 Treinando modelo: {{model_id}}")
    model = create_model(model_id, fold={config['models']['n_folds']})
    tuned = tune_model(model, optimize='{config['models']['metric']}')
    best_models[model_id] = tuned

# ═══════════════════════════════════════════════════════════
# 📊 COMPARAÇÃO DE MODELOS
# ═══════════════════════════════════════════════════════════
comparison = compare_models(include=models_to_train, sort='{config['models']['metric']}')

# ═══════════════════════════════════════════════════════════
# 💾 SALVANDO O MELHOR MODELO
# ═══════════════════════════════════════════════════════════
best_model = comparison
save_model(best_model, '{config['output']['model_dir']}{config['output']['experiment_name']}_best_model')

# ═══════════════════════════════════════════════════════════
# 📈 AVALIAÇÃO E VISUALIZAÇÕES
# ═══════════════════════════════════════════════════════════
"""
    
    if config['output']['save_plots']:
        script += """plot_model(best_model, plot='confusion_matrix', save=True)
plot_model(best_model, plot='auc', save=True)
plot_model(best_model, plot='feature', save=True)
"""
    else:
        script += "# Visualizações desabilitadas\n"
    
    script += f"""
# ═══════════════════════════════════════════════════════════
# ✅ FINALIZAÇÃO
# ═══════════════════════════════════════════════════════════
final_model = finalize_model(best_model)
save_model(final_model, '{config['output']['model_dir']}{config['output']['experiment_name']}_final_model')

print("\\n✨ Treinamento concluído com sucesso!")
print(f"📁 Modelos salvos em: {config['output']['model_dir']}")
"""
    
    if config['advanced']['notes']:
        script += f"print(f\"📝 Notas: {config['advanced']['notes']}\")\n"
    
    return script


def save_config_and_script(config, script):
    """Salva configuração JSON e script Python"""
    output_dir = Path("generated_configs")
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Salvar JSON
    json_path = output_dir / f"config_{timestamp}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    # Salvar Python script
    script_path = output_dir / f"train_{timestamp}.py"
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script)
    
    return json_path, script_path


def main():
    """Função principal"""
    show_banner()
    
    console.print(Panel(
        "[bold cyan]Bem-vindo ao Configurador Interativo de ML![/bold cyan]\n"
        "Este assistente irá guiá-lo pela configuração completa do seu experimento.",
        border_style="cyan",
        box=box.DOUBLE
    ))
    console.print("\n")
    
    # Coleta todas as configurações
    config = {
        "data": get_data_config(),
        "models": get_model_config(),
        "preprocessing": get_preprocessing_config(),
        "output": get_output_config(),
        "advanced": get_advanced_config()
    }
    
    # Mostra resumo
    show_config_summary(config)
    
    # Confirma para gerar
    console.print("\n")
    if Confirm.ask("[bold yellow]🚀 Gerar script Python e salvar configurações?[/bold yellow]"):
        with console.status("[bold green]Gerando arquivos...[/bold green]"):
            script = generate_python_script(config)
            json_path, script_path = save_config_and_script(config, script)
        
        console.print("\n")
        console.print(Panel.fit(
            f"[bold green]✅ ARQUIVOS GERADOS COM SUCESSO![/bold green]\n\n"
            f"📄 Configuração JSON: [cyan]{json_path}[/cyan]\n"
            f"🐍 Script Python: [cyan]{script_path}[/cyan]\n\n"
            f"[yellow]Para executar:[/yellow]\n"
            f"[white]python {script_path}[/white]",
            border_style="green",
            box=box.DOUBLE
        ))
    else:
        console.print("[yellow]❌ Operação cancelada.[/yellow]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ Operação interrompida pelo usuário.[/yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Erro: {e}[/bold red]")
