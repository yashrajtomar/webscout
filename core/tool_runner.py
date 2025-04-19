import subprocess

class ToolRunner:
    def __init__(self, tool_name, switches, target):
        self.tool_name = tool_name
        self.switches = [switches] if isinstance(switches, str) else switches
        self.target = target
        print(f"Using {self.tool_name} on target {self.target}")

    def run(self):
        cmd = [self.tool_name] + self.switches + [self.target]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"[!] Error: {e.stderr.strip()}" 
