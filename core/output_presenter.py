from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text


class OutputPresenter:
    def __init__(self):
        self.console = Console()

    def display_output(self, title, content):
        self.console.print(Panel(content, title=title, border_style="green"))

    def display_colored_nmap_output(self, output):
        lines = output.strip().split('\n')
        styled_output = Text()

        for line in lines:
            if "open" in line:
                styled_output.append(line + "\n", style="bold green")
            elif "closed" in line:
                styled_output.append(line + "\n", style="dim red")
            elif "filtered" in line:
                styled_output.append(line + "\n", style="yellow")
            elif "Nmap scan report for" in line:
                styled_output.append(line + "\n", style="bold cyan")
            else:
                styled_output.append(line + "\n")

        self.console.print(Panel(styled_output, title="Nmap Scan Results", border_style="blue"))
'''        
    def display(self, title, output):
        if not output:
            output = "[bold red]No output received or tool failed to run.[/bold red]"
        self.console.print(Panel.fit(str(output), title=f"[bold green]{title}", border_style="cyan"))
'''