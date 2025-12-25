import os
import json
from litellm import completion
from coding_agent.tools import tools
from coding_agent.system_prompt import get_system_prompt
from coding_agent.utils import get_valid_project_root, get_folder_structure
from project_tools import ProjectTools

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def main():
    project_root = get_valid_project_root()
    project_structure = get_folder_structure(project_root)
    project_tools = ProjectTools(project_root)
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
                    result = project_tools.write_file(**args)
                elif name == "exec_command":
                    result = project_tools.exec_command(**args)
                elif name == "read_file":
                    result = project_tools.read_file(**args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                })
        else:
            messages.append(msg)
            if "DONE" in msg.content:
                print(msg.content)
                break

if __name__ == "__main__":
    main()