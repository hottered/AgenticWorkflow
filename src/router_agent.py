from typing import Optional
from coding_agent import CodingAgent
from conversation_agent import ConversationalAgent


class AgentRouter:
    """Routes user input to appropriate agent."""

    def __init__(self, project_root: Optional[str] = None):
        """
        Initialize agent router.

        Args:
            project_root: Optional project root for coding agent
        """
        self.conversational_agent = ConversationalAgent()
        self.coding_agent = CodingAgent(project_root) if project_root else None

    def _detect_intent(self, user_input: str) -> str:
        """
        Detect user intent.

        Args:
            user_input: User input

        Returns:
            Agent type: 'conversational' or 'coding'
        """
        coding_keywords = [
            "napravi", "kreiraj", "izmeni", "dodaj", "obriši",
            "refaktorisi", "debug", "popravi", "implementiraj",
            "kod", "fajl", "projekat", "funkciju", "klasu"
        ]

        user_input_lower = user_input.lower()

        for keyword in coding_keywords:
            if keyword in user_input_lower:
                return "coding"

        return "conversational"

    def route(self, user_input: str) -> str:
        """
        Route user input to appropriate agent.

        Args:
            user_input: User input

        Returns:
            Agent response
        """
        intent = self._detect_intent(user_input)

        if intent == "coding":
            if not self.coding_agent:
                return "Coding agent nije konfigurisan. Molim te podesi project_root."
            return self.coding_agent.run(user_input)
        else:
            return self.conversational_agent.run(user_input)
