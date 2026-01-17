from typing import List, Optional


class TaskCompletion:
    """Data class for task completion information."""
    
    def __init__(
        self,
        summary: str,
        files_modified: List[str],
        commands_executed: List[str],
        success: bool,
        next_steps: Optional[str] = None
    ):
        self.summary = summary
        self.files_modified = files_modified
        self.commands_executed = commands_executed
        self.success = success
        self.next_steps = next_steps
    
    def __str__(self) -> str:
        """Format task completion as readable string."""
        output = [
            "=" * 60,
            "TASK FINISHED" if self.success else "TASK FAILED",
            "=" * 60,
            "",
            "📋 SUMMARY:",
            self.summary,
            ""
        ]
        
        if self.files_modified:
            output.append("📁 MODIFIED/CREATED FILES:")
            for file in self.files_modified:
                output.append(f"  • {file}")
            output.append("")
        
        if self.commands_executed:
            output.append("⚙️  EXECUTED COMMANDS:")
            for cmd in self.commands_executed:
                output.append(f"  • {cmd}")
            output.append("")
        
        if self.next_steps:
            output.append("💡 NEXT STEPS:")
            output.append(self.next_steps)
            output.append("")
        
        output.append("=" * 60)
        
        return "\n".join(output)