#!/usr/bin/env python3
import os
import importlib
import requests
from core.tool_runner import ToolRunner
from core.output_presenter import OutputPresenter
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def list_modules():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current dir of __main__.py
    module_dir = os.path.join(current_dir, "modules")         # Join with modules
    return [f[:-3] for f in os.listdir(module_dir) if f.endswith(".py") and not f.startswith("__")]

def main():
    console.print(Panel("[bold cyan]Welcome to WebScout CLI[/bold cyan]", border_style="blue"))

    modules = list_modules()
    for i, mod in enumerate(modules):
        console.print(f"[bold green]{i + 1}[/bold green]. {mod}")

    choice = int(Prompt.ask("[bold yellow]Choose a tool to run[/bold yellow]")) - 1
    selected_module = modules[choice]

    target = Prompt.ask("[bold yellow]Enter target (IP or domain)[/bold yellow]")
    switches_input = Prompt.ask("[bold yellow]Enter switches (e.g., -sV -T4)[/bold yellow]")
    switches = switches_input.split()

    tool_module = importlib.import_module(f"modules.{selected_module}")
    output = tool_module.run(target, switches)
    tool_module.display(output)

if __name__ == "__main__":
    list_modules()
    main()