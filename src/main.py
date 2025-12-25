import os
import json
import subprocess
from pathlib import Path
from litellm import completion
from coding_agent.tools import tools
from coding_agent.system_prompt import get_system_prompt

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def write_file(path: str, content: str, project_root: Path):
    """
    Tool for the LLM to write content into a file.
    Ensures files are only written inside project_root.
    """
    file_path = Path(project_root) / path

    file_path = file_path.resolve()
    if not str(file_path).startswith(str(project_root.resolve())):
        raise ValueError(f"Attempted to write outside of project root: {file_path}")

    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File written to {file_path}"

def read_file(path: str, project_root: Path) -> str:
    """
    Tool for the LLM to read content from a file.
    Ensures files are only read inside project_root.
    """
    file_path = Path(project_root) / path
    file_path = file_path.resolve()

    if not str(file_path).startswith(str(project_root.resolve())):
        raise ValueError(f"Attempted to read outside of project root: {file_path}")

    if not file_path.is_file():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def get_folder_structure(path: str) -> str:
    """
    Recursively lists the folder structure starting from `path`.
    Returns a nicely formatted string similar to `ls -R`.
    """
    path = Path(path)
    structure = []

    def recurse(p: Path, prefix=""):
        for item in sorted(p.iterdir()):
            if item.is_dir():
                structure.append(f"{prefix}{item.name}/")
                recurse(item, prefix + "  ")
            else:
                structure.append(f"{prefix}{item.name}")

    recurse(path)
    return "\n".join(structure)

def get_valid_project_root(prompt: str = "Please enter the root folder of your project: ") -> Path:
    """
    Prompts the user for a project root folder path.
    Validates that it is not empty, exists, and is a directory.
    Returns a Path object.
    """
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            print("Error: You must enter a path. Try again.")
            continue

        path_obj = Path(user_input)
        if not path_obj.exists():
            print(f"Error: The path '{user_input}' does not exist. Try again.")
            continue
        if not path_obj.is_dir():
            print(f"Error: The path '{user_input}' is not a directory. Try again.")
            continue

        return path_obj
    
def exec_command(command: str):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

def main():
    project_root = get_valid_project_root()
    project_structure = get_folder_structure(project_root)
    task = input("Please enter the task: ").strip()
    messages = [
    {
        "role": "system",
        "content": get_system_prompt(project_root=project_root)
    },
    {
        "role": "user",
        "content": f"""
TASK:
{task}

PROJECT STRUCTURE:
{project_structure}
"""
    }
]
    while True:
        response = completion(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        messages.append({
            "role": "assistant",
            "content": msg.content,
            "tool_calls": msg.tool_calls if msg.tool_calls else None
        })

        if msg.tool_calls:
            for call in msg.tool_calls:
                name = call.function.name
                args = json.loads(call.function.arguments)

                if name == "write_file":
                    result = write_file(**args, project_root=project_root)
                elif name == "exec_command":
                    result = exec_command(**args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                })
        else:
            messages.append(msg)
            if "DONE" in msg.content:
                break
if __name__ == "__main__":
    main()