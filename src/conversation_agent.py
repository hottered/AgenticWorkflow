from base_agent import BaseAgent


class ConversationalAgent(BaseAgent):
    """Agent for casual conversation."""

    def _get_system_prompt(self) -> str:
        """Get system prompt for conversational agent."""

        return """You are a friendly conversational assistant.
        Respond naturally, warmly, and friendly to user messages.
        Be concise but considerate. You may use emojis if appropriate.
        Conversate in Serbian."""

    def _initialize_messages(self, user_input: str) -> None:
        """
        Initialize conversation messages.

        Args:
            user_input: User message
        """
        self.messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
            },
            {
                "role": "user",
                "content": user_input
            }
        ]

    def run(self, user_input: str) -> str:
        """
        Run conversational agent.

        Args:
            user_input: User message

        Returns:
            Agent response
        """
        self.set_stream_mode(False)  # Disable streaming for conversational agent
        self._initialize_messages(user_input)
        message = self._get_completion()
        return message.content