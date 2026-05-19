import subprocess
from pathlib import Path
from typing import Dict, Any

class ProjectTools:
    """Handles file system and command execution tools for the LLM agent."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root.resolve()
    
    def _validate_path(self, path: str) -> Path:
        """Ensures path is within project root."""
        file_path = (self.project_root / path).resolve()
        if not str(file_path).startswith(str(self.project_root)):
            raise ValueError(f"Attempted to access outside project root: {file_path}")
        return file_path
    
    def write_file(self, path: str, content: str) -> str:
        """Write content to a file within project root."""
        file_path = self._validate_path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File written to {file_path.relative_to(self.project_root)}"
    
    def read_file(self, path: str) -> str:
        """Read content from a file within project root."""
        file_path = self._validate_path(path)
        
        if not file_path.is_file():
            raise FileNotFoundError(f"File does not exist: {path}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    
    @staticmethod
    def confirm_command(command: str) -> bool:
        """Ask the user to confirm before running a shell command."""
        while True:
            answer = input(f"\nAre you sure you want to run `{command}`? (y/n): ").strip().lower()
            if answer == "y":
                return True
            elif answer == "n":
                print("Command skipped.")
                return False
            else:
                print("Please enter 'y' or 'n'.")
    
    def exec_command(self, command: str) -> Dict[str, Any]:
        """Execute a shell command and return results."""
        if not self.confirm_command(command):
            return {"stdout": "", "stderr": "Command execution cancelled by user.", "returncode": -1}
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=self.project_root
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }