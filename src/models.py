from typing import List, Optional
from pydantic import BaseModel

class FunctionCall(BaseModel):
    name: str
    arguments: str

class ToolCall(BaseModel):
    id: str
    type: str
    function: FunctionCall

class StreamedMessage(BaseModel):
    content: Optional[str] = None
    tool_calls: Optional[List[ToolCall]] = None