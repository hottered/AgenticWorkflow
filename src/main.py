import os
from router_agent import AgentRouter
from utils import get_valid_project_root
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def main() -> None:
    """Main entry point for the multi-agent system."""
    try:
        try:
            project_root = get_valid_project_root()
        except Exception:
            project_root = None
            print("WARNING: Coding agent not available (project root not found).")

        router = AgentRouter(project_root)

        print("Multi-Agent System running!")
        print("Press 'exit' or 'quit' to leave the session.\n")

        while True:
            user_input = input("Ti: ").strip()

            if user_input.lower() in ["exit", "quit", "izlaz"]:
                print("Goodbye... :(")
                break

            if not user_input:
                continue

            response = router.route(user_input)
            print(f"\nAgent: {response}\n")

    except KeyboardInterrupt:
        print("\n\nOperation interrupted.")
    except Exception as e:
        print(f"Error: {e}")
        raise
    
if __name__ == "__main__":
    main()