from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    messages: List[str]
    intent: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
