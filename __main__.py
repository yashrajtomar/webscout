import os
import importlib
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def list_modules():
    module_dir = os.path.join(os.path.dirname(__file__), "modules")
    return [f[:-3] for f in os.listdir(module_dir) if f.endswith(".py") and not f.startswith("__")]

def show_module_table(modules):
    table = Table(title="📦 Available Modules", show_lines=True, border_style="blue")
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("Module Name", style="bold magenta")

    for idx, module in enumerate(modules, 1):
        table.add_row(str(idx), module)

    console.print(table)

def select_modules(modules):
    show_module_table(modules)
    choices = Prompt.ask(
        "[bold cyan]Enter module number(s) to run (e.g. 1 or 1,2,3)[/bold cyan]"
    )
    selected = [modules[int(i.strip()) - 1] for i in choices.split(",") if i.strip().isdigit()]
    return selected

def main():
    console.print(Panel("[bold cyan]Welcome to WebScout CLI[/bold cyan]", border_style="blue"))
    modules = list_modules()
    selected_modules = select_modules(modules)

    target = Prompt.ask("[bold green]Enter the target (IP/domain)[/bold green]")

    for module_name in selected_modules:
        mod = importlib.import_module(f"modules.{module_name}")
        switches = Prompt.ask(f"[bold green]Enter switches for [cyan]{module_name}[/cyan] (or leave blank)[/bold green]").split()

        try:
            output = mod.run(target, switches)
            mod.display(output)
        except Exception as e:
            console.print(f"[bold red]Error running {module_name}:[/bold red] {e}")

if __name__ == "__main__":
    main()
