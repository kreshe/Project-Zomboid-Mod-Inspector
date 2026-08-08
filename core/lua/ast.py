from dataclasses import dataclass, field


@dataclass
class FunctionNode:

    class_name: str = ""

    method: str = ""

    line: int = 0

    local = False

    assignment = False

    override = False

    wraps_original = False

    events: list[str] = field(default_factory=list)