from pathlib import Path

def get_valid_project_root(prompt: str = "Enter project root: ") -> Path:
    """Prompt user for valid project root."""
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            print("Error: Path cannot be empty.")
            continue
        
        path_obj = Path(user_input)
        if not path_obj.exists():
            print(f"Error: Path does not exist.")
            continue
        if not path_obj.is_dir():
            print(f"Error: Not a directory.")
            continue
        
        return path_obj
    
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
