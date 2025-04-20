from core.output_presenter import OutputPresenter
import subprocess

presenter = OutputPresenter()

def run(target, switches):
    cmd = ["httpx"] + switches + [target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def display(output):
    presenter.display_output("HTTPX Scan", output)