#!/usr/bin/env python3
import requests
from core.tool_runner import ToolRunner
from core.output_presenter import OutputPresenter

def main():
    tool = ToolRunner("nmap", ["-v", "-A"], "192.168.1.1")
    output = tool.run()

    presenter = OutputPresenter()
    presenter.display("Nmap Scan", output)

if __name__ == "__main__":
    main()