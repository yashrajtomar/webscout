from core.tool_runner import ToolRunner
from core.output_presenter import OutputPresenter

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import subprocess

console = Console()

def run(target, switches):
    cmd = ["nmap"] + switches + [target]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"[!] Error: {e.stderr.strip()}"

def display(output):
    lines = output.strip().split('\n')
    styled = Text()

    for line in lines:
        if "open" in line:
            styled.append(line + "\n", style="bold green")
        elif "closed" in line:
            styled.append(line + "\n", style="dim red")
        elif "filtered" in line:
            styled.append(line + "\n", style="yellow")
        elif "Nmap scan report for" in line:
            styled.append(line + "\n", style="bold cyan")
        else:
            styled.append(line + "\n")

    console.print(Panel(styled, title="Nmap Scan Results", border_style="blue"))