from rich.console import Console
from rich.panel import Panel

class OutputPresenter:
    def __init__(self):
        self.console = Console()
    
    def display(self, title, output):
        if not output:
            output = "[bold red]No output received or tool failed to run.[/bold red]"
        self.console.print(Panel.fit(str(output), title=f"[bold green]{title}", border_style="cyan"))