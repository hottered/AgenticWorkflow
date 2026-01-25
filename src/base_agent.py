import litellm
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from models import StreamedMessage, ToolCall

class BaseAgent(ABC):
    """Base class for all agents."""

    def __init__(self, model: str = "gpt-4o-mini"):
        """
        Initialize the base agent.

        Args:
            model: LLM model to use
        """
        self.model = model
        self.messages = []
        self.stream = False
        
    @abstractmethod
    def _get_system_prompt(self) -> str:
        """
        Get system prompt for the agent.

        Returns:
            System prompt string
        """
        pass

    @abstractmethod
    def _initialize_messages(self, user_input: str) -> None:
        """
        Initialize conversation messages.

        Args:
            user_input: User input
        """
        pass

    def set_stream_mode(self, enabled: bool):
        """Enable or disable streaming mode."""
        self.stream_mode = enabled

    def _get_completion(self, tools: Optional[List[Dict]] = None) -> Any:
        """Get completion from LiteLLM."""
        params = {
            "model": self.model,
            "messages": self.messages,
            "stream": self.stream_mode,
        }
        if tools:
            params["tools"] = tools
        
        response = litellm.completion(**params)
        
        if self.stream_mode:
            return self._handle_streaming_response(response)
        else:
            return response.choices[0].message
        
    def _handle_streaming_response(self, stream):
        """Handle streaming response from LiteLLM."""
        collected_content = ""
        collected_tool_calls = []
        
        for chunk in stream:
            if not chunk.choices:
                continue
                
            delta = chunk.choices[0].delta
            
            if hasattr(delta, 'content') and delta.content:
                collected_content += delta.content
                print(delta.content, end="", flush=True)
            
            if hasattr(delta, 'tool_calls') and delta.tool_calls:
                for tool_call in delta.tool_calls:
                    idx = tool_call.index if hasattr(tool_call, 'index') else 0
                    
                    while len(collected_tool_calls) <= idx:
                        collected_tool_calls.append({
                            "id": None,
                            "type": "function",
                            "function": {
                                "name": "",
                                "arguments": ""
                            }
                        })
                    
                    if hasattr(tool_call, 'id') and tool_call.id:
                        collected_tool_calls[idx]["id"] = tool_call.id
                    
                    if hasattr(tool_call, 'function'):
                        if hasattr(tool_call.function, 'name') and tool_call.function.name:
                            collected_tool_calls[idx]["function"]["name"] = tool_call.function.name
                        if hasattr(tool_call.function, 'arguments') and tool_call.function.arguments:
                            collected_tool_calls[idx]["function"]["arguments"] += tool_call.function.arguments

        pydantic_tool_calls = None
        if collected_tool_calls:
            pydantic_tool_calls = [
                ToolCall(**tc) for tc in collected_tool_calls
            ]
        
        return StreamedMessage(
            content=collected_content if collected_content else None,
            tool_calls=pydantic_tool_calls
        )

    @abstractmethod
    def run(self, user_input: str) -> str:
        """
        Run the agent with user input.

        Args:
            user_input: User input

        Returns:
            Agent response
        """
        pass