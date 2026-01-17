from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import litellm

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

    def _get_completion(self, tools: Optional[List[Dict]] = None) -> Any:
        """
        Get completion from the LLM.

        Args:
            tools: Optional tools for the agent

        Returns:
            Completion response message
        """
        params = {
            "model": self.model,
            "messages": self.messages,
            "stream": False
        }

        if tools:
            params["tools"] = tools
            params["tool_choice"] = "auto"

        response = litellm.completion(**params)
        return response.choices[0].message

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