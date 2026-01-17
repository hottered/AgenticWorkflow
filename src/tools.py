tools = [
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file. Creates files and folders if they do not exist",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read content from a file. Only allowed inside the project root.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "exec_command",
            "description": "Execute a shell command, but if a user asks to write something into file do not use this tool for that",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string"}
                },
                "required": ["command"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "complete_task",
            "description": "Call this function when the task is completely finished. Provide a detailed summary of all actions taken.",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {
                        "type": "string",
                        "description": "Detailed summary of all completed actions, changes made, files created/modified, and any important notes"
                    },
                    "files_modified": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of all files that were created or modified"
                    },
                    "commands_executed": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of all commands that were executed"
                    },
                    "success": {
                        "type": "boolean",
                        "description": "Whether the task was completed successfully"
                    },
                    "next_steps": {
                        "type": "string",
                        "description": "Optional suggestions for next steps or follow-up actions"
                    }
                },
                "required": ["summary", "files_modified", "success"]
            }
        }
    }
]