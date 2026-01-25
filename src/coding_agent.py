import json
from base_agent import BaseAgent
from task_completion import TaskCompletion
from tools import tools
from project_tools import ProjectTools
from coding_agnet_system_prompt import get_system_prompt
from utils import get_folder_structure
from typing import Any, Dict, List, Optional

class CodingAgent(BaseAgent):
    """AI coding agent that executes tasks on a project."""

    def __init__(self, project_root: str, model: str = "gpt-4o-mini"):
        """
        Initialize the coding agent.

        Args:
            project_root: Root directory of the project
            model: LLM model to use
        """
        super().__init__(model)
        self.project_root = project_root
        self.project_tools = ProjectTools(project_root)
        self.task_completion: Optional[TaskCompletion] = None

    def _get_system_prompt(self) -> str:
        """Get system prompt for coding agent."""
        base_prompt = get_system_prompt(project_root=self.project_root)
        
        completion_instruction = """
IMPORTANT: When you completely finish the task, you MUST call the 'complete_task' tool with a detailed summary:
- State exactly what you did
- List all files you created or modified
- List all commands you executed
- Whether the task was completed successfully
- Any recommendations for next steps

Do NOT finish the task without calling the 'complete_task' tool.
"""
        
        return base_prompt + completion_instruction

    def _initialize_messages(self, task: str) -> None:
        """
        Initialize conversation messages.

        Args:
            task: User task description
        """
        project_structure = get_folder_structure(self.project_root)
        self.messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
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

    def _handle_complete_task(self, args: Dict[str, Any]) -> str:
        """
        Handle task completion.

        Args:
            args: Task completion arguments

        Returns:
            Confirmation message
        """
        self.task_completion = TaskCompletion(
            summary=args.get("summary", ""),
            files_modified=args.get("files_modified", []),
            commands_executed=args.get("commands_executed", []),
            success=args.get("success", True),
            next_steps=args.get("next_steps")
        )
        
        return "Task completion recorded. Summary will be displayed to user."

    def _execute_tool(self, name: str, args: Dict[str, Any]) -> Any:
        """
        Execute a tool function.

        Args:
            name: Tool name
            args: Tool arguments

        Returns:
            Tool execution result
        """
        if name == "complete_task":
            return self._handle_complete_task(args)
        
        tool_map = {
            "write_file": self.project_tools.write_file,
            "exec_command": self.project_tools.exec_command,
            "read_file": self.project_tools.read_file,
        }

        if name not in tool_map:
            raise ValueError(f"Unknown tool: {name}")

        return tool_map[name](**args)

    def _process_tool_calls(self, tool_calls: List[Any]) -> None:
        """
        Process all tool calls from the assistant.

        Args:
            tool_calls: List of tool calls to execute
        """
        for call in tool_calls:
            
            name = call.function.name
            args = json.loads(call.function.arguments)
            tool_call_id = call.id
        
            result = self._execute_tool(name, args)

            self.messages.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "content": str(result)
            })

    def _is_task_complete(self, content: str) -> bool:
        """
        Check if task is complete.

        Args:
            content: Message content to check

        Returns:
            True if task is complete, False otherwise
        """
        return content and "DONE" in content

    def run(self, task: str, stream: bool = True) -> str: 
        """
        Run the coding agent with the given task.

        Args:
            task: Task description
            stream: Whether to stream the response

        Returns:
            Final agent response with task completion summary
        """
        try:
            self._initialize_messages(task)
            self.task_completion = None
            self.set_stream_mode(stream)
            max_iterations = 20
            iteration = 0

            while iteration < max_iterations:
                iteration += 1
                
                try:
                    message = self._get_completion(tools=tools)
                except Exception as e:
                    return f"Error getting completion: {str(e)}"

                self.messages.append({
                    "role": "assistant",
                    "content": message.content,
                    "tool_calls": message.tool_calls if message.tool_calls else None
                })

                if message.tool_calls:
                    self._process_tool_calls(message.tool_calls)
                    
                    if self.task_completion:
                        return str(self.task_completion)
                else:
                    self.messages.append({
                        "role": "user",
                        "content": "Please call the 'complete_task' tool with a summary of everything you did."
                    })

            return "Task reached maximum iterations. No completion summary received."
            
        except Exception as e:
            error_msg = f"Error in coding agent: {str(e)}"
            print(error_msg)
            return error_msg